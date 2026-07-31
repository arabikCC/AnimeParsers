from src.anime_parsers_ru import ShikimoriParser, ShikimoriParserAsync, errors
from time import sleep
import asyncio

def sync_test(delay: float, GLOBAL_USE_LXML: bool = False, mirror: str | None = None, proxy: str | None = None):
    from src.anime_parsers_ru import ShikimoriParser

    try_errors = 0
    try_succes = 0

    parser = ShikimoriParser(GLOBAL_USE_LXML, mirror=mirror, proxy=proxy)

    try:
        data = parser.search("Кулинарные скитания")
        if type(data) != list:
            raise AssertionError('Type of data is not list. Type:', type(data))
        if len(data) == 0:
            raise AssertionError('Length of data == 0')
        if type(data[0]) != dict:
            raise AssertionError('Type of data[0] is not dict. Type:', type(data[0]))
    except Exception as ex:
        print(f'[FAIL] Search "Кулинарные скитания". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Search "Кулинарные скитания"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.search("Наруто")
        if type(data) != list:
            raise AssertionError('Type of data is not list. Type:', type(data))
        if len(data) == 0:
            raise AssertionError('Length of data == 0')
        if type(data[0]) != dict:
            raise AssertionError('Type of data[0] is not dict. Type:', type(data[0]))
    except Exception as ex:
        print(f'[FAIL] Search "Наруто". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Search "Наруто"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.search("Класс превосходства")
        if type(data) != list:
            raise AssertionError('Type of data is not list. Type:', type(data))
        if len(data) == 0:
            raise AssertionError('Length of data == 0')
        if type(data[0]) != dict:
            raise AssertionError('Type of data[0] is not dict. Type:', type(data[0]))
    except Exception as ex:
        print(f'[FAIL] Search "Класс превосходства". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Search "Класс превосходства"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.search("Клинок рассекающий демонов")
        if type(data) != list:
            raise AssertionError('Type of data is not list. Type:', type(data))
        if len(data) == 0:
            raise AssertionError('Length of data == 0')
        if type(data[0]) != dict:
            raise AssertionError('Type of data[0] is not dict. Type:', type(data[0]))
    except Exception as ex:
        print(f'[FAIL] Search "Клинок рассекающий демонов". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Search "Клинок рассекающий демонов"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.anime_info('https://shikimori.one/animes/z20-naruto')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Info "z20". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Info "z20"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.anime_info('https://shikimori.one/animes/53446-tondemo-skill-de-isekai-hourou-meshi')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Info "53446". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Info "53446"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.anime_info('https://shikimori.one/animes/58426-shikanoko-nokonoko-koshitantan')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Info "58426". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Info "58426"')
        try_succes += 1
    sleep(delay)
    
    try:
        data = parser.anime_info('https://shikimori.one/animes/z40456-kimetsu-no-yaiba-movie-mugen-ressha-hen')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Info "z40456". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Info "z40456"')
        try_succes += 1
    sleep(delay)

    # Проверка на ограничение по возрасту (все поудаляли, не актуально)
    """
    try:
        data = parser.anime_info('https://shikimori.one/animes/53725-class-de-otoko-wa-boku-ichinin')
    except errors.AgeRestricted:
        print('[OK] Info "53725". AgeRestricted block works')
    except Exception as ex:
        print(f'[FAIL] Info "53725". Непредвиденная ошибка "{ex}". Ожидалось: "AgeRestricted"')
        try_errors += 1
    else:
        print('[FAIL] Info "53725". Обработка ограниченного по возрасту аниме не вернуло ошибку. Ожидалось: "AgeRestricted"')
        try_succes += 1
    sleep(delay)
    """    
    
    try:
        data = parser.additional_anime_info('https://shikimori.one/animes/z20-naruto')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
        if len(data['related']) == 0:
            raise AssertionError('Length of data[\'related\'] == 0')
    except Exception as ex:
        print(f'[FAIL] Additional info "z20". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Additional info "z20"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.additional_anime_info('https://shikimori.one/animes/z40456-kimetsu-no-yaiba-movie-mugen-ressha-hen')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Additional info "z40456". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Additional info "z40456"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.additional_anime_info('https://shikimori.one/animes/53446-tondemo-skill-de-isekai-hourou-meshi')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
        if len(data['main_characters']) == 0:
            raise AssertionError('Length of data[\'main_characters\'] == 0')
    except Exception as ex:
        print(f'[FAIL] Additional info "53446". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Additional info "53446"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.link_by_id('20') # Наруто (реальный id - z20)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Link by id "20". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Link by id "20"')
        try_succes += 1
    sleep(delay)
    
    try:
        data = parser.link_by_id('40456') # Клинок, рассекающий демонов: Бесконечный поезд. Фильм (реальный id - z40456)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Link by id "40456". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Link by id "40456"')
        try_succes += 1
    sleep(delay)
    
    try:
        data = parser.link_by_id('58426') # Моя подруга-олениха Нокотан (реальный id - 58426)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Link by id "58426". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Link by id "58426"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.link_by_id('53446') # Кулинарные скитания в параллельном мире (реальный id - 53446)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Link by id "53446". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Link by id "53446"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.id_by_link('https://shikimori.one/animes/z20-naruto') # Наруто (реальный id - z20 ожидаем - 20)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
        if data != "20":
            raise AssertionError('data != 20. data =', data)
    except Exception as ex:
        print(f'[FAIL] Id by link "z20". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Id by link "z20"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.id_by_link('https://shikimori.one/animes/z40456-kimetsu-no-yaiba-movie-mugen-ressha-hen') # Клинок, рассекающий демонов: Бесконечный поезд. Фильм (реальный id - z40456 ожидаем - 40456)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
        if data != "40456":
            raise AssertionError('data != 40456. data =', data)
    except Exception as ex:
        print(f'[FAIL] Id by link "z40456". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Id by link "z40456"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.id_by_link('https://shikimori.one/animes/58426-shikanoko-nokonoko-koshitantan') # Моя подруга-олениха Нокотан (реальный id - 58426 ожидаем - 58426)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
        if data != "58426":
            raise AssertionError('data != 58426. data =', data)
    except Exception as ex:
        print(f'[FAIL] Id by link "58426". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Id by link "58426"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list()
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(status=['ongoing'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list ongoing. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list ongoing')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(status=['released'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list released. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list released')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(status=['released', 'ongoing'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list released & ongoing. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list released & ongoing')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(anime_type=['tv'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type tv. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type tv')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(anime_type=['movie'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] != 'Фильм':
            raise AssertionError(f"data[0]['type'] != 'Фильм'. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type movie. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type movie')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(anime_type=['movie', 'tv'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] != 'Фильм' and data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал'] and not 'Фильм'. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type movie | tv. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type movie | tv')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(status=['ongoing'], anime_type=['tv'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type ongoing tv. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type ongoing tv')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(status=['ongoing'], anime_type=['tv'], start_page=3, page_limit=2, sort_by='popularity')
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type ongoing tv with pages and sort. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type ongoing tv with pages and sort')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(status=['ongoing'], anime_type=['tv'], rating='pg_13', genres=['2-Adventure'], start_page=1, page_limit=2, sort_by='popularity')
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type ongoing tv with pages, sort, pg rating, genres. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type ongoing tv with pages, sort, pg rating, genres')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(status=['!ongoing'], anime_type=['!tv'], rating='!pg_13', genres=['!2-Adventure'], start_page=1, page_limit=1, sort_by='popularity')
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] in ['TV Сериал', 'ТВ Сериал']")
    except Exception as ex:
        print(f'[FAIL] Anime list type !ongoing !tv with pages, sort, !pg rating, !genres. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type !ongoing !tv with pages, sort, !pg rating, !genres')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(status=['ongoing'], anime_type=['tv'], genres=['Приключения'], start_page=1, page_limit=1, sort_by='popularity')
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']")
    except Exception as ex:
        print(f'[FAIL] Anime list type ongoing tv with pages, sort, ru genres. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type ongoing tv with pages, sort, ru genres')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(seasons=['winter_2026', '2023'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with seasons. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with seasons')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(duration='S')
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with duration S. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with duration S')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(duration=['S', 'D'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with duration [\'S\', \'D\']. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with duration [\'S\', \'D\']')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(origin=['web_novel'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with origin web_novel. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with origin web_novel')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(studios=['11-Madhouse'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with studio 11-Madhouse. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with studio 11-Madhouse')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(licensed=['Crunchyroll'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with licensed Crunchyroll. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with licensed Crunchyroll')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(rating_from=5)
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with rating from 5. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with rating from 5')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(rating_to=5)
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with rating to 5. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with rating to 5')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.get_anime_list(rating_from=5, rating_to=7)
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with rating from 5 and rating_to 7. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with rating from 5 and rating_to 7')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.deep_search('Кулинарные скитания', {}, ['id', 'name', 'url', 'genres { name russian }'])
        if type(data) != list:
            raise AssertionError('Type of data is not list. Type:', type(data))
        if len(data) == 0:
            raise AssertionError('Length of data == 0')
        if type(data[0]) != dict:
            raise AssertionError('Type of data[0] is not dict. Type:', type(data[0]))
    except Exception as ex:
        print(f'[FAIL] Deep search. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Deep search')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.deep_anime_info('53446', ['id', 'name', 'url', 'genres { name russian }'])
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
        if type(data['name']) != str:
            raise AssertionError('Type of data[\'name\'] is not str. Type:', type(data['name']))
    except Exception as ex:
        print(f'[FAIL] Deep info. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Deep info')
        try_succes += 1
    sleep(delay)

    try: # Проверка на несуществующем id
        data = parser.deep_anime_info('fff', ['id', 'name', 'url', 'genres { name russian }'])
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
        if type(data['name']) != str:
            raise AssertionError('Type of data[\'name\'] is not str. Type:', type(data['name']))
    except errors.NoResults:
        print('[OK] Deep info with unknown id')
        try_succes += 1
    except Exception as ex:
        print(f'[FAIL] Deep info with unknown id. Exception: {ex}')
        try_errors += 1
    else:
        print(f'[FAIL] Deep info with unknown id. Expected NoResults exception but no exception was triggered')
        try_errors += 1
    sleep(delay)

    return (try_errors, try_succes)

async def async_test(delay: float, GLOBAL_USE_LXML: bool = False, mirror: str | None = None, proxy: str | None = None):
    from src.anime_parsers_ru import ShikimoriParserAsync

    try_errors = 0
    try_succes = 0

    parser = ShikimoriParserAsync(GLOBAL_USE_LXML, mirror=mirror, proxy=proxy)

    try:
        data = await parser.search("Кулинарные скитания")
        if type(data) != list:
            raise AssertionError('Type of data is not list. Type:', type(data))
        if len(data) == 0:
            raise AssertionError('Length of data == 0')
        if type(data[0]) != dict:
            raise AssertionError('Type of data[0] is not dict. Type:', type(data[0]))
    except Exception as ex:
        print(f'[FAIL] Search "Кулинарные скитания". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Search "Кулинарные скитания"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.search("Наруто")
        if type(data) != list:
            raise AssertionError('Type of data is not list. Type:', type(data))
        if len(data) == 0:
            raise AssertionError('Length of data == 0')
        if type(data[0]) != dict:
            raise AssertionError('Type of data[0] is not dict. Type:', type(data[0]))
    except Exception as ex:
        print(f'[FAIL] Search "Наруто". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Search "Наруто"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.search("Класс превосходства")
        if type(data) != list:
            raise AssertionError('Type of data is not list. Type:', type(data))
        if len(data) == 0:
            raise AssertionError('Length of data == 0')
        if type(data[0]) != dict:
            raise AssertionError('Type of data[0] is not dict. Type:', type(data[0]))
    except Exception as ex:
        print(f'[FAIL] Search "Класс превосходства". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Search "Класс превосходства"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.search("Клинок рассекающий демонов")
        if type(data) != list:
            raise AssertionError('Type of data is not list. Type:', type(data))
        if len(data) == 0:
            raise AssertionError('Length of data == 0')
        if type(data[0]) != dict:
            raise AssertionError('Type of data[0] is not dict. Type:', type(data[0]))
    except Exception as ex:
        print(f'[FAIL] Search "Клинок рассекающий демонов". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Search "Клинок рассекающий демонов"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.anime_info('https://shikimori.one/animes/z20-naruto')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Info "z20". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Info "z20"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.anime_info('https://shikimori.one/animes/53446-tondemo-skill-de-isekai-hourou-meshi')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Info "53446". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Info "53446"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.anime_info('https://shikimori.one/animes/58426-shikanoko-nokonoko-koshitantan')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Info "58426". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Info "58426"')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.anime_info('https://shikimori.one/animes/z40456-kimetsu-no-yaiba-movie-mugen-ressha-hen')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Info "z40456". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Info "z40456"')
        try_succes += 1
    sleep(delay)

    # Проверка на ограничение по возрасту (все поудаляли, не актуально)
    """
    try:
        data = await parser.anime_info('https://shikimori.one/animes/53725-class-de-otoko-wa-boku-ichinin')
    except errors.AgeRestricted:
        print('[OK] Info "53725". AgeRestricted block works')
    except Exception as ex:
        print(f'[FAIL] Info "53725". Непредвиденная ошибка "{ex}". Ожидалось: "AgeRestricted"')
        try_errors += 1
    else:
        print('[FAIL] Info "53725". Обработка ограниченного по возрасту аниме не вернуло ошибку. Ожидалось: "AgeRestricted"')
        try_succes += 1
    sleep(delay)
    """
    try:
        data = await parser.additional_anime_info('https://shikimori.one/animes/z20-naruto')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
        if len(data['related']) == 0:
            raise AssertionError('Length of data[\'related\'] == 0')
    except Exception as ex:
        print(f'[FAIL] Additional info "z20". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Additional info "z20"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.additional_anime_info('https://shikimori.one/animes/z40456-kimetsu-no-yaiba-movie-mugen-ressha-hen')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Additional info "z40456". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Additional info "z40456"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.additional_anime_info('https://shikimori.one/animes/53446-tondemo-skill-de-isekai-hourou-meshi')
        if type(data) != dict:
            raise AssertionError('Type of data is not dict. Type:', type(data))
        if len(data['main_characters']) == 0:
            raise AssertionError('Length of data[\'main_characters\'] == 0')
    except Exception as ex:
        print(f'[FAIL] Additional info "53446". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Additional info "53446"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.link_by_id('20') # Наруто (реальный id - z20)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Link by id "20". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Link by id "20"')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.link_by_id('40456') # Клинок, рассекающий демонов: Бесконечный поезд. Фильм (реальный id - z40456)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Link by id "40456". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Link by id "40456"')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.link_by_id('58426') # Моя подруга-олениха Нокотан (реальный id - 58426)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Link by id "58426". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Link by id "58426"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.link_by_id('53446') # Кулинарные скитания в параллельном мире (реальный id - 53446)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
    except Exception as ex:
        print(f'[FAIL] Link by id "53446". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Link by id "53446"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.id_by_link('https://shikimori.one/animes/z20-naruto') # Наруто (реальный id - z20 ожидаем - 20)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
        if data != "20":
            raise AssertionError('data != 20. Data =', data)
    except Exception as ex:
        print(f'[FAIL] Id by link "z20". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Id by link "z20"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.id_by_link('https://shikimori.one/animes/z40456-kimetsu-no-yaiba-movie-mugen-ressha-hen') # Клинок, рассекающий демонов: Бесконечный поезд. Фильм (реальный id - z40456 ожидаем - 40456)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
        if data != "40456":
            raise AssertionError('data != 40456. Data =', data)
    except Exception as ex:
        print(f'[FAIL] Id by link "z40456". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Id by link "z40456"')
        try_succes += 1
    sleep(delay)

    try:
        data = parser.id_by_link('https://shikimori.one/animes/58426-shikanoko-nokonoko-koshitantan') # Моя подруга-олениха Нокотан (реальный id - 58426 ожидаем - 58426)
        if type(data) != str:
            raise AssertionError('Type of data is not str. Type:', type(data))
        if data != "58426":
            raise AssertionError('data != 58426. Data =', data)
    except Exception as ex:
        print(f'[FAIL] Id by link "58426". Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Id by link "58426"')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list()
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(status=['ongoing'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list ongoing. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list ongoing')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(status=['released'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list released. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list released')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(status=['released', 'ongoing'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list released & ongoing. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list released & ongoing')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(anime_type=['tv'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type tv. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type tv')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(anime_type=['movie'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] != 'Фильм':
            raise AssertionError(f"data[0]['type'] != 'Фильм'. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type movie. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type movie')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(anime_type=['movie', 'tv'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] != 'Фильм' and data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал'] and not 'Фильм'. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type movie | tv. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type movie | tv')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(status=['ongoing'], anime_type=['tv'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type ongoing tv. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type ongoing tv')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(status=['ongoing'], anime_type=['tv'], start_page=3, page_limit=2, sort_by='popularity')
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type ongoing tv with pages and sort. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type ongoing tv with pages and sort')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(status=['ongoing'], anime_type=['tv'], rating='pg_13', genres=['2-Adventure'], start_page=1, page_limit=2, sort_by='popularity')
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']. ->: {data[0]['type']}")
    except Exception as ex:
        print(f'[FAIL] Anime list type ongoing tv with pages, sort, pg rating, genres. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type ongoing tv with pages, sort, pg rating, genres')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(status=['!ongoing'], anime_type=['!tv'], rating='!pg_13', genres=['!2-Adventure'], start_page=1, page_limit=1, sort_by='popularity')
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] in ['TV Сериал', 'ТВ Сериал']")
    except Exception as ex:
        print(f'[FAIL] Anime list type !ongoing !tv with pages, sort, !pg rating, !genres. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type !ongoing !tv with pages, sort, !pg rating, !genres')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.get_anime_list(status=['ongoing'], anime_type=['tv'], genres=['Приключения'], start_page=1, page_limit=1, sort_by='popularity')
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
        if data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']:
            raise AssertionError(f"data[0]['type'] not in ['TV Сериал', 'ТВ Сериал']")
    except Exception as ex:
        print(f'[FAIL] Anime list type ongoing tv with pages, sort, ru genres. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list type ongoing tv with pages, sort, ru genres')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.get_anime_list(seasons=['winter_2026', 'winter_2023'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with seasons. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with seasons')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.get_anime_list(duration='S')
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with duration S. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with duration S')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.get_anime_list(duration=['S', 'D'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with duration [\'S\', \'D\']. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with duration [\'S\', \'D\']')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.get_anime_list(origin=['web_novel'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with origin web_novel. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with origin web_novel')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.get_anime_list(studios=['11-Madhouse'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with studio 11-Madhouse. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with studio 11-Madhouse')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.get_anime_list(licensed=['Crunchyroll'])
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with licensed Crunchyroll. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with licensed Crunchyroll')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.get_anime_list(rating_from=5)
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with rating from 5. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with rating from 5')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.get_anime_list(rating_to=5)
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with rating to 5. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with rating to 5')
        try_succes += 1
    sleep(delay)
    
    try:
        data = await parser.get_anime_list(rating_from=5, rating_to=7)
        if len(data) == 0:
            raise AssertionError("Len data == 0")
        if type(data) != list:
            raise AssertionError(f"typeof data != list. Type: {type(data)}")
        if type(data[0]) != dict:
            raise AssertionError(f"typeof data[0] != dict. Type: {type(data[0])}")
    except Exception as ex:
        print(f'[FAIL] Anime list with rating from 5 and rating_to 7. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Anime list with rating from 5 and rating_to 7')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.deep_search('Кулинарные скитания', {}, ['id', 'name', 'url', 'genres { name russian }'])
        if type(data) != list:
            raise AssertionError('Type of data is not a list. Type:', type(data))
        if len(data) == 0:
            raise AssertionError('Length of data is 0')
        if type(data[0]) != dict:
            raise AssertionError('Type of data[0] is not a dict. Type:', type(data[0]))
    except Exception as ex:
        print(f'[FAIL] Deep search. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Deep search')
        try_succes += 1
    sleep(delay)

    try:
        data = await parser.deep_anime_info('53446', ['id', 'name', 'url', 'genres { name russian }'])
        if type(data) != dict:
            raise AssertionError('Type of data is not a dict. Type:', type(data))
        if type(data['name']) != str:
            raise AssertionError('Type of data[\'name\'] is not str. Type:', type(data['name']))
    except Exception as ex:
        print(f'[FAIL] Deep info. Exception: {ex}')
        try_errors += 1
    else:
        print('[OK] Deep info')
        try_succes += 1
    sleep(delay)

    try: # Проверка на несуществующем id
        data = await parser.deep_anime_info('fff', ['id', 'name', 'url', 'genres { name russian }'])
        if type(data) != dict:
            raise AssertionError('Type of data is not a dict. Type:', type(data))
        if type(data['name']) != str:
            raise AssertionError('Type of data[\'name\'] is not str. Type:', type(data['name']))
    except errors.NoResults:
        print('[OK] Deep info with unknown id')
    except Exception as ex:
        print(f'[FAIL] Deep info with unknown id. Exception: {ex}')
        try_errors += 1
    else:
        print(f'[FAIL] Deep info with unknown id. Expected NoResults exception but no exception was triggered')
        try_succes += 1
    sleep(delay)

    await parser.close_async_session()
    return (try_errors, try_succes)