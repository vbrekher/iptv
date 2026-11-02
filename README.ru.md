<div align="center">

# 📺 IPTV HUB

### Открытые IPTV-плейлисты со всего мира

**Samsung Tizen · Lampa · VLC · Bunny CDN**

[![CI](https://github.com/vbrekher/iptv/actions/workflows/personal-bunny-playlists.yml/badge.svg)](https://github.com/vbrekher/iptv/actions/workflows/personal-bunny-playlists.yml) [![CC0](https://img.shields.io/badge/License-CC0-blue.svg)](LICENSE) [![M3U](https://img.shields.io/badge/M3U-237-2563eb.svg)](catalog/bunny-playlists.json) [![CDN](https://img.shields.io/badge/CDN_verified-237%2F237-15803d.svg)](catalog/cdn-verification-2026-11-02.json)

### 🌐 [🇬🇧 ENGLISH](README.md#english) &nbsp; · &nbsp; [🇷🇺 РУССКИЙ](README.ru.md) &nbsp; · &nbsp; [🇳🇱 NEDERLANDS](README.nl.md)

[📚 Полный каталог](docs/BUNNY_PLAYLISTS.md) · [🚀 Быстрый старт](#quick-start) · [🌍 Страны](#countries) · [📖 История изменений](docs/FORK_CHANGELOG.md)

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

**237/237 публичных M3U-файлов прошли CDN-проверку в терминале** (HTTP 206 и `#EXTM3U`; 0 ошибок). [Полный отчёт проверки](catalog/cdn-verification-2026-11-02.json). Это подтверждает доступность самих плейлистов, **но не воспроизведение телеканалов** на Samsung.

> **✅ CDN checked in terminal** означает успешную проверку файла плейлиста. Видеопотоки и права распространения не проверялись.

<a id="quick-start"></a>

## 🚀 Быстрый старт Samsung / Lampa

Начинай с коротких M3U: большие списки ранее вызывали долгую загрузку на Samsung Tizen.

| Плейлист | Содержимое | Публикация | 
|---|---|---|
| **Lampa Clean Lite** | До 240 записей, исправленные категории | [lampa-clean-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) | ✅ CDN checked in terminal |
| **Pluto TV Lite** | 240 Pluto FAST-каналов | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ✅ CDN checked in terminal |
| **Россия** | Россия — страновой список | [countries/ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ✅ CDN checked in terminal |
| **Украина** | Украина — страновой список | [countries/ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ✅ CDN checked in terminal |
| **Общий IPTV** | Полный публичный IPTV | [index.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.m3u) | ✅ CDN checked in terminal |
| **Список стран** | Все страны в одном списке | [index.country.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u) | ✅ CDN checked in terminal |
| **Adult / XXX** | Ранее загруженный 18+ список | [adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) | ✅ CDN checked in terminal |

<details>
<summary><strong>📱 Как открыть плейлист</strong></summary>

1. В IPTV-плагине Lampa или VLC выбери открытие сетевого плейлиста.
2. Скопируй полную HTTPS-ссылку, для Samsung начни с версии Lite.
3. Добавь ссылку напрямую; загрузка в облако CUB — отдельная функция плагина.
4. Доступный файл M3U не гарантирует, что каждый телеканал воспроизводится. Возможны геоограничения.

</details>

<a id="countries"></a>

## 🌍 Страны — сначала Россия, затем Украина

Все 188 страновых M3U прошли проверку CDN 2 ноября 2026 года. Россия остаётся первой, Украина — второй.

| Country / Land / Страна | M3U | Status |
|---|---|---|
| 🇷🇺 Россия | [ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ✅ CDN checked in terminal |
| 🇺🇦 Украина | [ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ✅ CDN checked in terminal |
| 🇩🇪 Германия | [de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/de.m3u) | ✅ CDN checked in terminal |
| 🇳🇱 Нидерланды | [nl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/nl.m3u) | ✅ CDN checked in terminal |
| 🇵🇱 Польша | [pl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pl.m3u) | ✅ CDN checked in terminal |
| 🇺🇰 Великобритания | [uk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/uk.m3u) | ✅ CDN checked in terminal |
| 🇺🇸 Соединенные Штаты | [us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/us.m3u) | ✅ CDN checked in terminal |
| 🇫🇷 Франция | [fr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/fr.m3u) | ✅ CDN checked in terminal |
| 🇮🇹 Италия | [it.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/it.m3u) | ✅ CDN checked in terminal |
| 🇪🇸 Испания | [es.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/es.m3u) | ✅ CDN checked in terminal |
| 🇨🇦 Канада | [ca.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ca.m3u) | ✅ CDN checked in terminal |
| 🇯🇵 Япония | [jp.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/jp.m3u) | ✅ CDN checked in terminal |

**[🗺 Показать все 188 стран с флагами →](docs/BUNNY_PLAYLISTS.md#countries)**

<a id="categories"></a>

## 🎭 Категории каналов

34 отдельных M3U из первой загрузки Bunny: новости, спорт, кино, наука и XXX. В старых источниках возможны реклама и устаревшие потоки.

| M3U | Status |
|---|---|
| [Новости](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/news.m3u) | ✅ CDN checked in terminal |
| [Спорт](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/sports.m3u) | ✅ CDN checked in terminal |
| [Фильмы](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/movies.m3u) | ✅ CDN checked in terminal |
| [Сериалы](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/series.m3u) | ✅ CDN checked in terminal |
| [Музыка](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/music.m3u) | ✅ CDN checked in terminal |
| [Детские](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/kids.m3u) | ✅ CDN checked in terminal |
| [Образование](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/education.m3u) | ✅ CDN checked in terminal |
| [Наука](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/science.m3u) | ✅ CDN checked in terminal |
| [Документальные](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/documentary.m3u) | ✅ CDN checked in terminal |
| [Путешествия](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/travel.m3u) | ✅ CDN checked in terminal |
| [XXX](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u) | ✅ CDN checked in terminal |

**[📂 Показать все 34 категории →](docs/BUNNY_PLAYLISTS.md#categories)**

## 🪐 Pluto TV — отдельное бесплатное FAST

Списки из стороннего генератора; потоки идут через jmp2.uk и могут иметь геоограничения. Это не замена платным премиальным каналам.

| M3U | Status |
|---|---|
| [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ✅ CDN checked in terminal |
| [plutotv-de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u) | ✅ CDN checked in terminal |
| [plutotv-us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-us.m3u) | ✅ CDN checked in terminal |
| [plutotv-gb.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-gb.m3u) | ✅ CDN checked in terminal |
| [plutotv-erotic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u) | ✅ CDN checked in terminal |
| [plutotv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv.m3u) | ✅ CDN checked in terminal |

## 🔞 Adult / XXX

Категории 18+ отделены от обычного телевидения. Успешная проверка HLS не доказывает бесплатность эфира: встречались заглушки с оплатой и cam-реклама. Старый тестовый список в публичном форке отсутствует.

[adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) · [categories/xxx.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u)

## ✅ Проверка всех 237 ссылок Bunny CDN

Этот скрипт только читает ссылки: проверяет HTTP 200/206 и настоящий заголовок `#EXTM3U`. API-ключ Bunny не требуется, видеопотоки телеканалов не тестируются. Запусти на Mac:

```bash
mkdir -p "$HOME/iptv-bunny"
cd "$HOME/iptv-bunny"
curl -fsSL --retry 3 https://raw.githubusercontent.com/vbrekher/iptv/master/tools/check_public_cdn.py -o check_public_cdn.py
curl -fsSL --retry 3 https://raw.githubusercontent.com/vbrekher/iptv/master/catalog/bunny-playlists.json -o bunny-playlists.json
python3 check_public_cdn.py --self-test
python3 check_public_cdn.py --catalog bunny-playlists.json --output public-cdn-report.json
```

Команда выводит `CDN_CHECKED`, `CDN_FAILED` и список неуспешных адресов. По **локальному JSON-отчёту** можно обновить статусы в каталоге и документации на трёх языках. Загрузка в Storage сама по себе не даёт права ставить ✅; проверка CDN не подтверждает воспроизведение телеканалов.

## 🛠 Что изменили относительно IPTV-org

Создание Bunny-зон и исправление Storage 401, экспорт стран и категорий, правильная группировка каналов, облегчённые M3U для Lampa, Pluto FAST, публичный каталог со статусами и JSON-манифест. Авторство исходного IPTV-org сохранено.

**Документация:** [Полный каталог](docs/BUNNY_PLAYLISTS.md) · [Публикация недостающих файлов](docs/PUBLIC_RELEASE.md) · [Изменения форка](docs/FORK_CHANGELOG.md) · [Настройка Bunny](docs/BUNNY_ONE_CLICK.md) · [Pluto и исследование qist](docs/QIST_PLUTOTV.md) · [Персональные плейлисты](docs/PERSONAL_BUNNY_IPTV.md) · [JSON-каталог](catalog/bunny-playlists.json)

---

Основа проекта: [iptv-org/iptv](https://github.com/iptv-org/iptv) · Лицензия: [CC0](LICENSE) · [Contributing](CONTRIBUTING.md)

Bunny CDN хранит M3U и метаданные, но не видеопотоки. Логотипы, бренды и трансляции принадлежат их правообладателям.
