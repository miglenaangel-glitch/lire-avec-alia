# БИБЛИЯ НА ПРОЕКТА — Lire avec Alia
**Версия:** 1.0
**Дата:** 2026-06-03
**Owner:** Miglena Angelova
**Статус:** Production — MVP

---

## Как се чете този документ

Документът описва всичко изградено до момента. Всеки елемент има статус:
- ✅ **изградено**
- 🔧 **частично изградено**
- 📋 **планирано**
- ⚠️ **техдълг**

---

## РАЗДЕЛ 1. ИДЕНТИЧНОСТ НА ПРОЕКТА

### 1.1. Основни данни

| Поле | Стойност |
|------|----------|
| Официално име | Lire avec Alia |
| Домейн | alia-adri.com |
| URL | https://alia-adri.com |
| GitHub | https://github.com/miglenaangel-glitch/lire-avec-alia |
| Основател | Miglena Angelova |
| Юридически субект | Физическо лице |
| Версия на Библията | 1.0 |
| Начало | 2026-06-03 |
| Текущ статус | **Production MVP** |

### 1.2. Мисия и смисъл

Проектът е уеб приложение за ограмотяване на **Alia** — 13-годишно момиче с кохлеарен имплант, живеещо в Париж. Alia чува добре благодарение на импланта, но обработката на фонеми е по-трудна отколкото при чуващи деца.

**Методология:** Apili (apili.fr) — мултисензорен, сричков метод, създаден от логопед Benjamin Stevens.

**Основни принципи:**
- Alia е ПЪРВА — тя чете/произнася, системата оценява
- Три цвята навсякъде: съгласни=тъмносин, гласни=тъмночервен, неми=сиво
- Визуалното правило замества обяснението
- Микрофонът е основен инструмент за взаимодействие
- Системата говори на глас — Alia още не може да чете
- Наградата се показва при ≥ 70% точност

**Какво никога не бива да се наруши:**
- Цветовата система на Apili
- Строгата прогресия на нивата (не се прескача)
- Езикът на интерфейса — само френски
- Alia е ПЪРВА — системата не чете преди нея

### 1.3. Обхват

**Влиза:**
- Детски интерфейс `/` — Alia
- Родителски кабинет `/parent` — Майката
- 5 нива на упражнения по Apili
- Speech Recognition (микрофон)
- Text-to-Speech (Web Speech API)
- Система за награди с персонаж
- Claude API за генериране на изречения и резюме

**Не влиза (засега):**
- Регистрация/логин система ⚠️
- Push нотификации
- Мобилно приложение
- Multiplayer / social функции

---

## РАЗДЕЛ 2. БИЗНЕС РАМКА

### 2.1. Бизнес модел

- **Тип:** Персонален проект / семейна употреба
- **Монетизация:** Няма (MVP за Alia)
- **Целева аудитория:** 1 потребител — Alia, 13 г., Париж
- **Вторична аудитория:** Майката (родителски кабинет)

### 2.2. Целеви аудитории

| Роля | Интерфейс | Достъп |
|------|-----------|--------|
| Alia | `/` (child) | Свободен |
| Майката | `/parent` | Парола: `maman` |

---

## РАЗДЕЛ 3. ПРОДУКТОВА ЛОГИКА

### 3.1. Основни модули

| Модул | Път | Статус |
|-------|-----|--------|
| Home screen | `/` | ✅ |
| Les voyelles | `/child/exercise/voyelles` | ✅ |
| Les consonnes | `/child/exercise/consonnes_1` | ✅ |
| Lecture rapide | `/child/exercise/lecture_rapide` | ✅ |
| Les mots | `/child/exercise/mots_simples` | ✅ |
| Les phrases | `/child/exercise/phrases` | ✅ |
| Reward screen | `/child/reward/<id>` | ✅ |
| Parent dashboard | `/parent/` | ✅ |
| Parent progress | `/parent/progress` | ✅ |
| Parent settings | `/parent/settings` | ✅ |

