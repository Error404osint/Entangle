#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Entangle - OSINT Spider That Weaves Identities
# Created by: @errorov404

import os
import re
from datetime import datetime
from pathlib import Path

# ==================== КОНСТАНТЫ ====================
DESKTOP_PATH = Path.home() / "Desktop" / "Entangle_Reports"
DESKTOP_PATH.mkdir(parents=True, exist_ok=True)

# ==================== ЛОГОТИП ====================
LOGO = r"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     ███████╗███╗   ██╗████████╗ █████╗ ███╗   ██╗ ██████╗ ██╗███████╗        ║
║     ██╔════╝████╗  ██║╚══██╔══╝██╔══██╗████╗  ██║██╔════╝ ██║██╔════╝        ║
║     █████╗  ██╔██╗ ██║   ██║   ███████║██╔██╗ ██║██║  ███╗██║█████╗          ║
║     ██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║╚██╗██║██║   ██║██║██╔══╝          ║
║     ███████╗██║ ╚████║   ██║   ██║  ██║██║ ╚████║╚██████╔╝██║███████╗        ║
║     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚══════╝        ║
║                                                                              ║
║                    The OSINT Spider That Weaves Identities                   ║
║                              Created by: @errorov404                         ║
║                                                                              ║
║                    FOR EDUCATIONAL AND LEGAL PURPOSES ONLY!                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ==================== ГЕНЕРАЦИЯ ДОРКОВ ====================

def get_telegram_dorks(username):
    username = username.lstrip('@')
    return [
        f'site:t.me/ + "@{username}"',
        f'site:telegram.me + "{username}"',
        f'"t.me/{username}"',
        f'"{username}" site:pastebin.com',
        f'"{username}" "telegram" site:github.com',
        f'https://fanstat.ru/user/@{username}',
        f'https://telelog.io/@{username}',
        f'https://tgstat.ru/chat/@{username}',
        f'"{username}" "bio" site:t.me'
    ]

def get_instagram_dorks(username):
    return [
        f'site:instagram.com "{username}"',
        f'"{username}" site:linktr.ee',
        f'https://www.picuki.com/profile/{username}'
    ]

def get_twitter_dorks(username):
    return [
        f'site:twitter.com "{username}"',
        f'"{username}" site:nitter.net'
    ]

def get_github_dorks(username):
    return [
        f'site:github.com "{username}"',
        f'"{username}" "commits" site:github.com'
    ]

def get_email_dorks(email):
    return [
        f'"{email}" site:pastebin.com',
        f'"{email}" site:github.com'
    ]

def get_phone_dorks(phone):
    phone_clean = re.sub(r'\D', '', phone)
    return [
        f'"{phone_clean}" site:pastebin.com',
        f'"{phone_clean}" "telegram"'
    ]

def get_crypto_dorks(address):
    return [
        f'"{address}" site:bitcointalk.org',
        f'"{address}" "transaction"'
    ]

def get_fio_dorks(name):
    return [
        f'"{name}" site:vk.com',
        f'"{name}" site:ok.ru',
        f'"{name}" site:linkedin.com'
    ]

def get_geo_dorks(location):
    return [
        f'"{location}" site:vk.com',
        f'"живу в {location}" site:t.me'
    ]

def get_archive_dorks(site):
    site = re.sub(r'^https?://', '', site)
    return [
        f'https://web.archive.org/web/*/http://{site}',
        f'https://web.archive.org/web/*/https://{site}'
    ]

def detect_type(identifier):
    identifier = identifier.strip()
    
    if identifier.startswith('@'):
        return 'telegram', identifier
    
    if '@' in identifier and '.' in identifier:
        return 'email', identifier
    
    if re.match(r'^\+?\d{10,15}$', re.sub(r'\D', '', identifier)):
        return 'phone', identifier
    
    if re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', identifier) or identifier.startswith('0x'):
        return 'crypto', identifier
    
    if ' ' in identifier and len(identifier.split()) >= 2:
        return 'fio', identifier
    
    return 'username', identifier

# ==================== ЯЗЫКИ ====================

