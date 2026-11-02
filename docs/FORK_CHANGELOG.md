# IPTV Bunny Public Hub — история изменений

[English](en/FORK_CHANGELOG.md) · [Nederlands](nl/FORK_CHANGELOG.md) · [Русский](FORK_CHANGELOG.md)

**Дата оформления витрины:** 2026-11-02
**Форк:** https://github.com/vbrekher/iptv
**Оригинальный проект:** https://github.com/iptv-org/iptv

## История объединённых PR

| Pull Request | Что мы изменили |
|---|---|
| [#1 · Personal Bunny Playlists](https://github.com/vbrekher/iptv/pull/1) | Отдельная Python-сборка M3U, исторические 18+ кандидаты, категории, Bunny Storage |
| [#2 · Free HLS Filter](https://github.com/vbrekher/iptv/pull/2) | Анонимная проверка HLS-манифеста и небольшого видеофрагмента |
| [#3 · Bunny One-Click](https://github.com/vbrekher/iptv/pull/3) | Создание Storage Zone и Pull Zone, один скрытый Account API Key, авторазвёртывание |
| [#4 · Storage 401 Repair](https://github.com/vbrekher/iptv/pull/4) | Корректный регион и writable пароль Bunny Storage, retry и продолжение загрузки |
| [#5 · All Countries](https://github.com/vbrekher/iptv/pull/5) | Страновые M3U из официального списка IPTV-org, grouped index, countries-only |
| [#6 · Samsung Tizen Lite](https://github.com/vbrekher/iptv/pull/6) | Облегчённые M3U на 240 и 600 записей |
| [#7 · Clean Groups](https://github.com/vbrekher/iptv/pull/7) | Одна нормальная категория на телеканал, устранение комбинаций Family;Series и др. |
| [#8 · Архивный эксперимент](https://github.com/vbrekher/iptv/pull/8) | Экспериментальный тестер потоков позднее исключён из публичной версии |
| [#9 · Pluto TV & qist](https://github.com/vbrekher/iptv/pull/9) | Pluto all/DE/US/GB/lite/erotic FAST, изучение qist/tvbox |
| [#10 · Публичная витрина](https://github.com/vbrekher/iptv/pull/10) | Каталог 237 M3U, 188 стран с флагами, 34 категории, JSON-манифест и инструкция публикации |
| [#11 · Вывод тестового каталога](https://github.com/vbrekher/iptv/pull/11) | Удалены прежний тестовый плейлист, генератор, проверки и документация |

## Public Playlist Hub

- [237 прямых ссылок M3U](BUNNY_PLAYLISTS.md): 15 основных и специальных плейлистов, 34 категории, 188 стран с флагами.
- [Машиночитаемый JSON-каталог](../catalog/bunny-playlists.json): URL, описание, тип и статус каждой ссылки.
- [Один запуск публикации в существующий Bunny](PUBLIC_RELEASE.md): один скрытый ввод ключа, без пересоздания зон, без повторной проверки потоков.
- Новая главная страница GitHub и проверка каталога в CI.

## Что реально подтверждено

В предыдущем терминальном отчёте пользователя опубликованы 39 M3U/каталожных файлов: большой index.m3u, adult.m3u, countries/ua.m3u, отдельные категории. CDN index отмечен VERIFIED.

GitHub CI построил Pluto ALL 3016 записей, Germany 200, Erotic FAST 8, Lite 240, US 433 и GB 183. **Это сборка данных в CI, не доказательство загрузки Pluto на Bunny или воспроизведения каналов на Samsung.**

**2 ноября 2026 года владелец проверил все 237 публичных CDN-ссылок**: каждая вернула HTTP 206 и заголовок `#EXTM3U`. Результат — **237 успешно, 0 ошибок**. [Полный машинный отчёт](../catalog/cdn-verification-2026-11-02.json) сохранён в репозитории.

Каталог содержит **188 стран, 34 категории и 15 основных списков**. Предыдущая загрузка 198 файлов в Bunny Storage — отдельный исторический этап, а новая проверка охватывает все 237 публичных M3U. **Воспроизведение отдельных телеканалов и работа на Samsung не подтверждались**.

**Главная страница обновлена:** на корневом GitHub README теперь сразу видны английский, русский и нидерландский разделы, языковое меню и прямые ссылки на M3U. Отдельные полные переводы и каталоги сохранены.

Наблюдение пользователя: многие потоки возвращали корректный HLS, но показывали заставку о платной подписке. Поэтому HTTP 200 / OPEN не приравнивается к доступному бесплатному телевидению. Ошибка CUB относится к отдельному облачному действию Lampa.

## Техническая архитектура

Оригинальный IPTV-org остаётся базой. Наши скрипты расположены в папке [tools/](../tools/): personal_bunny_playlists.py, free_hls_filter.py, auto_bunny_setup.py, sync_bunny_countries.py, build_lampa_lite.py, lampa_category_fix.py, plutotv_bunny.py, publish_public_bunny.py.

Bunny Storage и CDN хранят/выдают **только M3U и текстовые отчёты**. HLS-видео идёт от третьих сторон. Наличие ссылки не снимает лицензионные, DRM или географические ограничения.

Исходная лицензия [CC0](../LICENSE) сохраняется. На логотипы, товарные знаки и вещание сторонних каналов могут распространяться отдельные права.

## Удаление тестового 18+ каталога

Тестовый список и его генератор исключены из текущего дерева форка по запросу владельца. Исторические PR GitHub сохраняются как история разработки. Удаление ранее загруженного объекта из Bunny Storage и очистка CDN выполняются отдельно в аккаунте владельца.