### 3.2. Потребителски роли

**Alia (child):**
- Вижда home екрана с Karumi
- Избира упражнение
- Използва микрофон за произнасяне
- Получава оценка и обратна връзка на глас
- Получава наградата при ≥ 70% точност

**Майката (parent):**
- Влиза с парола `maman` (plain text — ⚠️ техдълг)
- Вижда седмична статистика
- Вижда AI резюме на прогреса
- Вижда трудни/усвоени елементи
- Сменя активния персонаж
- Добавя/трие фрази за наградата

### 3.3. Протокол на взаимодействие (универсален)

Прилага се за: **сричките, думите, фразите**

1. Системата показва елемента (с Apili цветове)
2. Системата произнася на глас подканата: *"Appuie sur le micro et lis [la syllabe / le mot / la phrase] !"*
3. **Alia е ПЪРВА** — натиска микрофона и произнася
4. Системата изчаква 3 секунди пауза след края на речта
5. Оценка:
   - **≥ 80% съвпадение** → "Bravo ! 🎉" (изговаря) + системата произнася елемента
   - **50-80% съвпадение** → "Bien essayé ! Réessaie !" (изговаря) + системата произнася елемента
   - **< 50% съвпадение** → "Réessaie ! 💪" (изговаря) + системата произнася елемента
6. Показват се бутони: **Répéter** и **Suivant**

**За voyelles:** Системата задава задача: "Appuie sur le [буква] !" → Alia натиска правилната карта → Bravo/Non.

### 3.4. Правило за оцветяване (Apili)

```
Съгласни → #1a3a6b (тъмносин)
Гласни   → #c0392b (тъмночервен)
Неми     → #b0a090 (светлосив)

Гласни: a â à e é è ê ë i î ï o ô u û ù y

Неми букви:
- финално 'e' → само ако думата има друга гласна (le, de = червено!)
- финални s, t, d, x, z, p → сиво
- 'h' в digraph 'ch', 'ph', 'gn' → синьо (част от съгласния звук)
- самостоятелно 'h' → сиво

Digraphs (две букви = един звук = и двете сини):
- ch → [ʃ]
- ph → [f]
- gn → [ɲ]
- qu → q(синьо) + u(сиво)
```

### 3.5. Прогресия на нивата (строга — не се прескача)

| Ниво | Ключ | Тип упражнение |
|------|------|----------------|
| 0 | `voyelles` | `tap_to_hear` — намери буквата |
| 1 | `consonnes_1` | `slide_to_merge` — слей сричката |
| 2 | `lecture_rapide` | `rapid_read` — таблица сричка по сричка |
| 3 | `mots_simples` | `word_tap` — произнеси думата |
| 4 | `phrases` | `sentence_read` — произнеси изречението |

---

## РАЗДЕЛ 4. ПРАВИЛА НА ПРОДУКТА

### 4.1. Абсолютни правила

1. **Само френски** в интерфейса на Alia — никакъв друг език
2. **Alia е ПЪРВА** — системата не произнася преди нея (освен подканата)
3. **Цветовата система на Apili** се спазва навсякъде
4. **Линията между съгласна и гласна** е ключов визуален елемент (slide animation)
5. **Web Speech API** — езикът е винаги `fr-FR`, rate: 0.6, pitch: 1.1
6. **Наградата** се показва само при ≥ 70% точност, минимум 20 упражнения
7. **Никога не се прескача ниво** — прогресията е строга
8. **Системата говори на глас подканата** — Alia не може да чете

### 4.2. CSS правило (научено от опит)

> **Контейнер с `color` override-ва child `span` цветовете.**
> Когато има оцветени child елементи, контейнерът НИКОГА не трябва да има `color`.
> Дефинирай child цветовете с пълния selector: `.parent .child { color: ... }`

---

## РАЗДЕЛ 5. UX / UI / ДИЗАЙН СИСТЕМА

### 5.1. Идентичност

