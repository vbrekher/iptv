# 🚀 Публикация полного IPTV-каталога на Bunny

[English](en/PUBLIC_RELEASE.md) · [Nederlands](nl/PUBLIC_RELEASE.md) · [Русский](PUBLIC_RELEASE.md)

**Это инструкция для владельца уже созданных зон, не для создания новых.**

- Storage Zone: lampa-iptv-875323ab-storage
- Pull Zone: lampa-iptv-875323ab-cdn
- CDN: https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/

### Подтверждённая проверка CDN — 2 ноября 2026 года

Владелец проверил через терминал **все 237 публичных M3U-ссылок**: **237 успешно, 0 ошибок**. Каждый файл вернул HTTP 206 и заголовок `#EXTM3U`. [Полный отчёт проверки](../catalog/cdn-verification-2026-11-02.json). Это подтверждает доставку M3U-файлов, но **не воспроизведение телеканалов**.

Предыдущий запуск загрузил 198 файлов (188 стран, общий список стран, шесть Pluto и три Clean). Новая проверка CDN охватила также файлы более ранних публикаций.


## Одна команда для Mac

Используй ту же папку ~/iptv-bunny, в которой была первая загрузка:

~~~bash
(
  set -euo pipefail
  cd "$HOME/iptv-bunny"
  for file in \
    personal_bunny_playlists.py \
    free_hls_filter.py \
    sync_bunny_countries.py \
    build_lampa_lite.py \
    lampa_category_fix.py \
    auto_bunny_setup.py \
    plutotv_bunny.py \
    publish_public_bunny.py
  do
    curl -fsSL --retry 3 \
      "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" \
      -o "$file"
  done
  python3 publish_public_bunny.py --self-test
  python3 publish_public_bunny.py
)
~~~

Терминал попросит Bunny Account API Key (hidden). **Не пересылай ключ**. Он не публикуется и не записывается в файл.

### Что произойдёт

1. Сбор списка 188 стран из IPTV-org. Если один M3U не доступен, он записывается в отчёт и **не считается загруженным**. Остальные страны продолжают обрабатываться.
2. Генерация шести Pluto TV M3U из публичных каталогов BuddyChewChew.
3. Если на Mac есть ранее сохранённые index.m3u и adult.m3u, создание исправленных Tizen/Category-файлов.
4. Проверка **существующих** Storage/Pull Zone и скрытый ввод одного Account API Key.
5. Загрузка только недостающих типов файлов: countries, Pluto, новые clean-плейлисты. **Не трогает adult.m3u, прежние категории и исходный index.m3u.**
6. Отчёт на Mac: dist/public-hub/publication-report.json с опубликованными именами и результатом CDN_CHECK.

## Другие режимы

| Режим | Команда |
|---|---|
| Только подготовка, без Bunny | python3 publish_public_bunny.py --dry-run |
| Только все доступные страны | python3 publish_public_bunny.py --only countries |
| Только Pluto | python3 publish_public_bunny.py --only pluto |
| Только чистые Samsung-плейлисты | python3 publish_public_bunny.py --only clean |
| Локальные тесты | python3 publish_public_bunny.py --self-test |

## Рекомендуемые ссылки после публикации

| Название | URL |
|---|---|
| Samsung Clean Lite | https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u |
| Pluto Lite | https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u |
| Pluto Germany | https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u |
| Pluto Erotic FAST | https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u |
| 🇷🇺 Россия | https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u |
| 🇺🇦 Украина | https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u |
| Все страны | https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u |

Весь каталог с флагами и статусами: [BUNNY_PLAYLISTS.md](BUNNY_PLAYLISTS.md).

## Диагностика

- **Bunny 401:** должен использоваться writable пароль Storage Zone, а не Account Key. Встроенный retry не создаёт новые зоны.
- **Pluto не воспроизводится:** HLS выдаёт сторонний jmp2.uk; возможны геоблокировки. Исходный M3U не равен гарантированному видео.
- **Медленное открытие на Samsung:** выбирай плейлисты Lite, а не 3000+ или 11000+ записей.
- **Pay for a subscription:** это кадры внешнего источника, не ошибка CDN.
- **Failed upload to CUB:** отдельная операция IPTV-плагина, не Bunny PUT.
- **Секреты:** не добавляй личные IPTV-подписки, API ключи и токены в публичный GitHub.
