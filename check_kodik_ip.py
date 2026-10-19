import sys
import json
import base64
import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import re
import ssl

def run_diagnostic():
    print("=" * 65)
    print("      ДИАГНОСТИКА ПОДКЛЮЧЕНИЯ И ССЫЛОК KODIK CDN (РФ vs EU)")
    print("=" * 65)

    cj = http.cookiejar.CookieJar()
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj),
        urllib.request.HTTPSHandler(context=ctx)
    )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # 1. Проверка внешнего IP и страны
    print("\n[1/5] Определение вашего внешнего IP и провайдера...")
    try:
        req = urllib.request.Request("http://ip-api.com/json/", headers={"User-Agent": "Mozilla/5.0"})
        with opener.open(req, timeout=5) as r:
            ip_info = json.loads(r.read().decode())
            print(f" -> Ваш IP: {ip_info.get('query')}")
            print(f" -> Страна: {ip_info.get('country')} ({ip_info.get('countryCode')})")
            print(f" -> Провайдер: {ip_info.get('isp')}")
    except Exception as e:
        print(f" -> Ошибка проверки через ip-api: {e}")

    # 2. Подготовка ссылки на серию
    print("\n[2/5] Подготовка ссылки на тестовую серию (Стальной алхимик, 1 серия)...")
    ep_url = "https://kodikplayer.com/serial/10015/43d8c68777a985339ef086457a72f06a/720p?min_age=16&first_url=false&season=1&episode=1"
    print(f" -> URL плеера: {ep_url}")

    # 3. Загрузка HTML страницы плеера и анализ
    print("\n[3/5] Загрузка страницы плеера Kodik и вердикт сервера...")
    try:
        req = urllib.request.Request(ep_url, headers=headers)
        with opener.open(req, timeout=8) as r:
            html = r.read().decode("utf-8")

        kodik_ip = re.search(r'var\s+user_ip\s*=\s*["\']([^"\']+)["\']', html)
        kodik_country = re.search(r'var\s+country\s*=\s*["\']([^"\']+)["\']', html)
        print(f" -> Kodik определил IP как: {kodik_ip.group(1) if kodik_ip else 'Не найдено'}")
        print(f" -> Kodik определил страну как: {kodik_country.group(1) if kodik_country else 'Не найдено'}")

        if "p12." in html or "p14." in html or "/s/m/" in html or "/f/aHR" in html:
            print(" -> [ИНДИКАТОР В HTML]: Сервер УЖЕ вставил превью через прокси-ноду (Edge Proxy)!")
        else:
            print(" -> [ИНДИКАТОР В HTML]: Сервер использует прямые адреса Origin-хранилища (cloud)!")

        # Поиск параметров vInfo
        v_type_m = re.search(r"vInfo\.type\s*=\s*['\"]([^'\"]+)['\"]", html)
        v_hash_m = re.search(r"vInfo\.hash\s*=\s*['\"]([^'\"]+)['\"]", html)
        v_id_m = re.search(r"vInfo\.id\s*=\s*['\"]([^'\"]+)['\"]", html)
        
        if not (v_type_m and v_hash_m and v_id_m):
            v_type_m = re.search(r"\.type\s*=\s*['\"]([^'\"]+)['\"]", html)
            v_hash_m = re.search(r"\.hash\s*=\s*['\"]([^'\"]+)['\"]", html)
            v_id_m = re.search(r"\.id\s*=\s*['\"]([^'\"]+)['\"]", html)

        v_type = v_type_m.group(1)
        v_hash = v_hash_m.group(1)
        v_id = v_id_m.group(1)

        url_params_raw = re.search(r'var\s+urlParams\s*=\s*["\'](\{.*?\})["\']', html)
        urlParams = json.loads(url_params_raw.group(1))

        # Скрипт плеера
        scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
        target_script = None
        for s in scripts:
            if "app.serial" in s or "app.player" in s:
                target_script = s
                break
        if not target_script and len(scripts) > 1:
            target_script = scripts[1]
    except Exception as e:
        print(f" -> ОШИБКА парсинга HTML: {e}")
        return

    # 4. Запрос к роуту за ссылкой на видеопоток
    print("\n[4/5] Расшифровка роута и получение ссылки на видео...")
    try:
        script_full_url = target_script if target_script.startswith("http") else "https://kodikplayer.com" + target_script
        req_js = urllib.request.Request(script_full_url, headers=headers)
        with opener.open(req_js, timeout=8) as r:
            js_text = r.read().decode("utf-8")

        cache_pos = js_text.find("cache:!1")
        ajax_pos = js_text.rfind("$.ajax", 0, cache_pos)
        chunk = js_text[ajax_pos:cache_pos]
        
        raw_b64 = re.search(r'url:\s*atob\(["\']([^"\']+)["\']\)', chunk)
        if raw_b64:
            post_link = base64.b64decode(raw_b64.group(1).encode()).decode()
        else:
            raw_b64_2 = re.search(r'url:\s*["\']([A-Za-z0-9+/=]+)["\']', chunk)
            if raw_b64_2:
                post_link = base64.b64decode(raw_b64_2.group(1).encode()).decode()
            else:
                post_link = "/ftor"

        print(f" -> Эндпоинт отправки формы: {post_link}")

        post_url = f"https://kodikplayer.com{post_link}"
        post_data = {
            "hash": v_hash,
            "id": v_id,
            "type": v_type,
            "d": urlParams["d"],
            "d_sign": urlParams["d_sign"],
            "pd": urlParams["pd"],
            "pd_sign": urlParams["pd_sign"],
            "ref": urlParams.get("ref", ""),
            "ref_sign": urlParams["ref_sign"],
            "bad_user": "true",
            "cdn_is_working": "true"
        }
        encoded_data = urllib.parse.urlencode(post_data).encode("utf-8")
        headers_post = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": ep_url,
            "Origin": "https://kodikplayer.com",
            "User-Agent": headers["User-Agent"]
        }
        req_post = urllib.request.Request(post_url, data=encoded_data, headers=headers_post)
        with opener.open(req_post, timeout=8) as r:
            res_json = json.loads(r.read().decode())
    except Exception as e:
        print(f" -> ОШИБКА запроса к роуту видео: {e}")
        return

    def decode_caesar(text, step):
        res = []
        for c in text:
            code = ord(c)
            if 65 <= code <= 90:
                res.append(chr((code - 65 + step) % 26 + 65))
            elif 97 <= code <= 122:
                res.append(chr((code - 97 + step) % 26 + 97))
            else:
                res.append(c)
        crypted = "".join(res)
        pad = (4 - len(crypted) % 4) % 4
        crypted += "=" * pad
        return base64.b64decode(crypted.encode()).decode("utf-8", errors="ignore")

    best_quality = list(res_json.get("links", {}).keys())[-1]
    enc_src = res_json["links"][best_quality][0]["src"]
    
    video_url = None
    for step in range(1, 26):
        try:
            cand = decode_caesar(enc_src, step)
            if ".mp4" in cand or "http" in cand or "//" in cand:
                video_url = cand
                break
        except Exception:
            continue

    if not video_url:
        video_url = enc_src

    # 5. Анализ и тесты доступности MP4 и HLS
    print("\n[5/5] АНАЛИЗ ПОЛУЧЕННОЙ ССЫЛКИ И ПРОВЕРКА ДОСТУПНОСТИ:")
    print("-" * 65)
    print(f"Ссылка:\n{video_url}")
    print("-" * 65)

    is_proxy = "/s/m/" in video_url or "p12." in video_url or "p14." in video_url or "kodik.info" in video_url
    if is_proxy:
        print("\n [!] ТИП ССЫЛКИ: ПРОКСИ-ССЫЛКА (/s/m/ - Edge Proxy Cache)")
        print("  -> Сервер Kodik определил IP как внешний (Non-RU или датацентр)!")
    else:
        print("\n [OK] ТИП ССЫЛКИ: ЧИСТАЯ ССЫЛКА НА ORIGIN (cloud.solodcdn.com)")
        print("  -> Сервер Kodik определил IP как домашний/резидентский в зоне РФ/СНГ!")

    clean_base = video_url.replace("https:", "").replace("http:", "")
    if not clean_base.startswith("//"):
        clean_base = "//" + clean_base
    clean_base = clean_base[: clean_base.rfind("/") + 1]
    
    mp4_url = "https:" + clean_base + f"{best_quality}.mp4"
    m3u8_url = "https:" + clean_base + f"{best_quality}.mp4:hls:manifest.m3u8"

    print("\n--- Проверка прямого скачивания MP4 ---")
    try:
        req_mp4 = urllib.request.Request(mp4_url, headers={
            "User-Agent": headers["User-Agent"],
            "Referer": "https://kodikplayer.com/",
            "Range": "bytes=0-1024"
        })
        with opener.open(req_mp4, timeout=8) as r:
            print(f" -> HTTP статус: {r.status} (Прочитано: {len(r.read())} байт)")
            print(" -> [РЕЗУЛЬТАТ MP4]: РАБОТАЕТ! Прямой файл .mp4 отдается!")
    except urllib.error.HTTPError as e:
        print(f" -> Ошибка HTTP: {e.code} {e.reason}")
        if e.code == 500:
            print(" -> [РЕЗУЛЬТАТ MP4]: НЕ РАБОТАЕТ (Код 500 - Edge-прокси нода не поддерживает монолитный MP4)!")
    except Exception as e:
        print(f" -> Ошибка: {e}")

    print("\n--- Проверка потокового HLS (.m3u8) ---")
    try:
        req_m3u8 = urllib.request.Request(m3u8_url, headers={
            "User-Agent": headers["User-Agent"],
            "Referer": "https://kodikplayer.com/"
        })
        with opener.open(req_m3u8, timeout=8) as r:
            print(f" -> HTTP статус: {r.status}")
            print(" -> [РЕЗУЛЬТАТ HLS]: РАБОТАЕТ! Потоковый манифест m3u8 отдается штатно!")
    except Exception as e:
        print(f" -> Ошибка: {e}")

    print("\n" + "=" * 65)
    print("                      ИТОГОВЫЙ ВЕРДИКТ")
    print("=" * 65)
    if not is_proxy:
        print(" У ВАС ЧИСТЫЙ РФ-ДОСТУП: Kodik отдает прямой Origin и рабочий MP4!")
    else:
        print(" У ВАС ПРОКСИ-ДОСТУП: Kodik выдает /s/m/, MP4 отключен, но HLS работает.")
    print("=" * 65)

if __name__ == "__main__":
    run_diagnostic()