**Child интерфейс (Alia):**
- Светла тема — кремав фон, вдъхновена от книга
- Фон: `#fdf8f0`
- Accent: `#c2622a` (топло оранжево-кафяво)
- Шрифт заглавие: Georgia/serif (за буквите)
- Шрифт UI: Nunito (Google Fonts)
- Персонаж Karumi плава с CSS animation

**Parent интерфейс (Майката):**
- Светла тема, информативна
- Фон: `#f8fafc`
- Accent: `#7c3aed` (лилаво)
- Шрифт: Nunito

### 5.2. Компоненти

| Компонент | Клас | Описание |
|-----------|------|----------|
| Level card | `.level-card` | Карта за ниво на home |
| Tap card | `.tap-card` | Карта за гласна |
| Mic button | `.mic-btn` | Микрофон бутон, пулсира в червено когато е активен |
| Next button | `.next-btn` | Следващ елемент |
| Reward character | `.reward-character` | Персонажът на наградата |
| Sentence display | `.sentence-display` | Показва фраза с Apili цветове |

### 5.3. UX правила

- ✅ Mobile-first (375px като baseline)
- ✅ Голям шрифт — мин. 20px за UI, 28px+ за букви/срички
- ✅ Dark mode за reward екрана (радиален градиент)
- ✅ Tap feedback — scale(0.92) при натискане
- ✅ Плаваща анимация на Karumi (3s ease-in-out)
- ⚠️ Няма auto-save — прогресът се записва при всяко взаимодействие

---

## РАЗДЕЛ 6. ТЕХНИЧЕСКА АРХИТЕКТУРА

### 6.1. Технологичен стек

| Слой | Технология | Версия |
|------|-----------|--------|
| Backend | Python + Flask | 2.0.3 |
| База данни | MySQL | 8.x |
| Web сървър | Nginx | 1.24.0 |
| WSGI сървър | Gunicorn | 26.0.0 |
| Frontend | Vanilla HTML/CSS/JS | — |
| Шрифтове | Google Fonts (Nunito) | — |
| AI | Anthropic API (HTTP) | claude-sonnet-4-20250514 |
| Глас | Web Speech API | вграден в браузъра |
| OS | Ubuntu | 24.04 LTS |

### 6.2. Архитектурен модел

- **Монолит** — Flask Blueprint структура
- **API-first** за запис на прогрес (`/api/record`)
- **No framework** на frontend — чист HTML/CSS/JS
- Anthropic API се извиква директно с `requests` (без SDK) — съвместимост с Python 3.12

### 6.3. Структура на репото

```
lire-avec-alia/
├── app.py                  # Flask app — главен файл
├── config.py               # Конфигурация от .env
├── passenger_wsgi.py       # WSGI entry point (не се ползва на VPS)
├── requirements.txt        # Python зависимости
├── .env                    # Secrets (не е в git)
├── .env.example            # Шаблон за .env
├── .gitignore
├── CLAUDE.md               # Инструкции за Claude Code
├── BIBLE.md                # Този документ
├── database/
│   └── schema.sql          # MySQL схема
├── routes/
│   ├── __init__.py
│   ├── child.py            # / и /child/* маршрути
│   ├── parent.py           # /parent/* маршрути
│   └── api.py              # /api/* маршрути
├── static/
│   ├── css/
│   │   ├── child.css       # Стил за детския интерфейс
│   │   └── parent.css      # Стил за родителския кабинет
│   ├── js/
│   │   └── reward.js       # Reward анимация + Web Speech
│   └── characters/
│       └── karumi.png      # Персонажът
└── templates/
    ├── base.html           # Open Graph meta тагове
    ├── child/
    │   ├── home.html
    │   ├── exercise.html
    │   └── reward.html
    └── parent/
        ├── dashboard.html
        ├── progress.html
        └── settings.html
```

---

## РАЗДЕЛ 7. ИНФРАСТРУКТУРА И СРЕДИ

