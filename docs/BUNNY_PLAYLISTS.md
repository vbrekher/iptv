# 📚 Каталог IPTV-плейлистов на Bunny CDN

**Public playlist directory • 2 ноября 2026**

> [!IMPORTANT]
> Ссылки приведены как публичные пути существующей Pull Zone. **Статус публикации и воспроизведения — разные вещи.** Перечисление URL не подтверждает, что файл уже загружен или что все каналы играют. Сейчас снаружи мы не можем выполнить независимую HTTP-проверку Bunny CDN.

**Легенда:** ✅ — CDN подтверждён ранее присланным отчётом · ☑️ — загрузка зафиксирована в логе пользователя · ○ — URL зарезервирован генератором, загрузка на Bunny не подтверждена.

**База URL:** `https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/` · [↩ На главную](../README.md) · [Инструкция по публикации](BUNNY_ONE_CLICK.md)

## 🚀 Основные и Samsung Lampa

| Плейлист | Каналов / цель | Публичный M3U | Статус |
|---|---|---|---|
| **Полный IPTV** | 11 420 записей на момент первого деплоя; не все проверены | [index.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.m3u) | ☑️ Загружен по логу |
| **Все категории (исторический)** | Изначальная загрузка, может содержать старую группировку | [index.category.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.category.m3u) | ☑️ Загружен по логу |
| **Все категории (исправлено)** | Исправление собрано, новая публикация не подтверждена | [index.clean.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.clean.m3u) | ○ Публикация не подтверждена |
| **Все страны вместе** | Публикация в Bunny ещё не подтверждена | [index.country.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u) | ○ Публикация не подтверждена |
| **Lampa Lite · 240** | Первый облегчённый вариант | [lampa-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-lite.m3u) | ○ Публикация не подтверждена |
| **Lampa · 600** | Расширенный облегчённый вариант | [lampa.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa.m3u) | ○ Публикация не подтверждена |
| **Lampa Clean Lite · 240** | Рекомендуется после загрузки | [lampa-clean-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) | ○ Публикация не подтверждена |
| **Lampa Clean · 600** | Рекомендуется после загрузки | [lampa-clean.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean.m3u) | ○ Публикация не подтверждена |

## 🔞 Adult / XXX

> 18+. Содержимое сторонних источников и права вещания не подтверждены. **HLS OPEN ≠ полноценный бесплатный телеканал**: ранее обнаружены cam-реклама и заставки с требованием подписки.

| Плейлист | Примечание | URL | Статус |
|---|---|---|---|
| Adult / XXX (исходный) | 46 ранее технически открытых HLS; много рекламных/платных заглушек | [adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) | ☑️ Загружен по логу |
| Adulttest / 18+ (тестовый) | 141 анонимный HLS прошёл тест; качество не подтверждено | [adulttest.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adulttest.m3u) | ✅ CDN подтверждён отчётом |

## 🪐 Pluto TV · отдельные списки

