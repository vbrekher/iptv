<div align="center">

# 📺 IPTV HUB
### 🌍 Global channels · 📂 Categories · 🪐 Pluto TV · 🔞 Adult · 🐰 Bunny CDN

**Открытый каталог M3U для Samsung Tizen / Lampa, VLC и других IPTV-плееров.**

[![CI](https://github.com/vbrekher/iptv/actions/workflows/personal-bunny-playlists.yml/badge.svg)](https://github.com/vbrekher/iptv/actions/workflows/personal-bunny-playlists.yml) [![License: CC0](https://img.shields.io/badge/License-CC0-5c6bc0.svg)](LICENSE) [![237 M3U](https://img.shields.io/badge/M3U_links-237-2da8a6.svg)](docs/BUNNY_PLAYLISTS.md)

**🌐 Language / Taal / Язык:** [English](README.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md)

[📚 Все плейлисты](docs/BUNNY_PLAYLISTS.md) · [🚀 Быстрый старт](#quick-start) · [🌍 Страны](#countries) · [📖 Изменения](docs/FORK_CHANGELOG.md)

</div>

---

> [!IMPORTANT]
> Независимый форк [iptv-org/iptv](https://github.com/iptv-org/iptv), а не официальный CDN IPTV-org. Наличие M3U не гарантирует воспроизведение, HD-качество, бесплатный доступ или право распространения.

## ✨ Что добавлено в форк

| 🌍 | 📂 | 📺 | 🪐 |
|---|---|---|---|
| 188 стран с флагами | 34 тематические категории | Облегчённые списки для Samsung | Отдельные Pluto TV и 18+ списки |

**237 публичных M3U-ссылок** = 188 стран + 34 категории + 15 основных/специальных плейлистов. Это число адресов, **не количество рабочих каналов**.

### Статус публикации (2 ноября 2026)

**6 файлов проверены через CDN**, **229 остальных загружены в Bunny Storage**, **2 адреса пока не подтверждены**. В шесть проверенных входят ранее подтверждённый `index.m3u` и пять файлов с `CDN_CHECKS: true` из нового лога. Воспроизведение на телевизоре отдельно не проверено.

> Что означают статусы?: Загружено в Storage = Bunny принял M3U. CDN проверен = HTTP-запрос в терминале вернул заголовок M3U. Ни один из результатов не гарантирует работу видео на Samsung.

<a id="quick-start"></a>

## 🚀 Быстрый старт Samsung / Lampa

Начинай с коротких M3U: большие списки ранее вызывали долгую загрузку на Samsung Tizen.

| Плейлист | Содержимое | Публикация | 
|---|---|---|
| **Lampa Clean Lite** | До 240 записей, исправленные категории | [lampa-clean-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) | ✅ CDN проверен в терминале |
| **Pluto TV Lite** | 240 Pluto FAST-каналов | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ✅ CDN проверен в терминале |
| **Россия** | Россия — страновой список | [countries/ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ☑️ Загружен в Bunny Storage |
| **Украина** | Украина — страновой список | [countries/ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ✅ CDN проверен в терминале |
| **Общий IPTV** | Полный публичный IPTV | [index.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.m3u) | ✅ CDN проверен в терминале |
| **Список стран** | Все страны в одном списке | [index.country.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u) | ☑️ Загружен в Bunny Storage |
| **Adult / XXX** | Ранее загруженный 18+ список | [adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) | ☑️ Загружен в Bunny Storage |

<details>
<summary><strong>📱 Как открыть плейлист</strong></summary>

1. В IPTV-плагине Lampa или VLC выбери открытие сетевого плейлиста.
2. Скопируй полную HTTPS-ссылку, для Samsung начни с версии Lite.
3. Добавь ссылку напрямую; загрузка в облако CUB — отдельная функция плагина.
4. Доступный файл M3U не гарантирует, что каждый телеканал воспроизводится. Возможны геоограничения.

</details>

<a id="countries"></a>

## 🌍 Страны — сначала Россия, затем Украина

Все 188 файлов стран загружены в Storage по последнему логу. Россия и Украина закреплены первыми по предпочтению владельца, затем идут остальные страны.

| Country / Land / Страна | M3U | Status |
|---|---|---|
| 🇷🇺 Россия | [ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ☑️ Загружен в Bunny Storage |
| 🇺🇦 Украина | [ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ✅ CDN проверен в терминале |
| 🇩🇪 Германия | [de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/de.m3u) | ☑️ Загружен в Bunny Storage |
| 🇳🇱 Нидерланды | [nl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/nl.m3u) | ☑️ Загружен в Bunny Storage |
| 🇵🇱 Польша | [pl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pl.m3u) | ☑️ Загружен в Bunny Storage |
| 🇺🇰 Великобритания | [uk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/uk.m3u) | ☑️ Загружен в Bunny Storage |
| 🇺🇸 Соединенные Штаты | [us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/us.m3u) | ☑️ Загружен в Bunny Storage |
| 🇫🇷 Франция | [fr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/fr.m3u) | ☑️ Загружен в Bunny Storage |
| 🇮🇹 Италия | [it.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/it.m3u) | ☑️ Загружен в Bunny Storage |
| 🇪🇸 Испания | [es.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/es.m3u) | ☑️ Загружен в Bunny Storage |
| 🇨🇦 Канада | [ca.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ca.m3u) | ☑️ Загружен в Bunny Storage |
| 🇯🇵 Япония | [jp.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/jp.m3u) | ☑️ Загружен в Bunny Storage |

**[🗺 Показать все 188 стран с флагами →](docs/BUNNY_PLAYLISTS.md#countries)**

<a id="categories"></a>

## 🎭 Категории каналов

34 отдельных M3U из первой загрузки Bunny: новости, спорт, кино, наука и XXX. В старых источниках возможны реклама и устаревшие потоки.

| M3U | Status |
|---|---|
| [Новости](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/news.m3u) | ☑️ Загружен в Bunny Storage |
| [Спорт](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/sports.m3u) | ☑️ Загружен в Bunny Storage |
| [Фильмы](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/movies.m3u) | ☑️ Загружен в Bunny Storage |
| [Сериалы](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/series.m3u) | ☑️ Загружен в Bunny Storage |
| [Музыка](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/music.m3u) | ☑️ Загружен в Bunny Storage |
| [Детские](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/kids.m3u) | ☑️ Загружен в Bunny Storage |
| [Образование](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/education.m3u) | ☑️ Загружен в Bunny Storage |
| [Наука](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/science.m3u) | ☑️ Загружен в Bunny Storage |
| [Документальные](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/documentary.m3u) | ☑️ Загружен в Bunny Storage |
| [Путешествия](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/travel.m3u) | ☑️ Загружен в Bunny Storage |
| [XXX)](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u) | ☑️ Загружен в Bunny Storage |

**[📂 Показать все 34 категории →](docs/BUNNY_PLAYLISTS.md#categories)**

## 🪐 Pluto TV — отдельное бесплатное FAST

Списки из стороннего генератора; потоки идут через jmp2.uk и могут иметь геоограничения. Это не замена платным премиальным каналам.

| M3U | Status |
|---|---|
| [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ✅ CDN проверен в терминале |
| [plutotv-de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u) | ✅ CDN проверен в терминале |
| [plutotv-us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-us.m3u) | ☑️ Загружен в Bunny Storage |
| [plutotv-gb.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-gb.m3u) | ☑️ Загружен в Bunny Storage |
| [plutotv-erotic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u) | ✅ CDN проверен в терминале |
| [plutotv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv.m3u) | ☑️ Загружен в Bunny Storage |

## 🔞 Adult / XXX

Категории 18+ отделены от обычного телевидения. Успешная проверка HLS не доказывает бесплатность эфира: встречались заглушки с оплатой и cam-реклама. Старый тестовый список в публичном форке отсутствует.

[adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) · [categories/xxx.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u)

## 🛠 Что изменили относительно IPTV-org

Создание Bunny-зон и исправление Storage 401, экспорт стран и категорий, правильная группировка каналов, облегчённые M3U для Lampa, Pluto FAST, публичный каталог со статусами и JSON-манифест. Авторство исходного IPTV-org сохранено.

**Документация:** [Полный каталог](docs/BUNNY_PLAYLISTS.md) · [Публикация недостающих файлов](docs/PUBLIC_RELEASE.md) · [Изменения форка](docs/FORK_CHANGELOG.md) · [Настройка Bunny](docs/BUNNY_ONE_CLICK.md) · [Pluto и исследование qist](docs/QIST_PLUTOTV.md) · [Персональные плейлисты](docs/PERSONAL_BUNNY_IPTV.md) · [JSON-каталог](catalog/bunny-playlists.json)

---

Основа проекта: [iptv-org/iptv](https://github.com/iptv-org/iptv) · Лицензия: [CC0](LICENSE) · [Contributing](CONTRIBUTING.md)

Bunny CDN хранит M3U и метаданные, но не видеопотоки. Логотипы, бренды и трансляции принадлежат их правообладателям.