### 7.1. Production (VPS)

| Поле | Стойност |
|------|----------|
| Доставчик | Hostinger VPS |
| IP | 72.61.21.43 |
| Домейн | alia-adri.com |
| OS | Ubuntu 24.04 LTS |
| Python | 3.12 |
| Код директория | `/var/www/lire-avec-alia/` |
| Venv | `/var/www/lire-avec-alia/venv/` |
| SSH user | root |
| SSH port | 22 |
| Web сървър | Nginx (reverse proxy → Gunicorn :5000) |
| Process manager | systemd service `alia.service` |
| SSL | Let's Encrypt (Certbot, auto-renew) |

### 7.2. Systemd service

```
/etc/systemd/system/alia.service
ExecStart: gunicorn -w 2 -b 127.0.0.1:5000 app:app
```

**Управление:**
```bash
systemctl start/stop/restart alia
systemctl status alia
journalctl -u alia -n 50 --no-pager
```

### 7.3. Nginx конфигурация

```
/etc/nginx/sites-available/alia
server_name: alia-adri.com www.alia-adri.com
SSL: /etc/letsencrypt/live/alia-adri.com/
Static: /var/www/lire-avec-alia/static → /static
Proxy: → 127.0.0.1:5000
```

### 7.4. Shared хостинг (не се ползва)

- Акаунт: u455273345 @ Hostinger
- IP: 45.95.182.155
- SSH port: 65002
- Там има MySQL база: `u455273345_lire_avec_alia` (не се ползва — MySQL е на VPS)

### 7.5. Deploy команда

```bash
ssh root@72.61.21.43
cd /var/www/lire-avec-alia
git pull
pkill -9 -f gunicorn && sleep 1 && systemctl start alia
```

---

## РАЗДЕЛ 8. КОД, REPOSITORY И РАЗРАБОТКА

### 8.1. Git управление

| Поле | Стойност |
|------|----------|
| Repository | https://github.com/miglenaangel-glitch/lire-avec-alia |
| Owner | miglenaangel-glitch |
| Main branch | `main` |
| Branch стратегия | Директно в main (solo project) |

### 8.2. Стандарти за разработка

- Python: PEP8, коментари на английски
- HTML/CSS/JS: коментари на английски
- Commit съобщения: на английски
- Имена на файлове: lowercase, snake_case
- Jinja2 шаблони: `{% block %}` структура

### 8.3. CI/CD

- ❌ Няма автоматичен CI/CD
- Deploy: ръчно `git pull` + рестартиране на Gunicorn

---

## РАЗДЕЛ 9. ИЗГРАЖДАНЕ ОТ НУЛАТА

### 9.1. Пълно възстановяване на VPS

```bash
# 1. Влез в сървъра
ssh root@72.61.21.43

# 2. Инсталирай зависимости
apt update && apt install -y python3 python3-pip python3-venv nginx git \
  default-libmysqlclient-dev pkg-config mysql-server

# 3. MySQL setup
mysql_secure_installation
mysql -u root <<EOF
CREATE DATABASE lire_avec_alia CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'alia'@'localhost' IDENTIFIED BY 'Alia2026!xK9m';
GRANT ALL PRIVILEGES ON lire_avec_alia.* TO 'alia'@'localhost';
FLUSH PRIVILEGES;
EOF

# 4. Клонирай кода
cd /var/www
git clone https://github.com/miglenaangel-glitch/lire-avec-alia.git
cd lire-avec-alia

# 5. Виртуална среда
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

# 6. .env файл
cat > .env << 'EOF'
ANTHROPIC_API_KEY=<ключът>
MYSQL_HOST=localhost
MYSQL_USER=alia
MYSQL_PASSWORD=Alia2026!xK9m
MYSQL_DB=lire_avec_alia
SECRET_KEY=lire-alia-secret-2026-xK9mP
EOF

# 7. Зареди схемата
mysql -u alia -p'Alia2026!xK9m' lire_avec_alia < database/schema.sql

# 8. Systemd service
cat > /etc/systemd/system/alia.service << 'EOF'
[Unit]
Description=Lire avec Alia Flask App
After=network.target

[Service]
User=root
WorkingDirectory=/var/www/lire-avec-alia
Environment="PATH=/var/www/lire-avec-alia/venv/bin"
ExecStart=/var/www/lire-avec-alia/venv/bin/gunicorn -w 2 -b 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload && systemctl enable alia && systemctl start alia

# 9. Nginx
cat > /etc/nginx/sites-available/alia << 'EOF'
server {
    listen 80;
    server_name alia-adri.com www.alia-adri.com;
    location /static { alias /var/www/lire-avec-alia/static; }
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
EOF
ln -s /etc/nginx/sites-available/alia /etc/nginx/sites-enabled/
nginx -t && systemctl restart nginx

# 10. SSL
apt install -y certbot python3-certbot-nginx
certbot --nginx -d alia-adri.com -d www.alia-adri.com

# 11. Firewall
ufw allow 80 && ufw allow 443
```