LANG_RU = {
    'name': 'Русский 🇷🇺',
    'enter_usernames': 'Введите @username (несколько через пробел или запятую):\nПодсказка: ники можно найти на fanstat.ru, telelog.io, tgstat.ru\n> ',
    'no_usernames': 'Ни одного username не введено!',
    'enter_nicks': '\nНашли новые ники? (через запятую)\nПример: insta:john, twitter:john, github:john\n> ',
    'enter_site': '\nЗнаете сайт пользователя? (Enter чтобы пропустить)\n> ',
    'enter_location': '\nНашли геолокацию? (Enter чтобы пропустить)\n> ',
    'enter_fullname': '\nНашли полное имя? (Enter чтобы пропустить)\n> ',
    'enter_crypto': '\nНашли криптоадрес? (Enter чтобы пропустить)\n> ',
    'enter_phone': '\nНашли номер телефона? (Enter чтобы пропустить)\n> ',
    'enter_email': '\nНашли email? (Enter чтобы пропустить)\n> ',
    'continue': '\nПродолжить? (да/нет)\n> ',
    'rate': 'Оцените этот дорк (1-5, 1=бесполезно, 5=очень полезно, или 0=пропустить)\n> ',
    'save': '\nСохранить отчёт на Рабочий стол? (да/нет)\n> ',
    'filename': 'Имя файла (Enter для авто-имени)\n> ',
    'press_enter': 'Нажмите Enter для продолжения...',
    'goodbye': 'До свидания! Соблюдайте закон!',
    'saved': 'Отчёт сохранён: {}',
    'collected': 'Собрано {} полезных дорков (оценка 4-5)',
    'no_useful': 'Нет полезных дорков (оценка 4-5).',
    'dork_instruction': 'СКОПИРУЙТЕ этот дорк → ВСТАВЬТЕ в браузер → НАЖМИТЕ Enter',
    'telegram_title': 'TELEGRAM ДОРКИ для @{}',
    'instagram_title': 'INSTAGRAM ДОРКИ для {}',
    'twitter_title': 'TWITTER ДОРКИ для {}',
    'github_title': 'GITHUB ДОРКИ для {}',
    'email_title': 'EMAIL ДОРКИ для {}',
    'phone_title': 'ДОРКИ ПО ТЕЛЕФОНУ для {}',
    'crypto_title': 'КРИПТО ДОРКИ для {}',
    'fio_title': 'ДОРКИ ПО ФИО для {}',
    'geo_title': 'ГЕОДОРКИ для {}',
    'archive_title': 'АРХИВНЫЕ ДОРКИ для {}',
    'universal_title': 'УНИВЕРСАЛЬНЫЙ ПОИСК для {}',
    'menu_interactive': '1. Интерактивный режим (сплести паутину) - РЕКОМЕНДУЕТСЯ',
    'menu_single': '2. Одиночная цель (быстрый поиск)',
    'menu_exit': '3. Выход'
}

LANG_EN = {
    'name': 'English 🇬🇧',
    'enter_usernames': 'Enter @username(s) (separate by space or comma):\nTip: Find usernames on fanstat.ru, telelog.io, tgstat.ru\n> ',
    'no_usernames': 'No usernames entered!',
    'enter_nicks': '\nFound new nicknames? (comma separated)\nExample: insta:john, twitter:john, github:john\n> ',
    'enter_site': '\nKnow the user\'s website? (press Enter to skip)\n> ',
    'enter_location': '\nFound location? (press Enter to skip)\n> ',
    'enter_fullname': '\nFound full name? (press Enter to skip)\n> ',
    'enter_crypto': '\nFound crypto address? (press Enter to skip)\n> ',
    'enter_phone': '\nFound phone number? (press Enter to skip)\n> ',
    'enter_email': '\nFound email? (press Enter to skip)\n> ',
    'continue': '\nContinue? (yes/no)\n> ',
    'rate': 'Rate this dork (1-5, 1=useless, 5=very useful, or 0=skip)\n> ',
    'save': '\nSave report to Desktop? (yes/no)\n> ',
    'filename': 'Filename (press Enter for auto-name)\n> ',
    'press_enter': 'Press Enter to continue...',
    'goodbye': 'Goodbye! Stay legal!',
    'saved': 'Report saved to: {}',
    'collected': 'Collected {} useful dorks (rated 4-5)',
    'no_useful': 'No useful dorks marked (4-5).',
    'dork_instruction': 'COPY this dork → PASTE into browser → PRESS ENTER',
    'telegram_title': 'TELEGRAM DORKS for @{}',
    'instagram_title': 'INSTAGRAM DORKS for {}',
    'twitter_title': 'TWITTER DORKS for {}',
    'github_title': 'GITHUB DORKS for {}',
    'email_title': 'EMAIL DORKS for {}',
    'phone_title': 'PHONE DORKS for {}',
    'crypto_title': 'CRYPTO DORKS for {}',
    'fio_title': 'FIO DORKS for {}',
    'geo_title': 'GEO DORKS for {}',
    'archive_title': 'ARCHIVE DORKS for {}',
    'universal_title': 'UNIVERSAL SEARCH for {}',
    'menu_interactive': '1. Interactive mode (weave the web) - RECOMMENDED',
    'menu_single': '2. Single target (quick search)',
    'menu_exit': '3. Exit'
}

