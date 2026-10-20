try:
    import aiohttp
    import asyncio
except ImportError:
    CAN_WORK = False
else:
    CAN_WORK = True

import json
import time
from collections import OrderedDict

class TTLCache:
    """
    Простой LRU-кэш с ограничением по времени жизни (TTL) и максимальному размеру (maxsize).
    Используется для кэширования данных в библиотеке, чтобы избежать утечек памяти в долгоживущих процессах.
    """
    def __init__(self, maxsize: int = 100, ttl: float = 3600) -> None:
        self.cache = OrderedDict()
        self.maxsize = maxsize
        self.ttl = ttl

    def __contains__(self, key) -> bool:
        if key not in self.cache:
            return False
        value, timestamp = self.cache[key]
        if time.time() - timestamp > self.ttl:
            del self.cache[key]
            return False
        return True

    def __getitem__(self, key):
        value, timestamp = self.cache.pop(key)
        if time.time() - timestamp > self.ttl:
            raise KeyError(key)
        self.cache[key] = (value, timestamp)
        return value

    def __setitem__(self, key, value) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = (value, time.time())
        if len(self.cache) > self.maxsize:
            self.cache.popitem(last=False)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def clear(self):
        self.cache.clear()

class Response:
    """
    Класс для удобства использования AsyncSession
    Параметры:
    status, status_code, text, url
    """
    def __init__(self, status, text, url) -> None:
        self.status = status
        self.status_code = status
        self.text = text
        self.url = url

    def json(self):
        return json.loads(self.text)

class AsyncSession:
    """
    Класс-обертка для удобства использования асинхронных запросов
    """
    def __init__(self, proxy=None) -> None:
        if not CAN_WORK:
            raise ImportError("Невозможно получить доступ к библиотекам \"aiohttp\" и/или \"asyncio\". Проверьте правильность установки библиотеки.")
        self.proxy = proxy
        self._session = None

    async def _get_session(self):
        if self._session is None:
            if self.proxy and self.proxy.startswith('socks'):
                try:
                    from aiohttp_socks import ProxyConnector
                except ImportError:
                    raise ImportError("Для работы с proxy-серверами SOCKS требуется библиотека 'aiohttp_socks'. Установите ее с помощью 'pip install aiohttp_socks'")
                connector = ProxyConnector.from_url(self.proxy)
                self._session = aiohttp.ClientSession(connector=connector)
            else:
                self._session = aiohttp.ClientSession()
        return self._session

    async def _request(self, method: str, url: str, **kwargs) -> Response:
        session = await self._get_session()
        
        if self.proxy and not self.proxy.startswith('socks'):
            kwargs['proxy'] = self.proxy
            
        async with session.request(method=method, url=url, **kwargs) as response:
            return Response(response.status, await response.text(), str(response.url))

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()

    async def get(self, url: str, **kwargs) -> Response:
        return await self._request('get', url, **kwargs)
    
    async def post(self, url: str, **kwargs) -> Response:
        return await self._request('post', url, **kwargs)
    
    async def sleep(time: float): # Чтобы потом не импортировать asyncio отдельно
        await asyncio.sleep(time)


class KodikDomainManager:
    """
    Менеджер ротации и нормализации доменов плеера Kodik.
    Использует официальный сервис Kodik Replacer (https://domain.get-video-domain.com/domain/replace_v2.json)
    для автоматического отслеживания актуальных зеркал и предотвращения поломок при блокировках РКН.
    """
    DEFAULT_PLAYER_DOMAIN = "kodikplayer.com"
    REPLACE_API = "https://domain.get-video-domain.com/domain/replace_v2.json?domain=localhost"
    DEFAULT_REPLACEMENTS = {
        "//kodik.info/": "//kodikplayer.com/",
        "//kodik.org/": "//kodikplayer.com/",
        "//kodik.cc/": "//kodikplayer.com/",
        "//kodikdb.com/": "//kodikplayer.com/",
        "//anivod.com/": "//kodikplayer.com/",
        "//aniqit.com/": "//kodikplayer.com/",
        "//kodik.biz/": "//kodikplayer.com/",
        "//hdlizor.com/": "//kodikplayer.com/",
        "//hdrise.com/": "//kodikplayer.com/",
    }

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._replacements = cls.DEFAULT_REPLACEMENTS.copy()
            cls._instance._player_domain = cls.DEFAULT_PLAYER_DOMAIN
            cls._instance._last_update = 0
            cls._instance._update_interval = 1800  # 30 минут
        return cls._instance

    def normalize_url(self, url: str) -> str:
        """
        Заменяет любые устаревшие или заблокированные домены плеера Kodik на актуальный рабочий домен.
        Поддерживает форматы //domain/, http://domain/ и https://domain/.
        """
        if not url or not isinstance(url, str):
            return url

        for src, dst in self._replacements.items():
            if src in url:
                url = url.replace(src, dst)
            if src.startswith("//"):
                clean_src = src[2:]
                clean_dst = dst[2:]
                for proto in ("http://", "https://"):
                    old_prefix = proto + clean_src
                    new_prefix = proto + clean_dst
                    if old_prefix in url:
                        url = url.replace(old_prefix, new_prefix)
        return url

    def get_player_domain(self) -> str:
        """Возвращает текущий актуальный домен плеера (например, 'kodikplayer.com')"""
        return self._player_domain

    def update_sync(self, proxies=None) -> bool:
        """Синхронное обновление списка зеркал от официального сервиса Kodik"""
        now = time.time()
        if now - self._last_update < self._update_interval:
            return False
        # Фиксируем попытку сразу: при недоступности сервиса не блокируем каждую инициализацию парсера
        self._last_update = now
        try:
            import requests
            headers = {"User-Agent": "Kodik Replacer"}
            resp = requests.get(self.REPLACE_API, headers=headers, proxies=proxies, timeout=3)
            if resp.status_code == 200:
                data = resp.json()
                from_list = data.get("replace", {}).get("from", [])
                to_list = data.get("replace", {}).get("to", [])
                if from_list and to_list and len(from_list) == len(to_list):
                    for f, t in zip(from_list, to_list):
                        self._replacements[f] = t
                    if to_list:
                        clean = to_list[0].strip("/").split("/")[0]
                        if clean:
                            self._player_domain = clean
                    self._last_update = now
                    return True
        except Exception:
            pass
        return False

    async def update_async(self, async_session=None) -> bool:
        """Асинхронное обновление списка зеркал от официального сервиса Kodik"""
        now = time.time()
        if now - self._last_update < self._update_interval:
            return False
        self._last_update = now
        try:
            data = None
            if async_session is not None:
                resp = await async_session.get(self.REPLACE_API, headers={"User-Agent": "Kodik Replacer"})
                if resp.status_code == 200:
                    data = resp.json()
            elif CAN_WORK:
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.REPLACE_API, headers={"User-Agent": "Kodik Replacer"}, timeout=aiohttp.ClientTimeout(total=3)) as resp:
                        if resp.status == 200:
                            data = await resp.json()
            if data:
                from_list = data.get("replace", {}).get("from", [])
                to_list = data.get("replace", {}).get("to", [])
                if from_list and to_list and len(from_list) == len(to_list):
                    for f, t in zip(from_list, to_list):
                        self._replacements[f] = t
                    if to_list:
                        clean = to_list[0].strip("/").split("/")[0]
                        if clean:
                            self._player_domain = clean
                    self._last_update = now
                    return True
        except Exception:
            pass
        return False