---

## РАЗДЕЛ 10. КОНФИГУРАЦИЯ И SECRETS

### 10.1. Environment variables

| Променлива | Задължителна | Описание |
|-----------|-------------|----------|
| `ANTHROPIC_API_KEY` | ✅ | Anthropic API ключ |
| `MYSQL_HOST` | ✅ | MySQL хост (localhost) |
| `MYSQL_USER` | ✅ | MySQL потребител |
| `MYSQL_PASSWORD` | ✅ | MySQL парола |
| `MYSQL_DB` | ✅ | Име на базата данни |
| `SECRET_KEY` | ✅ | Flask session secret |

### 10.2. Текущи стойности (production)

```
MYSQL_HOST=localhost
MYSQL_USER=alia
MYSQL_PASSWORD=Alia2026!xK9m
MYSQL_DB=lire_avec_alia
SECRET_KEY=lire-alia-secret-2026-xK9mP
```

⚠️ **ВАЖНО:** Паролата на MySQL базата (`iS@3BRnpq`) е за Hostinger shared хостинг — тя беше споделена в чат и трябва да се смени. VPS MySQL паролата е `Alia2026!xK9m`.

### 10.3. Anthropic API

- Модел: `claude-sonnet-4-20250514`
- Max tokens: 1000
- Извиква се директно с `requests` (не SDK) — HTTP POST към `https://api.anthropic.com/v1/messages`
- Причина: Anthropic SDK не е достъпен за Python 3.12 на сървъра (мрежов проблем с PyPI по времето на инсталация)

---

## РАЗДЕЛ 11. БАЗА ДАННИ

### 11.1. Обща карта

- **База:** MySQL 8.x на VPS (`lire_avec_alia`)
- **Потребител:** `alia`@`localhost`
- **Схема:** `/var/www/lire-avec-alia/database/schema.sql`

### 11.2. Таблици

```sql
sessions          -- Сесии на упражнения
progress          -- Прогрес по елементи (буква/сричка/дума/фраза)
characters        -- Персонажи за наградата
reward_phrases    -- Фрази за наградата
```

### 11.3. Критични полета

**progress:**
- `UNIQUE KEY (element_type, element_value)` — ON DUPLICATE KEY UPDATE
- `status ENUM('nouveau', 'en_cours', 'difficile', 'maitrise')`
- Статусът се изчислява автоматично: ≥5 правилни + ≥80% = `maitrise`; ≥2 опита + <50% = `difficile`

**sessions:**
- `reward_shown BOOLEAN` — предотвратява двойна награда
- `total_exercises` и `correct_answers` се обновяват при всеки `/api/record`

### 11.4. Default данни

```sql
-- При инсталация се вмъкват:
characters: Karumi (active=TRUE), Cinnamon (active=FALSE)
reward_phrases: 6 фрази за Alia
```

---