LANG_UA = {
    'name': 'Українська 🇺🇦',
    'enter_usernames': 'Введіть @username (декілька через пробіл або кому):\nПідказка: ніки можна знайти на fanstat.ru, telelog.io, tgstat.ru\n> ',
    'no_usernames': 'Жодного username не введено!',
    'enter_nicks': '\nЗнайшли нові ніки? (через кому)\nПриклад: insta:john, twitter:john, github:john\n> ',
    'enter_site': '\nЗнаєте сайт користувача? (Enter щоб пропустити)\n> ',
    'enter_location': '\nЗнайшли геолокацію? (Enter щоб пропустити)\n> ',
    'enter_fullname': '\nЗнайшли повне ім\'я? (Enter щоб пропустити)\n> ',
    'enter_crypto': '\nЗнайшли криптоадресу? (Enter щоб пропустити)\n> ',
    'enter_phone': '\nЗнайшли номер телефону? (Enter щоб пропустити)\n> ',
    'enter_email': '\nЗнайшли email? (Enter щоб пропустити)\n> ',
    'continue': '\nПродовжити? (так/ні)\n> ',
    'rate': 'Оцініть цей дорк (1-5, 1=марно, 5=дуже корисно, або 0=пропустити)\n> ',
    'save': '\nЗберегти звіт на Робочий стіл? (так/ні)\n> ',
    'filename': 'Ім\'я файлу (Enter для авто-імені)\n> ',
    'press_enter': 'Натисніть Enter для продовження...',
    'goodbye': 'До побачення! Дотримуйтесь закону!',
    'saved': 'Звіт збережено: {}',
    'collected': 'Зібрано {} корисних дорків (оцінка 4-5)',
    'no_useful': 'Немає корисних дорків (оцінка 4-5).',
    'dork_instruction': 'СКОПІЮЙТЕ цей дорк → ВСТАВТЕ в браузер → НАТИСНІТЬ Enter',
    'telegram_title': 'TELEGRAM ДОРКИ для @{}',
    'instagram_title': 'INSTAGRAM ДОРКИ для {}',
    'twitter_title': 'TWITTER ДОРКИ для {}',
    'github_title': 'GITHUB ДОРКИ для {}',
    'email_title': 'EMAIL ДОРКИ для {}',
    'phone_title': 'ДОРКИ ЗА ТЕЛЕФОНОМ для {}',
    'crypto_title': 'КРИПТО ДОРКИ для {}',
    'fio_title': 'ДОРКИ ЗА ПІБ для {}',
    'geo_title': 'ГЕОДОРКИ для {}',
    'archive_title': 'АРХІВНІ ДОРКИ для {}',
    'universal_title': 'УНІВЕРСАЛЬНИЙ ПОШУК для {}',
    'menu_interactive': '1. Інтерактивний режим (сплести павутину) - РЕКОМЕНДУЄТЬСЯ',
    'menu_single': '2. Одинарна ціль (швидкий пошук)',
    'menu_exit': '3. Вихід'
}

# ==================== ОСНОВНОЙ КЛАСС ====================

