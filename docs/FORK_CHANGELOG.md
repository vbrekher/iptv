# IPTV Bunny Public Hub — история изменений

**Дата оформления витрины:** 2026-11-02
**Форк:** https://github.com/vbrekher/iptv
**Оригинальный проект:** https://github.com/iptv-org/iptv

## Девять объединённых PR

| Pull Request | Что мы изменили |
|---|---|
| [#1 · Personal Bunny Playlists](https://github.com/vbrekher/iptv/pull/1) | Отдельная Python-сборка M3U, исторические 18+ кандидаты, категории, Bunny Storage |
| [#2 · Free HLS Filter](https://github.com/vbrekher/iptv/pull/2) | Анонимная проверка HLS-манифеста и небольшого видеофрагмента |
| [#3 · Bunny One-Click](https://github.com/vbrekher/iptv/pull/3) | Создание Storage Zone и Pull Zone, один скрытый Account API Key, авторазвёртывание |
| [#4 · Storage 401 Repair](https://github.com/vbrekher/iptv/pull/4) | Корректный регион и writable пароль Bunny Storage, retry и продолжение загрузки |
| [#5 · All Countries](https://github.com/vbrekher/iptv/pull/5) | Страновые M3U из официального списка IPTV-org, grouped index, countries-only |
| [#6 · Samsung Tizen Lite](https://github.com/vbrekher/iptv/pull/6) | Облегчённые M3U на 240 и 600 записей |
| [#7 · Clean Groups](https://github.com/vbrekher/iptv/pull/7) | Одна нормальная категория на телеканал, устранение комбинаций Family;Series и др. |
| [#8 · Adulttest](https://github.com/vbrekher/iptv/pull/8) | Исследование 16 источников, фильтрация, логотипы, отдельный тестовый adulttest.m3u |
| [#9 · Pluto TV & qist](https://github.com/vbrekher/iptv/pull/9) | Pluto all/DE/US/GB/lite/erotic FAST, изучение qist/tvbox |

## Public Playlist Hub

- [238 прямых ссылок M3U](BUNNY_PLAYLISTS.md): 16 основных и специальных плейлистов, 34 категории, 188 стран с флагами.
- [Машиночитаемый JSON-каталог](../catalog/bunny-playlists.json): URL, описание, тип и статус каждой ссылки.
- [Один запуск публикации в существующий Bunny](PUBLIC_RELEASE.md): один скрытый ввод ключа, без пересоздания зон, без повторной проверки adulttest.
- Новая главная страница GitHub и проверка каталога в CI.

## Что реально подтверждено

В предыдущем терминальном отчёте пользователя опубликованы 39 M3U/каталожных файлов: большой index.m3u, adult.m3u, countries/ua.m3u, отдельные категории. CDN index отмечен VERIFIED. В отдельном пользовательском отчёте Adulttest — 682 URL-кандидата, 141 технически доступный HLS, 541 отклонён, adulttest_uploaded=true и cdn_verified=true.

GitHub CI построил Pluto ALL 3016 записей, Germany 200, Erotic FAST 8, Lite 240, US 433 и GB 183. **Это сборка данных в CI, не доказательство загрузки Pluto на Bunny или воспроизведения каналов на Samsung.**

Не подтверждены все 188 стран на Bunny, наличие чистых Tizen-плейлистов после фикса категорий, разрешение правообладателей на публичное распространение потоков и реальное качество HD.

Наблюдение пользователя: многие потоки возвращали корректный HLS, но показывали заставку о платной подписке. Поэтому HTTP 200 / OPEN не приравнивается к доступному бесплатному телевидению. Ошибка CUB относится к отдельному облачному действию Lampa.

## Техническая архитектура

Оригинальный IPTV-org остаётся базой. Наши скрипты расположены в папке [tools/](../tools/): personal_bunny_playlists.py, free_hls_filter.py, auto_bunny_setup.py, sync_bunny_countries.py, build_lampa_lite.py, lampa_category_fix.py, adulttest.py, plutotv_bunny.py, publish_public_bunny.py.

Bunny Storage и CDN хранят/выдают **только M3U и текстовые отчёты**. HLS-видео идёт от третьих сторон. Наличие ссылки не снимает лицензионные, DRM или географические ограничения.

Исходная лицензия [CC0](../LICENSE) сохраняется. На логотипы, товарные знаки и вещание сторонних каналов могут распространяться отдельные права.