## РАЗДЕЛ 12. ФАЙЛОВЕ И MEDIA STORAGE

### 12.1. Персонажи

- Местоположение: `/var/www/lire-avec-alia/static/characters/`
- Текущо: `karumi.png` (440 KB, PNG)
- Достъп: публичен (сервира се от Nginx)
- Добавяне на нов персонаж: качи PNG + добави ред в таблица `characters`

---

## РАЗДЕЛ 13. ИНТЕГРАЦИИ И ВЪНШНИ УСЛУГИ

| Услуга | Роля | Статус | Owner |
|--------|------|--------|-------|
| Hostinger VPS | Хостинг | ✅ Production | Miglena |
| Hostinger Shared | Домейн купен оттам | ✅ | Miglena |
| GitHub | Code repository | ✅ | miglenaangel-glitch |
| Anthropic API | AI (изречения + резюме) | ✅ | Miglena |
| Let's Encrypt | SSL сертификат | ✅ Auto-renew | автоматично |
| Google Fonts | Nunito шрифт | ✅ CDN | N/A |
| Web Speech API | TTS + STT | ✅ Вграден в браузър | N/A |
| Hostinger Shared MySQL | Стара база (не се ползва) | ⚠️ Излишна | Miglena |

---

## РАЗДЕЛ 14. СИГУРНОСТ

### 14.1. Текущо състояние

| Защита | Статус | Бележка |
|--------|--------|---------|
| HTTPS / SSL | ✅ | Let's Encrypt |
| Firewall (ufw) | ✅ | 22, 80, 443 |
| MySQL — отделен потребител | ✅ | `alia`@`localhost` |
| Parent парола | ⚠️ **ТЕХДЪЛГ** | Plain text `maman` в JS |
| API ключ в .env | ✅ | Не е в git |
| .gitignore | ✅ | .env изключен |
| Root SSH | ⚠️ | Root достъп — препоръчително да се създаде отделен user |
| CSRF защита | ❌ | Няма |
| Rate limiting | ❌ | Няма |

### 14.2. Приоритетен техдълг (сигурност)

1. ⚠️ Паролата на `/parent` е plain text в JS — лесно се вижда в source кода. Трябва да се преместри на бекенда.
2. ⚠️ Root SSH — препоръчва се `sudo` потребител
3. ⚠️ Mysql паролата беше споделена в чат — да се смени

---

## РАЗДЕЛ 15. BACKUP И DISASTER RECOVERY

### 15.1. Текущо

- ❌ Няма автоматичен backup
- Кодът е в GitHub — това е единственият backup

### 15.2. Ръчно backup на база

```bash
mysqldump -u alia -p'Alia2026!xK9m' lire_avec_alia > backup_$(date +%Y%m%d).sql
```

### 15.3. Disaster recovery

При паднал VPS:
1. Вземи нов VPS (Hostinger или друг)
2. Следвай **Раздел 9.1** стъпка по стъпка
3. Кодът се клонира от GitHub
4. .env трябва да се пресъздаде ръчно (не е в git)
5. Базата данни — ако няма backup, се губи прогресът на Alia

---

## РАЗДЕЛ 16. РИСКОВЕ И ТЕХДЪЛГ

### 16.1. Known issues и техдълг

| Проблем | Приоритет | Бележка |
|---------|-----------|---------|
| Parent парола в JS | 🔴 Висок | Лесно заобикаляема |
| Няма backup на база | 🔴 Висок | Прогресът може да се изгуби |
| Root SSH достъп | 🟡 Среден | По-добре sudo user |
| Speech Recognition само в Chrome/Safari | 🟡 Среден | Firefox не поддържа |
| Gunicorn рестарт — `pkill -9` | 🟡 Среден | Грубо, но работи |
| Web Speech API гласовото качество | 🟢 Нисък | Chrome е машинен, Safari е по-добър |
| `passenger_wsgi.py` в репото | 🟢 Нисък | Не се ползва на VPS |
| Shared хостинг MySQL база (u455273345) | 🟢 Нисък | Празна, да се изтрие |

