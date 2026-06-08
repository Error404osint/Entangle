# 🕸️ Entangle

**Entangle** — терминальный OSINT-инструмент для ручного поиска информации. Генерирует Google Dorks по username, email, телефону, криптоадресам, ФИО и геолокации.

| Language | Description |
|----------|-------------|
| 🇬🇧 English | OSINT tool for manual dork generation by username, email, phone, crypto, FIO and geolocation |
| 🇷🇺 Русский | OSINT-инструмент для ручной генерации дорков по username, email, телефону, крипто, ФИО и геолокации |
| 🇺🇦 Українська | OSINT-інструмент для ручної генерації дорків за username, email, телефоном, крипто, ПІБ та геолокацією |

---

## 📦 Установка / Installation

### Требования / Requirements
- Python 3.6 или выше / Python 3.6 or higher

### Установка / Setup

git clone https://github.com/errorov404/Entangle.git
cd Entangle
python3 entangle.py
введи это по очереди в cmd или terminal 




Пошаговая инструкция:
Выбери язык — English, Русский или Українська

Выбери режим:

1 — Интерактивный режим (рекомендуется)

2 — Одиночная цель (быстрый поиск)

Введи идентификатор:

@username — для Telegram

email@example.com — для email

+79991234567 — для телефона

1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa — для крипто

Иван Иванов — для ФИО

Копируй каждый дорк → вставляй в браузер → нажимай Enter

Оценивай полезность (1-5, где 5 — очень полезно, 0 — пропустить)

Вводи найденные ники (например, insta:john_doe, twitter:johndoe)

В конце сохрани отчёт на рабочий стол

✨ Возможности / Features
Модуль / Module	Поиск / Search
📡 Telegram	site:t.me, fanstat.ru, telelog.io, tgstat.ru
📸 Instagram	site:instagram.com, linktr.ee, picuki.com
🐦 Twitter	site:twitter.com, nitter.net
💻 GitHub	site:github.com, commits, gist
📧 Email	pastebin.com, github.com
📱 Phone	pastebin.com, telegram
💰 Crypto	bitcointalk.org, transaction
👤 FIO	vk.com, ok.ru, linkedin.com
🗺️ Geo	vk.com, telegram
📦 Archive	Wayback Machine


📸 Пример работы / Example
 Введите @username (несколько через пробел или запятую):   
  > @errorov404                                              

  TELEGRAM ДОРКИ для @errorov404
  [1/9] site:t.me/ + "@errorov404"
  COPY this dork → PASTE into browser → PRESS ENTER


Оцените этот дорк (1-5, 1=бесполезно, 5=очень полезно, или 0=пропустить)
> 5

  [+] Добавлено (оценка: 5/5)

  📁 Отчёт / Report
После завершения сессии отчёт автоматически сохраняется на Рабочий стол в папку:
Desktop/Entangle_Reports/entangle_20241215_143022.txt
Desktop/Entangle_Reports/entangle_20241215_143022.html
В отчёт попадают только дорки с оценкой 4 или 5.

⚠️ Предупреждение / Warning
🛡️ Данный инструмент предназначен ТОЛЬКО для образовательных целей и для тестирования собственной цифровой безопасности.
This tool is intended ONLY for educational purposes and for testing your own digital security.
Не используйте для несанкционированного сбора данных о третьих лицах!
Do not use for unauthorized data collection!

👤 Автор / Author
Created by: @errorov404
