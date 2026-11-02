<div align="center">

# 📺 IPTV HUB
### 🌍 Global channels · 📂 Categories · 🪐 Pluto TV · 🔞 Adult · 🐰 Bunny CDN

**Открытый каталог M3U для Samsung Tizen / Lampa, VLC и других IPTV-плееров**

[![GitHub CI](https://github.com/vbrekher/iptv/actions/workflows/personal-bunny-playlists.yml/badge.svg)](https://github.com/vbrekher/iptv/actions/workflows/personal-bunny-playlists.yml)
[![License: CC0](https://img.shields.io/badge/License-CC0-5c6bc0.svg)](LICENSE)
[![Fork: IPTV-org](https://img.shields.io/badge/Based%20on-IPTV--org-2962ff.svg)](https://github.com/iptv-org/iptv)
[![Public M3U Directory](https://img.shields.io/badge/Catalog-238%20M3U%20links-2da8a6.svg)](docs/BUNNY_PLAYLISTS.md)

[**📚 ПОЛНЫЙ КАТАЛОГ**](docs/BUNNY_PLAYLISTS.md) · [**🚀 БЫСТРЫЙ СТАРТ**](#-начните-отсюда) · [**🌍 СТРАНЫ**](#-188-стран-с-флагами) · [**📖 ИЗМЕНЕНИЯ**](docs/FORK_CHANGELOG.md) · [**🛠 ПУБЛИКАЦИЯ**](docs/PUBLIC_RELEASE.md)

</div>

---

> [!IMPORTANT]
> **Это независимый форк [iptv-org/iptv](https://github.com/iptv-org/iptv), а не официальный CDN IPTV-org.** В каталоге приведены прямые ссылки на M3U. Статус URL может быть подтверждён загрузкой, отчётом CDN или пока не подтверждён. Ссылка сама по себе **не гарантирует воспроизведения** канала, отсутствие рекламы/платной заставки или право распространения.

## ✨ Что здесь особенного

| 🌍 Каталог | 📺 Samsung / Lampa | 🔞 Adulttest | 🪐 Pluto TV |
|---|---|---|---|
| 188 стран с флагами, 34 категории | Лёгкие варианты на 240/600 записей | Отдельный тестированный HLS-каталог | Общее, региональное и Erotic FAST |
| Прямые ссылки на Bunny CDN | Исправленные группы без случайных комбинаций | Отдельный список, не смешанный с Pluto | Источники и логотипы в M3U |

**238 описанных URL** = 188 стран + 34 категории + 16 основных/специальных списков. Это количество ссылок в каталоге, **не количество проверенных доступных CDN-объектов или телеканалов**.

## 🚀 Начните отсюда

**Для Samsung Tizen / Lampa начните с коротких списков.** Огромные M3U с тысячами записей могут надолго загружать IPTV-плагин.

| Вариант | Прямая ссылка | Что внутри | Публикация |
|---|---|---|---|
| ⭐ **Lampa Clean Lite** | [lampa-clean-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) | До 240 каналов, исправленные категории | ○ Не подтверждена |
| 🪐 **Pluto TV Lite** | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | 240 FAST-каналов | ○ Не подтверждена |
| 🇺🇦 **Украина** | [countries/ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | Украинский телекаталог | ☑️ Был загружен |
| 🎭 **Все категории** | [index.category.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.category.m3u) | Большой исторический список | ☑️ Был загружен |
| 🌐 **Общий IPTV** | [index.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.m3u) | Все каналы (большой файл) | ✅ CDN ранее VERIFIED |
| 🔞 **Adulttest** | [adulttest.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adulttest.m3u) | HLS-кандидаты 18+ | ✅ CDN по отчёту пользователя |

**Исправленный полный каталог:** [index.clean.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.clean.m3u) · **Общий по странам:** [index.country.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u) · **Lampa Clean 600:** [lampa-clean.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean.m3u)

<details>
<summary><strong>📱 Как подключить M3U в Lampa или VLC</strong></summary>

1. Откройте IPTV-плагин Lampa или VLC → **Открыть сетевой поток**.
2. Скопируйте полную HTTPS-ссылку на M3U из таблицы.
3. Добавьте её как прямой источник. Для начала выбирайте **Lite** на 240 записей.
4. Если IPTV-плагин предлагает «upload to CUB», это отдельная облачная функция: для проверки M3U лучше прямой импорт по URL.
5. Если список открылся, но видео показывает заставку «pay for a subscription», это проблема/ограничение внешнего вещателя, а не загрузки плейлиста с Bunny.

На Samsung Tizen нельзя гарантировать работу каждого внешнего потока: возможны геоблокировки, неподдерживаемые кодеки, CORS и ограничения стороннего сайта.

</details>

## 🌍 188 стран с флагами

Плейлисты стран формируются из официального [индекса IPTV-org](https://github.com/iptv-org/iptv/blob/master/PLAYLISTS.md). Украина подтверждена в предыдущем логе загрузки, а фактическая публикация остальных **требует проверки/синхронизации**.

| | Страна | M3U | | Страна | M3U |
|:---:|---|---|:---:|---|---|
| 🇺🇦 | Украина | [ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | 🇺🇸 | США | [us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/us.m3u) |
| 🇩🇪 | Германия | [de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/de.m3u) | 🇳🇱 | Нидерланды | [nl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/nl.m3u) |
| 🇵🇱 | Польша | [pl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pl.m3u) | 🇬🇧 | Великобритания | [uk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/uk.m3u) |
| 🇫🇷 | Франция | [fr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/fr.m3u) | 🇪🇸 | Испания | [es.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/es.m3u) |
| 🇮🇹 | Италия | [it.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/it.m3u) | 🇨🇦 | Канада | [ca.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ca.m3u) |
| 🇧🇷 | Бразилия | [br.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/br.m3u) | 🇯🇵 | Япония | [jp.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/jp.m3u) |

**[🔎 Открыть все 188 стран с флагами и прямыми ссылками →](docs/BUNNY_PLAYLISTS.md#-по-странам--188-направлений)**

## 🎭 Каналы по категориям

Наш форк хранит **34 отдельных тематических файла** из первой сборки. Подписаться на один раздел проще, чем открывать весь 11-тысячный список.

| Раздел | Прямая ссылка | Раздел | Прямая ссылка |
|---|---|---|---|
| 📰 Новости | [news.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/news.m3u) | ⚽ Спорт | [sports.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/sports.m3u) |
| 🎬 Фильмы | [movies.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/movies.m3u) | 🍿 Сериалы | [series.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/series.m3u) |
| 🎵 Музыка | [music.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/music.m3u) | 🧸 Детские | [kids.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/kids.m3u) |
| 🎓 Образование | [education.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/education.m3u) | 🔬 Наука | [science.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/science.m3u) |
| 🎞️ Документальные | [documentary.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/documentary.m3u) | ✈️ Путешествия | [travel.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/travel.m3u) |
| 🎭 Развлечения | [entertainment.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/entertainment.m3u) | 🌦️ Погода | [weather.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/weather.m3u) |

**[📂 Открыть все 34 категории →](docs/BUNNY_PLAYLISTS.md#-категории)**

## 🪐 Pluto TV · бесплатное FAST-телевидение

Из открытого источника [BuddyChewChew/app-m3u-generator](https://github.com/BuddyChewChew/app-m3u-generator) подготовлены отдельные M3U; некоторые используют сторонние ссылки **jmp2.uk**, поэтому географическая и реальная доступность не гарантированы. Публикация на Bunny ещё **не подтверждена**.

| Каталог | Содержимое по последнему CI | M3U |
|---|---:|---|
| 🌐 Все регионы | 3 016 записей | [plutotv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv.m3u) |
| 📺 Lite | 240 записей | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) |
| 🇩🇪 Германия | 200 | [plutotv-de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u) |
| 🇺🇸 США | 433 | [plutotv-us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-us.m3u) |
| 🇬🇧 Великобритания | 183 | [plutotv-gb.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-gb.m3u) |
| 🔞 Erotic FAST (DE) | 8 | [plutotv-erotic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u) |

## 🔞 Adult / XXX — отдельно от обычного каталога

<details>
<summary><strong>18+ · Открыть ссылки и предупреждения</strong></summary>

> Материалы исключительно для совершеннолетних. Старые M3U включают сторонние ссылки с рекламой, камерами или заставками о подписке. Факт ответа HLS **не подтверждает** бесплатный эфир, разрешение HD или права вещателя.

| Источник | M3U | Статус |
|---|---|---|
| Adulttest · 141 технически открытый HLS по пользовательскому отчёту | [adulttest.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adulttest.m3u) | ✅ CDN подтверждён отчётом |
| Исторический список · 46 анонимных HLS | [adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) | ☑️ Был загружен |
| Старый категорийный каталог | [categories/xxx.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u) | ☑️ Был загружен |
| Немецкие Pluto Erotic FAST (не премиальное хардкор-ТВ) | [plutotv-erotic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u) | ○ Публикация не подтверждена |

Платные каналы Brazzers, Hustler, Dorcel и Penthouse не превращаются в легальные бесплатные HD-потоки от того, что ссылка попала в GitHub. Личные подписочные IPTV-адреса в этот форк не добавляются.

</details>

## 🐰 Автоматизация Bunny Storage + CDN

Наши Python-инструменты используют только стандартную библиотеку, работают на Mac и Linux и **не хранят видео**. Готовая логика: создание зон для первого запуска, восстановление после 401, нормализация категорий, тестирование анонимного HLS, сбор стран и Pluto, публикация M3U.

Для владельца **уже существующих** Storage и Pull Zone:

~~~bash
cd "$HOME/iptv-bunny"
python3 publish_public_bunny.py --dry-run    # предварительный просмотр
python3 publish_public_bunny.py              # публикация отсутствующих файлов
~~~

Сначала скачайте актуальные инструменты: [инструкция «одна команда»](docs/PUBLIC_RELEASE.md). Account API Key запрашивается скрыто один раз; новые платные зоны не создаются.

### Репозиторий: 9 этапов развития

Изменения с PR [#1](https://github.com/vbrekher/iptv/pull/1) по [#9](https://github.com/vbrekher/iptv/pull/9) оформлены в [полной истории разработки](docs/FORK_CHANGELOG.md), включая скрипты, исправления ошибок, релизные границы и реальные результаты проверок.

**Документация:** [Каталог M3U](docs/BUNNY_PLAYLISTS.md) · [Развёртывание Bunny](docs/BUNNY_ONE_CLICK.md) · [Adulttest](docs/ADULTTEST.md) · [Pluto и qist](docs/QIST_PLUTOTV.md) · [Обновление публикаций](docs/PUBLIC_RELEASE.md) · [Данные каталога JSON](catalog/bunny-playlists.json)

---

## 🌐 About this fork (English)

**IPTV Hub** is an independent, public [IPTV-org](https://github.com/iptv-org/iptv) fork featuring curated **M3U directory links**, a Bunny CDN publishing workflow, country playlists with flag emojis, category playlists, Samsung Tizen/Lampa-friendly variants, Pluto TV FAST lists and a separate adult research playlist.

[Browse all playlist links](docs/BUNNY_PLAYLISTS.md) • [Publish to your existing Bunny zones](docs/PUBLIC_RELEASE.md) • [Fork change history](docs/FORK_CHANGELOG.md).

**Important:** Public M3U links are *not* guaranteed playable, licensed, geo-unrestricted or free of broadcaster paywalls. The server stores playlist metadata, never movies or livestream video. Some referenced destinations have not yet been deployed to Bunny; publication status is shown in the catalog.

**Credits & licenses:** based on [iptv-org/iptv](https://github.com/iptv-org/iptv) ([CC0](LICENSE)). Source logos, channel brands, channel data and external video streams belong to their respective owners and may have independent distribution terms. [Contributing](CONTRIBUTING.md) · [Upstream issues](https://github.com/iptv-org/iptv/issues).