### 16.2. Рисков регистър

| Риск | Вероятност | Въздействие | Мерки |
|------|-----------|-------------|-------|
| VPS пада | Ниска | Висока | Backup процедура от Раздел 9 |
| Anthropic API промяна | Ниска | Средна | Лесна смяна на модел в config.py |
| Изтекъл SSL | Ниска | Висока | Let's Encrypt auto-renew |
| Загубен GitHub достъп | Много ниска | Висока | Локално копие на кода |

---

## РАЗДЕЛ 17. CHANGE LOG

### v1.0 — 2026-06-03 (днес)

**Изградено от нулата:**
- ✅ Flask skeleton с Blueprint архитектура
- ✅ MySQL схема с 4 таблици
- ✅ 5 типа упражнения (tap_to_hear, slide_to_merge, rapid_read, word_tap, sentence_read)
- ✅ Apili цветова система навсякъде (consonant=синьо, vowel=червено, silent=сиво)
- ✅ Digraph логика (ch, ph, gn, qu)
- ✅ Правило за финално 'e' (silent само ако има друга гласна)
- ✅ Speech Recognition (микрофон) за срички, думи, фрази
- ✅ 3-ниво оценяване (Bravo / Bien essayé / Réessaie)
- ✅ Системата говори на глас всичко (подкана + оценка + елемента)
- ✅ Alia е ПЪРВА навсякъде
- ✅ 3 секунди пауза преди оценка
- ✅ Voyelles: задача-базирано (намери буквата)
- ✅ Система за награди (Karumi + фрази + star burst анимация)
- ✅ Родителски кабинет (dashboard, progress, settings)
- ✅ AI резюме на прогреса (Claude API)
- ✅ AI генериране на нови изречения (Claude API)
- ✅ Парола за /parent (`maman`)
- ✅ Deploy на Hostinger VPS (Ubuntu 24.04)
- ✅ SSL сертификат (Let's Encrypt)
- ✅ Open Graph meta тагове (WhatsApp preview)
- ✅ Светла тема "книга" с Karumi плаваща анимация
- ✅ Двуколонно меню на home екрана
- ✅ Maman бутон в менюто

**Ключови архитектурни решения:**
- Anthropic SDK → заменен с директен HTTP (`requests`) заради проблем с PyPI на сървъра
- Flask 2.0.3 + Python 3.12 (не Python 3.6 от shared хостинг)
- VPS вместо shared хостинг (shared нямаше Python поддръжка в hPanel)
- Vanilla JS без framework — лесно за поддръжка

---

## РАЗДЕЛ 18. СОБСТВЕНОСТ И КОНТРОЛ

| Ресурс | Owner | Достъп |
|--------|-------|--------|
| Домейн `alia-adri.com` | Miglena Angelova | Hostinger акаунт |
| VPS (72.61.21.43) | Miglena Angelova | SSH root + Hostinger hPanel |
| GitHub репо | miglenaangel-glitch | GitHub акаунт |
| Anthropic API ключ | Miglena Angelova | console.anthropic.com |
| SSL сертификат | auto (Let's Encrypt) | на сървъра |
| MySQL база | root на VPS | SSH + mysql CLI |

---

## РАЗДЕЛ 19. ПРИЕМНО-ПРЕДАВАТЕЛЕН CHECKLIST

При предаване към нов разработчик:

- [ ] GitHub достъп до `miglenaangel-glitch/lire-avec-alia`
- [ ] SSH достъп до `root@72.61.21.43`
- [ ] Hostinger акаунт (VPS + домейн)
- [ ] Anthropic API ключ
- [ ] .env файлът (не е в git — трябва ръчно)
- [ ] Прочитане на CLAUDE.md и BIBLE.md
- [ ] Тестване на deploy процедурата

---

*Библията е жив документ. Всяка съществена промяна по проекта → обновяване тук.*