> Каналы из стороннего источника [BuddyChewChew/app-m3u-generator](https://github.com/BuddyChewChew/app-m3u-generator), ссылки HLS идут через `jmp2.uk`; возможны геоограничения. Это FAST-платформа, не премиальные платные каналы.

| Плейлист | Назначение | URL | Статус |
|---|---|---|---|
| Pluto TV · все регионы | 3 016 записей по последнему CI-отчёту | [plutotv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv.m3u) | ○ Публикация не подтверждена |
| Pluto TV Lite | 240 каналов — для Samsung | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ○ Публикация не подтверждена |
| Pluto TV Germany | 200 каналов | [plutotv-de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u) | ○ Публикация не подтверждена |
| Pluto TV Erotic FAST | 8 немецких эротических FAST-каналов | [plutotv-erotic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u) | ○ Публикация не подтверждена |
| Pluto TV US | 433 канала | [plutotv-us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-us.m3u) | ○ Публикация не подтверждена |
| Pluto TV UK | 183 канала | [plutotv-gb.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-gb.m3u) | ○ Публикация не подтверждена |

## 🎭 Категории

В первом подтверждённом выводе терминала опубликовано **34 категорий**. Эти отдельные файлы могут содержать старые записи; улучшенная группировка относится к новым файлам `index.clean.m3u` и `lampa-clean-*.m3u`.

| Тематика | Ссылка | Статус |
|---|---|---|
| ⚠️ AdultIPTV (старый источник) | [categories/adultiptv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/adultiptv.m3u) | ☑️ По первоначальному логу |
| 🎨 Анимация | [categories/animation.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/animation.m3u) | ☑️ По первоначальному логу |
| 🚗 Автомобили | [categories/auto.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/auto.m3u) | ☑️ По первоначальному логу |
| 💼 Бизнес | [categories/business.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/business.m3u) | ☑️ По первоначальному логу |
| 📼 Классика | [categories/classic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/classic.m3u) | ☑️ По первоначальному логу |
| 😂 Комедии | [categories/comedy.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/comedy.m3u) | ☑️ По первоначальному логу |
| 🍳 Кулинария | [categories/cooking.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/cooking.m3u) | ☑️ По первоначальному логу |
| 🏛️ Культура | [categories/culture.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/culture.m3u) | ☑️ По первоначальному логу |
| 🎞️ Документальные | [categories/documentary.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/documentary.m3u) | ☑️ По первоначальному логу |
| 🎓 Образование | [categories/education.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/education.m3u) | ☑️ По первоначальному логу |
| 🎭 Развлечения | [categories/entertainment.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/entertainment.m3u) | ☑️ По первоначальному логу |
| 👨‍👩‍👧 Семья | [categories/family.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/family.m3u) | ☑️ По первоначальному логу |
| 📺 Общие | [categories/general.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/general.m3u) | ☑️ По первоначальному логу |
| 🎮 Интерактив | [categories/interactive.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/interactive.m3u) | ☑️ По первоначальному логу |
| 🧸 Детские | [categories/kids.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/kids.m3u) | ☑️ По первоначальному логу |
| 🏛️ Парламент | [categories/legislative.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/legislative.m3u) | ☑️ По первоначальному логу |
| 🌿 Образ жизни | [categories/lifestyle.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/lifestyle.m3u) | ☑️ По первоначальному логу |
| 🎬 Фильмы | [categories/movies.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/movies.m3u) | ☑️ По первоначальному логу |
| 🎵 Музыка | [categories/music.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/music.m3u) | ☑️ По первоначальному логу |
| ⚠️ MyCamTV (старый источник) | [categories/mycamtv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/mycamtv.m3u) | ☑️ По первоначальному логу |
| 📰 Новости | [categories/news.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/news.m3u) | ☑️ По первоначальному логу |
| 🔞 Другие 18+ (старый источник) | [categories/other-adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/other-adult.m3u) | ☑️ По первоначальному логу |
| 🏞️ Природа и активный отдых | [categories/outdoor.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/outdoor.m3u) | ☑️ По первоначальному логу |
| 📡 Общественные | [categories/public.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/public.m3u) | ☑️ По первоначальному логу |
| 🧘 Релакс | [categories/relax.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/relax.m3u) | ☑️ По первоначальному логу |
| ⛪ Религия | [categories/religious.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/religious.m3u) | ☑️ По первоначальному логу |
| 🔬 Наука | [categories/science.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/science.m3u) | ☑️ По первоначальному логу |
| 🍿 Сериалы | [categories/series.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/series.m3u) | ☑️ По первоначальному логу |
| 🛍️ Покупки | [categories/shop.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/shop.m3u) | ☑️ По первоначальному логу |
| ⚽ Спорт | [categories/sports.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/sports.m3u) | ☑️ По первоначальному логу |
| ✈️ Путешествия | [categories/travel.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/travel.m3u) | ☑️ По первоначальному логу |
| 📁 Без категории | [categories/undefined.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/undefined.m3u) | ☑️ По первоначальному логу |
| 🌦️ Погода | [categories/weather.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/weather.m3u) | ☑️ По первоначальному логу |
| 🔞 18+ (XXX) | [categories/xxx.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u) | ☑️ По первоначальному логу |

## 🌍 По странам · 188 направлений

Ниже **188 кодов стран, присутствующих в официальном списке IPTV-org**. Скрипт `sync_bunny_countries.py` поддерживает их зеркалирование, но загрузка всех стран на конкретный Bunny пока не подтверждена. В старом терминальном логе есть подтверждение `ua.m3u`.

<details>
<summary><strong>Показать все страны с флагами и прямыми M3U</strong></summary>

| Страна | ISO | Прямая ссылка | Статус |
|---|:---:|---|:---:|
| 🇦🇫 Афганистан | `af` | [countries/af.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/af.m3u) | ○ |
| 🇦🇱 Албания | `al` | [countries/al.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/al.m3u) | ○ |
| 🇩🇿 Алжир | `dz` | [countries/dz.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/dz.m3u) | ○ |
| 🇦🇩 Андорра | `ad` | [countries/ad.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ad.m3u) | ○ |
| 🇦🇴 Ангола | `ao` | [countries/ao.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ao.m3u) | ○ |
| 🇦🇬 Антигуа и Барбуда | `ag` | [countries/ag.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ag.m3u) | ○ |
| 🇦🇷 Аргентина | `ar` | [countries/ar.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ar.m3u) | ○ |
| 🇦🇲 Армения | `am` | [countries/am.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/am.m3u) | ○ |
| 🇦🇼 Аруба | `aw` | [countries/aw.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/aw.m3u) | ○ |
| 🇦🇺 Австралия | `au` | [countries/au.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/au.m3u) | ○ |
| 🇦🇹 Австрия | `at` | [countries/at.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/at.m3u) | ○ |
| 🇦🇿 Азербайджан | `az` | [countries/az.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/az.m3u) | ○ |
| 🇧🇸 Багамы | `bs` | [countries/bs.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bs.m3u) | ○ |
| 🇧🇭 Бахрейн | `bh` | [countries/bh.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bh.m3u) | ○ |
| 🇧🇩 Бангладеш | `bd` | [countries/bd.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bd.m3u) | ○ |
| 🇧🇧 Барбадос | `bb` | [countries/bb.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bb.m3u) | ○ |
| 🇧🇾 Беларусь | `by` | [countries/by.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/by.m3u) | ○ |
| 🇧🇪 Бельгия | `be` | [countries/be.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/be.m3u) | ○ |
| 🇧🇿 Белиз | `bz` | [countries/bz.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bz.m3u) | ○ |
| 🇧🇯 Бенин | `bj` | [countries/bj.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bj.m3u) | ○ |
| 🇧🇹 Бутан | `bt` | [countries/bt.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bt.m3u) | ○ |
| 🇧🇴 Боливия | `bo` | [countries/bo.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bo.m3u) | ○ |
| 🇧🇶 Бонэйр, Синт-Эстатиус и Саба | `bq` | [countries/bq.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bq.m3u) | ○ |
| 🇧🇦 Босния и Герцеговина | `ba` | [countries/ba.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ba.m3u) | ○ |
| 🇧🇷 Бразилия | `br` | [countries/br.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/br.m3u) | ○ |
| 🇻🇬 Виргинские о-ва (Великобритания) | `vg` | [countries/vg.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/vg.m3u) | ○ |
| 🇧🇳 Бруней | `bn` | [countries/bn.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bn.m3u) | ○ |
| 🇧🇬 Болгария | `bg` | [countries/bg.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bg.m3u) | ○ |
| 🇧🇫 Буркина-Фасо | `bf` | [countries/bf.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bf.m3u) | ○ |
| 🇧🇮 Бурунди | `bi` | [countries/bi.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/bi.m3u) | ○ |
| 🇰🇭 Камбоджа | `kh` | [countries/kh.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/kh.m3u) | ○ |
| 🇨🇲 Камерун | `cm` | [countries/cm.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cm.m3u) | ○ |
| 🇨🇦 Канада | `ca` | [countries/ca.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ca.m3u) | ○ |
| 🇨🇻 Кабо-Верде | `cv` | [countries/cv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cv.m3u) | ○ |
| 🇹🇩 Чад | `td` | [countries/td.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/td.m3u) | ○ |
| 🇨🇱 Чили | `cl` | [countries/cl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cl.m3u) | ○ |
| 🇨🇳 Китай | `cn` | [countries/cn.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cn.m3u) | ○ |
| 🇨🇴 Колумбия | `co` | [countries/co.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/co.m3u) | ○ |
| 🇰🇲 Коморы | `km` | [countries/km.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/km.m3u) | ○ |
| 🇨🇷 Коста-Рика | `cr` | [countries/cr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cr.m3u) | ○ |
| 🇭🇷 Хорватия | `hr` | [countries/hr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/hr.m3u) | ○ |
| 🇨🇺 Куба | `cu` | [countries/cu.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cu.m3u) | ○ |
| 🇨🇼 Кюрасао | `cw` | [countries/cw.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cw.m3u) | ○ |
| 🇨🇾 Кипр | `cy` | [countries/cy.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cy.m3u) | ○ |
| 🇨🇿 Чехия | `cz` | [countries/cz.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cz.m3u) | ○ |
| 🇨🇩 Конго - Киншаса | `cd` | [countries/cd.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cd.m3u) | ○ |
| 🇩🇰 Дания | `dk` | [countries/dk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/dk.m3u) | ○ |
| 🇩🇴 Доминиканская Республика | `do` | [countries/do.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/do.m3u) | ○ |
| 🇪🇨 Эквадор | `ec` | [countries/ec.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ec.m3u) | ○ |
| 🇪🇬 Египет | `eg` | [countries/eg.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/eg.m3u) | ○ |
| 🇸🇻 Сальвадор | `sv` | [countries/sv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sv.m3u) | ○ |
| 🇬🇶 Экваториальная Гвинея | `gq` | [countries/gq.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gq.m3u) | ○ |
| 🇪🇷 Эритрея | `er` | [countries/er.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/er.m3u) | ○ |
| 🇪🇪 Эстония | `ee` | [countries/ee.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ee.m3u) | ○ |
| 🇪🇹 Эфиопия | `et` | [countries/et.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/et.m3u) | ○ |
| 🇫🇮 Финляндия | `fi` | [countries/fi.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/fi.m3u) | ○ |
| 🇫🇷 Франция | `fr` | [countries/fr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/fr.m3u) | ○ |
| 🇬🇫 Французская Гвиана | `gf` | [countries/gf.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gf.m3u) | ○ |
| 🇵🇫 Французская Полинезия | `pf` | [countries/pf.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pf.m3u) | ○ |
| 🇬🇲 Гамбия | `gm` | [countries/gm.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gm.m3u) | ○ |
| 🇬🇪 Грузия | `ge` | [countries/ge.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ge.m3u) | ○ |
| 🇩🇪 Германия | `de` | [countries/de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/de.m3u) | ○ |
| 🇬🇭 Гана | `gh` | [countries/gh.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gh.m3u) | ○ |
| 🇬🇷 Греция | `gr` | [countries/gr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gr.m3u) | ○ |
| 🇬🇵 Гваделупа | `gp` | [countries/gp.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gp.m3u) | ○ |
| 🇬🇺 Гуам | `gu` | [countries/gu.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gu.m3u) | ○ |
| 🇬🇹 Гватемала | `gt` | [countries/gt.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gt.m3u) | ○ |
| 🇬🇬 Гернси | `gg` | [countries/gg.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gg.m3u) | ○ |
| 🇬🇳 Гвинея | `gn` | [countries/gn.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gn.m3u) | ○ |
| 🇬🇾 Гайана | `gy` | [countries/gy.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/gy.m3u) | ○ |
| 🇭🇹 Гаити | `ht` | [countries/ht.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ht.m3u) | ○ |
| 🇭🇳 Гондурас | `hn` | [countries/hn.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/hn.m3u) | ○ |
| 🇭🇰 Гонконг | `hk` | [countries/hk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/hk.m3u) | ○ |
| 🇭🇺 Венгрия | `hu` | [countries/hu.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/hu.m3u) | ○ |
| 🇮🇸 Исландия | `is` | [countries/is.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/is.m3u) | ○ |
| 🇮🇳 Индия | `in` | [countries/in.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/in.m3u) | ○ |
| 🇮🇩 Индонезия | `id` | [countries/id.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/id.m3u) | ○ |
| 🇮🇷 Иран | `ir` | [countries/ir.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ir.m3u) | ○ |
| 🇮🇶 Ирак | `iq` | [countries/iq.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/iq.m3u) | ○ |
| 🇮🇪 Ирландия | `ie` | [countries/ie.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ie.m3u) | ○ |
| 🇮🇱 Израиль | `il` | [countries/il.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/il.m3u) | ○ |
| 🇮🇹 Италия | `it` | [countries/it.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/it.m3u) | ○ |
| 🇨🇮 Кот-д’Ивуар | `ci` | [countries/ci.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ci.m3u) | ○ |
| 🇯🇲 Ямайка | `jm` | [countries/jm.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/jm.m3u) | ○ |
| 🇯🇵 Япония | `jp` | [countries/jp.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/jp.m3u) | ○ |
| 🇯🇴 Иордания | `jo` | [countries/jo.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/jo.m3u) | ○ |
| 🇰🇿 Казахстан | `kz` | [countries/kz.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/kz.m3u) | ○ |
| 🇰🇪 Кения | `ke` | [countries/ke.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ke.m3u) | ○ |
| 🇽🇰 Косово | `xk` | [countries/xk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/xk.m3u) | ○ |
| 🇰🇼 Кувейт | `kw` | [countries/kw.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/kw.m3u) | ○ |
| 🇰🇬 Киргизия | `kg` | [countries/kg.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/kg.m3u) | ○ |
| 🇱🇦 Лаос | `la` | [countries/la.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/la.m3u) | ○ |
| 🇱🇻 Латвия | `lv` | [countries/lv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/lv.m3u) | ○ |
| 🇱🇧 Ливан | `lb` | [countries/lb.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/lb.m3u) | ○ |
| 🇱🇾 Ливия | `ly` | [countries/ly.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ly.m3u) | ○ |
| 🇱🇮 Лихтенштейн | `li` | [countries/li.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/li.m3u) | ○ |
| 🇱🇹 Литва | `lt` | [countries/lt.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/lt.m3u) | ○ |
| 🇱🇺 Люксембург | `lu` | [countries/lu.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/lu.m3u) | ○ |
| 🇲🇴 Макао | `mo` | [countries/mo.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mo.m3u) | ○ |
| 🇲🇬 Мадагаскар | `mg` | [countries/mg.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mg.m3u) | ○ |
| 🇲🇾 Малайзия | `my` | [countries/my.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/my.m3u) | ○ |
| 🇲🇻 Мальдивы | `mv` | [countries/mv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mv.m3u) | ○ |
| 🇲🇱 Мали | `ml` | [countries/ml.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ml.m3u) | ○ |
| 🇲🇹 Мальта | `mt` | [countries/mt.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mt.m3u) | ○ |
| 🇲🇶 Мартиника | `mq` | [countries/mq.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mq.m3u) | ○ |
| 🇲🇷 Мавритания | `mr` | [countries/mr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mr.m3u) | ○ |
| 🇲🇺 Маврикий | `mu` | [countries/mu.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mu.m3u) | ○ |
| 🇲🇽 Мексика | `mx` | [countries/mx.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mx.m3u) | ○ |
| 🇲🇩 Молдова | `md` | [countries/md.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/md.m3u) | ○ |
| 🇲🇨 Монако | `mc` | [countries/mc.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mc.m3u) | ○ |
| 🇲🇳 Монголия | `mn` | [countries/mn.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mn.m3u) | ○ |
| 🇲🇪 Черногория | `me` | [countries/me.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/me.m3u) | ○ |
| 🇲🇦 Марокко | `ma` | [countries/ma.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ma.m3u) | ○ |
| 🇲🇿 Мозамбик | `mz` | [countries/mz.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mz.m3u) | ○ |
| 🇲🇲 Мьянма (Бирма) | `mm` | [countries/mm.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mm.m3u) | ○ |
| 🇳🇦 Намибия | `na` | [countries/na.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/na.m3u) | ○ |
| 🇳🇵 Непал | `np` | [countries/np.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/np.m3u) | ○ |
| 🇳🇱 Нидерланды | `nl` | [countries/nl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/nl.m3u) | ○ |
| 🇳🇨 Новая Каледония | `nc` | [countries/nc.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/nc.m3u) | ○ |
| 🇳🇿 Новая Зеландия | `nz` | [countries/nz.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/nz.m3u) | ○ |
| 🇳🇮 Никарагуа | `ni` | [countries/ni.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ni.m3u) | ○ |
| 🇳🇪 Нигер | `ne` | [countries/ne.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ne.m3u) | ○ |
| 🇳🇬 Нигерия | `ng` | [countries/ng.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ng.m3u) | ○ |
| 🇰🇵 КНДР | `kp` | [countries/kp.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/kp.m3u) | ○ |
| 🇲🇰 Северная Македония | `mk` | [countries/mk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/mk.m3u) | ○ |
| 🇳🇴 Норвегия | `no` | [countries/no.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/no.m3u) | ○ |
| 🇴🇲 Оман | `om` | [countries/om.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/om.m3u) | ○ |
| 🇵🇰 Пакистан | `pk` | [countries/pk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pk.m3u) | ○ |
| 🇵🇸 Палестина | `ps` | [countries/ps.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ps.m3u) | ○ |
| 🇵🇦 Панама | `pa` | [countries/pa.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pa.m3u) | ○ |
| 🇵🇬 Папуа — Новая Гвинея | `pg` | [countries/pg.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pg.m3u) | ○ |
| 🇵🇾 Парагвай | `py` | [countries/py.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/py.m3u) | ○ |
| 🇵🇪 Перу | `pe` | [countries/pe.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pe.m3u) | ○ |
| 🇵🇭 Филиппины | `ph` | [countries/ph.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ph.m3u) | ○ |
| 🇵🇱 Польша | `pl` | [countries/pl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pl.m3u) | ○ |
| 🇵🇹 Португалия | `pt` | [countries/pt.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pt.m3u) | ○ |
| 🇵🇷 Пуэрто-Рико | `pr` | [countries/pr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pr.m3u) | ○ |
| 🇶🇦 Катар | `qa` | [countries/qa.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/qa.m3u) | ○ |
| 🇨🇬 Конго - Браззавиль | `cg` | [countries/cg.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/cg.m3u) | ○ |
| 🇷🇪 Реюньон | `re` | [countries/re.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/re.m3u) | ○ |
| 🇷🇴 Румыния | `ro` | [countries/ro.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ro.m3u) | ○ |
| 🇷🇺 Россия | `ru` | [countries/ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ○ |
| 🇷🇼 Руанда | `rw` | [countries/rw.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/rw.m3u) | ○ |
| 🇰🇳 Сент-Китс и Невис | `kn` | [countries/kn.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/kn.m3u) | ○ |
| 🇱🇨 Сент-Люсия | `lc` | [countries/lc.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/lc.m3u) | ○ |
| 🇻🇨 Сент-Винсент и Гренадины | `vc` | [countries/vc.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/vc.m3u) | ○ |
| 🇼🇸 Самоа | `ws` | [countries/ws.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ws.m3u) | ○ |
| 🇸🇲 Сан-Марино | `sm` | [countries/sm.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sm.m3u) | ○ |
| 🇸🇦 Саудовская Аравия | `sa` | [countries/sa.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sa.m3u) | ○ |
| 🇸🇳 Сенегал | `sn` | [countries/sn.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sn.m3u) | ○ |
| 🇷🇸 Сербия | `rs` | [countries/rs.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/rs.m3u) | ○ |
| 🇸🇱 Сьерра-Леоне | `sl` | [countries/sl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sl.m3u) | ○ |
| 🇸🇬 Сингапур | `sg` | [countries/sg.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sg.m3u) | ○ |
| 🇸🇽 Синт-Мартен | `sx` | [countries/sx.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sx.m3u) | ○ |
| 🇸🇰 Словакия | `sk` | [countries/sk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sk.m3u) | ○ |
| 🇸🇮 Словения | `si` | [countries/si.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/si.m3u) | ○ |
| 🇸🇴 Сомали | `so` | [countries/so.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/so.m3u) | ○ |
| 🇿🇦 Южно-Африканская Республика | `za` | [countries/za.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/za.m3u) | ○ |
| 🇰🇷 Республика Корея | `kr` | [countries/kr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/kr.m3u) | ○ |
| 🇪🇸 Испания | `es` | [countries/es.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/es.m3u) | ○ |
| 🇱🇰 Шри-Ланка | `lk` | [countries/lk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/lk.m3u) | ○ |
| 🇸🇩 Судан | `sd` | [countries/sd.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sd.m3u) | ○ |
| 🇸🇷 Суринам | `sr` | [countries/sr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sr.m3u) | ○ |
| 🇸🇪 Швеция | `se` | [countries/se.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/se.m3u) | ○ |
| 🇨🇭 Швейцария | `ch` | [countries/ch.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ch.m3u) | ○ |
| 🇸🇾 Сирия | `sy` | [countries/sy.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/sy.m3u) | ○ |
| 🇹🇼 Тайвань | `tw` | [countries/tw.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/tw.m3u) | ○ |
| 🇹🇯 Таджикистан | `tj` | [countries/tj.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/tj.m3u) | ○ |
| 🇹🇿 Танзания | `tz` | [countries/tz.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/tz.m3u) | ○ |
| 🇹🇭 Таиланд | `th` | [countries/th.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/th.m3u) | ○ |
| 🇹🇬 Того | `tg` | [countries/tg.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/tg.m3u) | ○ |
| 🇹🇹 Тринидад и Тобаго | `tt` | [countries/tt.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/tt.m3u) | ○ |
| 🇹🇳 Тунис | `tn` | [countries/tn.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/tn.m3u) | ○ |
| 🇹🇷 Турция | `tr` | [countries/tr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/tr.m3u) | ○ |
| 🇹🇲 Туркменистан | `tm` | [countries/tm.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/tm.m3u) | ○ |
| 🇺🇬 Уганда | `ug` | [countries/ug.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ug.m3u) | ○ |
| 🇺🇦 Украина | `ua` | [countries/ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ☑️ |
| 🇦🇪 ОАЭ | `ae` | [countries/ae.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ae.m3u) | ○ |
| 🇺🇰 Великобритания | `uk` | [countries/uk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/uk.m3u) | ○ |
| 🇺🇸 Соединенные Штаты | `us` | [countries/us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/us.m3u) | ○ |
| 🇺🇾 Уругвай | `uy` | [countries/uy.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/uy.m3u) | ○ |
| 🇺🇿 Узбекистан | `uz` | [countries/uz.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/uz.m3u) | ○ |
| 🇻🇦 Ватикан | `va` | [countries/va.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/va.m3u) | ○ |
| 🇻🇪 Венесуэла | `ve` | [countries/ve.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ve.m3u) | ○ |
| 🇻🇳 Вьетнам | `vn` | [countries/vn.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/vn.m3u) | ○ |
| 🇪🇭 Западная Сахара | `eh` | [countries/eh.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/eh.m3u) | ○ |
| 🇾🇪 Йемен | `ye` | [countries/ye.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ye.m3u) | ○ |
| 🇿🇼 Зимбабве | `zw` | [countries/zw.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/zw.m3u) | ○ |

</details>

## 🛠 Как опубликовать недостающие файлы

При наличии уже созданных Bunny Storage и Pull Zone обновите локальные скрипты и запустите [команды публикации](BUNNY_ONE_CLICK.md), [зеркало всех стран](BUNNY_ONE_CLICK.md#country-playlists-all-countries-on-your-existing-bunny), [Pluto TV](QIST_PLUTOTV.md) или единый безопасный синхронизатор из [руководства](PUBLIC_RELEASE.md). Ключ вводится только локально в терминале.

После публикации проверяйте доступность HTTP + `#EXTM3U` и воспроизведение **на телевизоре**, особенно для ссылок `jmp2.uk` и 18+. Старые платные/рекламные заглушки не считаются качественными каналами.

## 📜 Происхождение и лицензии

Проект основан на [iptv-org/iptv](https://github.com/iptv-org/iptv). Списки IPTV-org прекращают распространять NSFW с 2024-01-30. Bunny-каталог — отдельная пользовательская сборка форка, **не официальный CDN IPTV-org**. Pluto TV, товарные знаки и оригинальный видеоконтент принадлежат правообладателям. Репозиторий хранит ссылки M3U, не видео. [История наших изменений](FORK_CHANGELOG.md).