class Entangle:
    def __init__(self):
        self.useful_dorks = []
        self.usernames = []
        self.lang = LANG_RU
    
    def show_header(self):
        clear()
        print(LOGO)
    
    def rate_dork(self, dork, num, total):
        print(f"\n{'─'*60}")
        print(f"  {self.lang['dork_instruction']}")
        print(f"{'─'*60}")
        print(f"\n  [{num}/{total}] {dork}")
        print(f"{'─'*60}")
        
        while True:
            rating = input(f"\n{self.lang['rate']}")
            if rating in ['0', 'skip']:
                return None
            if rating in ['1', '2', '3', '4', '5']:
                return int(rating)
            print("  Неверный ввод. Введите 1-5, 0 или skip")
    
    def show_dorks(self, title, dorks, category, target):
        if not dorks:
            return []
        
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}")
        
        results = []
        for i, dork in enumerate(dorks, 1):
            rating = self.rate_dork(dork, i, len(dorks))
            
            if rating and rating >= 4:
                results.append({
                    'dork': dork,
                    'rating': rating,
                    'category': category,
                    'target': target
                })
                print(f"\n  [+] Добавлено (оценка: {rating}/5)")
            elif rating:
                print(f"\n  [-] Не добавлено (оценка: {rating}/5) — нужно 4-5")
            else:
                print(f"\n  [~] Пропущено")
            
            if i < len(dorks):
                input(f"\n{self.lang['press_enter']}")
                self.show_header()
                print(f"\n{'='*60}")
                print(f"  {title} (продолжение)")
                print(f"{'='*60}")
        
        return results
    
    def process(self, identifier, id_type=None):
        if id_type is None:
            id_type, value = detect_type(identifier)
        else:
            value = identifier
        
        if id_type == 'telegram':
            dorks = get_telegram_dorks(value)
            title = self.lang['telegram_title'].format(value.lstrip('@'))
            return self.show_dorks(title, dorks, 'telegram', value)
        
        elif id_type == 'instagram':
            dorks = get_instagram_dorks(value)
            title = self.lang['instagram_title'].format(value)
            return self.show_dorks(title, dorks, 'instagram', value)
        
        elif id_type == 'twitter':
            dorks = get_twitter_dorks(value)
            title = self.lang['twitter_title'].format(value)
            return self.show_dorks(title, dorks, 'twitter', value)
        
        elif id_type == 'github':
            dorks = get_github_dorks(value)
            title = self.lang['github_title'].format(value)
            return self.show_dorks(title, dorks, 'github', value)
        
        elif id_type == 'email':
            dorks = get_email_dorks(value)
            title = self.lang['email_title'].format(value)
            return self.show_dorks(title, dorks, 'email', value)
        
        elif id_type == 'phone':
            dorks = get_phone_dorks(value)
            title = self.lang['phone_title'].format(value)
            return self.show_dorks(title, dorks, 'phone', value)
        
        elif id_type == 'crypto':
            dorks = get_crypto_dorks(value)
            title = self.lang['crypto_title'].format(value)
            return self.show_dorks(title, dorks, 'crypto', value)
        
        elif id_type == 'fio':
            dorks = get_fio_dorks(value)
            title = self.lang['fio_title'].format(value)
            return self.show_dorks(title, dorks, 'fio', value)
        
        elif id_type == 'geo':
            dorks = get_geo_dorks(value)
            title = self.lang['geo_title'].format(value)
            return self.show_dorks(title, dorks, 'geo', value)
        
        elif id_type == 'archive':
            dorks = get_archive_dorks(value)
            title = self.lang['archive_title'].format(value)
            return self.show_dorks(title, dorks, 'archive', value)
        
        else:
            all_dorks = []
            all_dorks.extend(get_telegram_dorks(value))
            all_dorks.extend(get_instagram_dorks(value))
            all_dorks.extend(get_twitter_dorks(value))
            all_dorks.extend(get_github_dorks(value))
            title = self.lang['universal_title'].format(value)
            return self.show_dorks(title, all_dorks, 'universal', value)
    
    def save_report(self):
        if not self.useful_dorks:
            print(f"\n{self.lang['no_useful']}")
            return
        
        filename = input(f"\n{self.lang['filename']}")
        if not filename.strip():
            filename = f"entangle_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        txt_path = DESKTOP_PATH / f"{filename}.txt"
        
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("ENTANGLE OSINT REPORT\n")
            f.write("="*80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Useful dorks: {len(self.useful_dorks)}\n")
            f.write(f"Usernames: {', '.join(self.usernames)}\n")
            f.write("="*80 + "\n\n")
            
            for i, d in enumerate(self.useful_dorks, 1):
                f.write(f"[{i}] Rating: {d['rating']}/5 | {d['category'].upper()}: {d['target']}\n")
                f.write(f"    {d['dork']}\n")
                f.write(f"    Google: https://www.google.com/search?q={d['dork'].replace(' ', '+')}\n\n")
        
        print(f"\n{self.lang['saved'].format(txt_path)}")
    
    def interactive_mode(self):
        self.show_header()
        
        print(f"\n{self.lang['enter_usernames']}")
        inp = input().strip()
        
        if not inp:
            print(f"\n{self.lang['no_usernames']}")
            input(f"\n{self.lang['press_enter']}")
            return
        
        usernames = re.split(r'[, ]+', inp)
        self.usernames = [u.strip() for u in usernames if u.strip()]
        
        for username in self.usernames:
            results = self.process(username)
            if results:
                self.useful_dorks.extend(results)
        
        while True:
            self.show_header()
            
            print(f"\n{self.lang['enter_nicks']}")
            nicks = input().strip()
            if nicks:
                for nick in nicks.split(','):
                    nick = nick.strip()
                    if nick:
                        if ':' in nick:
                            parts = nick.split(':', 1)
                            ptype = parts[0]
                            pvalue = parts[1]
                            type_map = {'insta': 'instagram', 'twitter': 'twitter', 'git': 'github'}
                            ptype = type_map.get(ptype, ptype)
                            results = self.process(pvalue, ptype)
                        else:
                            results = self.process(nick)
                        if results:
                            self.useful_dorks.extend(results)
            
            print(f"\n{self.lang['enter_site']}")
            site = input().strip()
            if site:
                results = self.process(site, 'archive')
                if results:
                    self.useful_dorks.extend(results)
            
            print(f"\n{self.lang['enter_location']}")
            loc = input().strip()
            if loc:
                results = self.process(loc, 'geo')
                if results:
                    self.useful_dorks.extend(results)
            
            print(f"\n{self.lang['enter_fullname']}")
            fio = input().strip()
            if fio:
                results = self.process(fio, 'fio')
                if results:
                    self.useful_dorks.extend(results)
            
            print(f"\n{self.lang['enter_crypto']}")
            crypto = input().strip()
            if crypto:
                results = self.process(crypto, 'crypto')
                if results:
                    self.useful_dorks.extend(results)
            
            print(f"\n{self.lang['enter_phone']}")
            phone = input().strip()
            if phone:
                results = self.process(phone, 'phone')
                if results:
                    self.useful_dorks.extend(results)
            
            print(f"\n{self.lang['enter_email']}")
            email = input().strip()
            if email:
                results = self.process(email, 'email')
                if results:
                    self.useful_dorks.extend(results)
            
            print(f"\n{self.lang['continue']}")
            cont = input().strip().lower()
            if cont in ['no', 'n', 'нет', 'н', 'ні']:
                break
        
        if self.useful_dorks:
            print(f"\n{self.lang['collected'].format(len(self.useful_dorks))}")
            save = input(f"\n{self.lang['save']}")
            if save.lower() in ['yes', 'y', 'да', 'д', 'так']:
                self.save_report()
        else:
            print(f"\n{self.lang['no_useful']}")
        
        input(f"\n{self.lang['press_enter']}")
    
    def single_mode(self):
        self.show_header()
        
        print(f"\n{self.lang['enter_usernames']}")
        inp = input().strip()
        
        if not inp:
            print(f"\n{self.lang['no_usernames']}")
            input(f"\n{self.lang['press_enter']}")
            return
        
        self.usernames = [inp]
        results = self.process(inp)
        if results:
            self.useful_dorks.extend(results)
        
        if self.useful_dorks:
            save = input(f"\n{self.lang['save']}")
            if save.lower() in ['yes', 'y', 'да', 'д', 'так']:
                self.save_report()
        
        input(f"\n{self.lang['press_enter']}")
    
    def select_language(self):
        self.show_header()
        print("\n" + "="*60)
        print("  Select language / Выберите язык")
        print("="*60)
        print("  1. English 🇬🇧")
        print("  2. Русский 🇷🇺")
        print("  3. Українська 🇺🇦")
        print("="*60)
        
        choice = input("\n  > ")
        if choice == '1':
            self.lang = LANG_EN
        elif choice == '2':
            self.lang = LANG_RU
        elif choice == '3':
            self.lang = LANG_UA
        else:
            self.lang = LANG_RU
        
        self.show_header()
        print(f"\n✓ Language set to: {self.lang['name']}")
        input(f"\n{self.lang['press_enter']}")
    
    def run(self):
        self.select_language()
        
        while True:
            self.show_header()
            print(f"\n{'='*60}")
            print(f"  {self.lang['menu_interactive']}")
            print(f"  {self.lang['menu_single']}")
            print(f"  {self.lang['menu_exit']}")
            print(f"{'='*60}")
            
            choice = input("\n  > ")
            
            if choice == '1':
                self.interactive_mode()
            elif choice == '2':
                self.single_mode()
            elif choice == '3':
                self.show_header()
                print(f"\n{self.lang['goodbye']}\n")
                break
            else:
                print("  Invalid choice / Неверный выбор")
                input(f"\n{self.lang['press_enter']}")

# ==================== ЗАПУСК ====================

if __name__ == "__main__":
    app = Entangle()
    app.run()