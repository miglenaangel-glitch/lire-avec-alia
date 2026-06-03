# МЕТОДОЛОГИЯ — LES NOMBRES (ЧИСЛИТЕЛНИТЕ)
## Сектор "Écriture des nombres" — Lire avec Alia
**Версия:** 1.0  
**Дата:** 2026-06-03  
**Статус:** Готов за имплементация от КК

---

## ЗАЩО ЧИСЛИТЕЛНИТЕ СА ОТДЕЛЕН СЕКТОР

Числителните на френски са **уникална орфографска система** — не следват общите правила на езика. Те са:

1. **Фонетично непрозрачни** — `deux` се чете [dø], не [dœks]. `vingt` финалното `t` се произнася само в `vingt et un`, не в `vingt-deux`.
2. **Морфологично нестандартни** — `quatre-vingt` (4×20), `soixante-dix` (60+10) — логика, която не съществува в повечето езици.
3. **Изключително чести в реалния живот** — Alia ги среща всеки ден: цени, часове, адреси, оценки, дати.
4. **Специфичен проблем при кохлеарен имплант** — [ɛ̃] в `vingt`, [wɛ̃] в `point`, [swa] в `soixante` — звукове, трудни за имплант.

**Педагогическото решение:** Числителните се учат като **зрителни цели** (визуален образ на думата) + **звуков анкор** (произношение) + **числова котва** (цифрата). Три канала едновременно — класически Apili.

---

## ЦВЕТОВА СИСТЕМА (абсолютна — не се нарушава)

```
Съгласни → #1a3a6b (тъмносин)
Гласни   → #c0392b (тъмночервен)
Неми     → #b0a090 (светлосив)
```

**Специфика за числителните:**
- Финалните неми букви са ОСОБЕНО важни тук: `vingt` → `t` = сиво
- Свързването (liaison) се маркира визуално: `vingt et un` → `t` = оранжево (специален маркер за liaison)
- Дефисът в `vingt-deux` се показва в неутрален сив цвят

**Нова категория: LIAISON маркер**
```
Liaison → #e67e22 (оранжево) — буква, която е нема сама, но се произнася при liaison
```

---

## СТРУКТУРА НА СЕКТОРА — 5 НИВА

```
НИВО N1 — 0 до 10        (les unités)
НИВО N2 — 11 до 20       (les irréguliers)
НИВО N3 — 21 до 69       (les dizaines régulières)
НИВО N4 — 70 до 99       (la logique belge/suisse vs française)
НИВО N5 — 100 до 1000+   (les centaines et milliers)
```

---

## НИВО N1 — LES UNITÉS (0–10)

### Педагогическа цел
Alia свързва **цифрата** ↔ **написаната дума** ↔ **произношението**. Фундаментът. Без грешка тук — всичко по-нагоре се гради върху това.

### Специфика за имплант
- `un` [ɛ̃] — назален звук, труден. Приемаме [œ̃] и [ɛ̃] еднакво.
- `deux` [dø] — специфичен звук. Свързваме с Ниво 15 на основния курс (eu/œu).
- `cinq` [sɛ̃k] — финалното `q` СЕ ПРОИЗНАСЯ. Маркираме в синьо, не в сиво.
- `six` [sis] — финалното `x` = [s]. Свързваме с Ниво 27 (x = cs/gz/s).
- `huit` [ɥit] — `h` е нямо, `t` СЕ ПРОИЗНАСЯ в изолация.
- `dix` [dis] — финалното `x` = [s].

### Съдържание

| Цифра | Дума | Произношение | Цветова разбивка |
|-------|------|-------------|-----------------|
| 0 | **z**é**r**o | [zero] | z=синьо, é=червено, r=синьо, o=червено |
| 1 | **un** | [ɛ̃] | u=червено, n=сиво |
| 2 | **d**e**ux** | [dø] | d=синьо, eu=червено, x=сиво |
| 3 | **tr**o**is** | [tʀwa] | t=синьо, r=синьо, o=червено, i=сиво, s=сиво |
| 4 | **qu**a**t**r**e** | [katʀ] | qu=синьо, a=червено, t=синьо, r=синьо, e=сиво |
| 5 | **c**i**nq** | [sɛ̃k] | c=синьо, in=червено, q=**СИНЬО** ← произнася се! |
| 6 | **s**i**x** | [sis] | s=синьо, i=червено, x=синьо ← [s] |
| 7 | **s**e**pt** | [sɛt] | s=синьо, e=червено, p=сиво, t=**СИНЬО** ← произнася се! |
| 8 | **h**u**it** | [ɥit] | h=сиво, u=червено, i=червено, t=**СИНЬО** ← произнася се! |
| 9 | **n**eu**f** | [nœf] | n=синьо, eu=червено, f=**СИНЬО** ← произнася се! |
| 10 | **d**i**x** | [dis] | d=синьо, i=червено, x=синьо ← [s] |

### ⚠️ Педагогически коментар: финалните съгласни
`cinq`, `sept`, `huit`, `neuf`, `dix`, `six` — всичките произнасят финала в изолация. Това е контра-интуитивно за Alia, която е научила "финалните са неми". Правило визуално: **ако е в синьо — произнасяш. Ако е в сиво — мълчиш.**

### Упражнения N1

**N1-EX1: `number_match`** *(ново упражнение)*
- На екрана: цифрата (голяма, центрирана) + 4 думи в Apili цветове
- Alia натиска правилната дума
- При натискане: системата произнася думата
- Обратен режим: думата голяма → натиска цифрата

**N1-EX2: `tap_to_hear`** (стандартен)
- Думата с цветове → Alia натиска → чува произношението
- 3 пъти всяка дума преди да се счита за усвоена

**N1-EX3: `spell_the_number`** *(ново упражнение)*
- Цифрата на екрана + разбъркани букви отдолу
- Alia наредя буквите в правилен ред
- Буквите се оцветяват при поставяне (синьо/червено/сиво)
- При успех: цифрата "скача" + произношението + конфети

**N1-EX4: `dictée_chiffres`** *(ново упражнение — само с микрофон)*
- Системата произнася цифра → Alia пише думата
- Или: Alia произнася цифра → системата проверява
- Протокол "Alia е ПЪРВА": тя пише, после чува потвърждение

### Критерий за напредване към N2
- 10/10 думи разпознати (number_match) ≥ 3 пъти
- 8/10 правилно изписани при spell_the_number
- `cinq`, `sept`, `huit`, `neuf` с правилно произнесен финал ≥ 4/5

---

## НИВО N2 — LES IRRÉGULIERS (11–20)

### Педагогическа цел
Числата 11–16 са **неправилни** (не следват никаква логика — само запаметяване). 17–19 следват логика (10+7, 10+8, 10+9). 20 е особен случай.

### Специфика за имплант
- `onze` [õz] — назален + z
- `douze` [duz] — ou = Ниво 10 от основния курс
- `treize` [tʀɛz] — ei = особена графема
- `quatorze` [katɔʀz] — дълга дума, 3 срички
- `quinze` [kɛ̃z] — in + z финал
- `seize` [sɛz] — ei = [ɛ]
- `vingt` [vɛ̃] — финалното `t` е НЯМО в изолация, но се произнася при liaison!

### Съдържание

| Число | Дума | Произношение | Бележка |
|-------|------|-------------|---------|
| 11 | **onz**e | [õz] | on = назален; z финал |
| 12 | **d**o**uz**e | [duz] | ou + z финал |
| 13 | **tr**ei**z**e | [tʀɛz] | ei = [ɛ]; z финал |
| 14 | **qu**a**t**o**rz**e | [katɔʀz] | 3 срички! |
| 15 | **qu**i**nz**e | [kɛ̃z] | in + z финал |
| 16 | **s**ei**z**e | [sɛz] | ei = [ɛ]; z финал |
| 17 | **d**i**x-s**e**pt** | [disɛt] | dix + sept — t произнася се! |
| 18 | **d**i**x-h**u**it** | [dizɥit] | liaison! x=[z] пред h aspiré |
| 19 | **d**i**x-n**eu**f** | [diznœf] | liaison! x=[z] |
| 20 | **v**i**ng**t | [vɛ̃] | t = НЯМО в изолация |

### ⚠️ Педагогически коментар: LIAISON при 17, 18, 19
`dix-sept`, `dix-huit`, `dix-neuf` — `x` се произнася [s] или [z] при liaison. Визуално: `x` в оранжево = liaison маркер. Alia вижда: "тук `x` се събужда и произнася!"

### ⚠️ Педагогически коментар: VINGT — капанът
`vingt` в изолация: `t` = сиво (нямо).  
`vingt et un`: `t` = оранжево (liaison, произнася се!).  
Това е едно от най-честите грешки. Показваме двете форми едновременно.

### Упражнения N2

**N2-EX1: `number_match`** — същото като N1, с числата 11–20

**N2-EX2: `irregular_gallery`** *(ново упражнение)*
- 6 карти (11–16) с хумористична илюстрация за всяко
- Всяка карта = картинка + цифра + дума с Apili цветове
- Alia "обръща" картата → чува произношението + смешен звуков ефект
- Цел: картите са специални — неправилните числа нямат логика, затова получават собствена "галерия на странните"

**N2-EX3: `liaison_spotter`** *(ново упражнение)*
- Показва се изречение: "Il a dix-huit ans."
- Alia трябва да намери liaison-а (натиска буквата в оранжево)
- При правилен отговор: звуков ефект + произношение

**N2-EX4: `vingt_trainer`** *(ново упражнение)*
- Специален мини-модул САМО за `vingt`
- Два режима: изолация (t = нямо) vs liaison (t = произнася се)
- Alia чува двете → натиска правилния режим
- 5 последователни верни отговора = завършен

### Критерий за напредване към N3
- 16/20 числа правилно match-нати ≥ 3 пъти
- 11–16 "irregular gallery" завършена с ≥ 80%
- `vingt` liaison vs. изолация ≥ 4/5

---

## НИВО N3 — LES DIZAINES RÉGULIÈRES (21–69)

### Педагогическа цел
Alia научава **логиката на системата**: 21–69 следват правилото dizaine + unité. `trente-deux` = 30 + 2. Единственото изключение: `et` само при `...et un` (21, 31, 41, 51, 61).

### Специфика за имплант
- Дефисът е **задължителен** — визуализираме го ясно
- `et un` — `et` без дефис, с дефис между dizaine и unité
- Многосричните думи (trente-quatre = 3 срички + 2 срички = 5 срички) — обработката е по-бавна при имплант. Делим с | : `tren|te-qua|tre`

### Десетиците

| Число | Дума | Произношение |
|-------|------|-------------|
| 20 | **v**i**ng**t | [vɛ̃] |
| 30 | **tr**e**nte** | [tʀɑ̃t] |
| 40 | **qu**a**r**a**nte** | [kaʀɑ̃t] |
| 50 | **c**i**nqu**a**nte** | [sɛ̃kɑ̃t] |
| 60 | **s**o**ix**a**nte** | [swasɑ̃t] |

### Правилото `et un`

```
21 = vingt et un       (et — без дефис!)
31 = trente et un
41 = quarante et un
51 = cinquante et un
61 = soixante et un

22 = vingt-deux        (дефис — без et!)
32 = trente-deux
```

### Визуален модел за разбивка

```
soixante - trois
   60    +   3

⬆ синьо/червено = основната дума
          ⬆ дефис = светлосив
              ⬆ единицата = отделна цветна блок-карта
```

### Упражнения N3

**N3-EX1: `dizaine_builder`** *(ново упражнение — ключово)*
- На екрана: цифра (напр. 47)
- Две зони: [ dizaine ] + [ - ] + [ unité ]
- Alia плъзга правилните карти в правилните зони
- При `...et un`: трета зона [ et ] се появява между dizaine и unité
- Апили стил: картите са с цветово кодирани букви

**N3-EX2: `defile_des_dizaines`** *(ново упражнение)*
- Анимирана "парада" на десетиците: 20, 30, 40, 50, 60 минават по екрана
- Alia натиска всяка → чува произношението
- Скоростта се увеличава при успех → gamification

**N3-EX3: `et_ou_tiret`** *(критично упражнение)*
- Показват се двойки: `21` vs `22`, `31` vs `32`...
- Alia избира: `et un` (без дефис) ИЛИ `dефис + unité`
- Визуален индикатор: зелено = правилно, червено = грешно + правилният вариант

**N3-EX4: `rapid_read_numbers`** (адаптация на стандартния rapid_read)
- Таблица от числа 21–69 в случаен ред
- Alia чете последователно → натиска → чува
- Хронометриране: прогресията се записва

### Критерий за напредване към N4
- Всички 10 десетици [20, 30...60 + основни комбинации] ≥ 8/10
- `et un` vs дефис: 0 грешки в 10 последователни примера
- 30 произволни числа 21–69: ≥ 25/30

---

## НИВО N4 — LA LOGIQUE COMPLEXE (70–99)

### Педагогическа цел
Това е **най-трудното ниво** — французската математическа логика е уникална в света:
- `soixante-dix` = 60+10 (не `septante` като в Белгия/Швейцария!)
- `quatre-vingts` = 4×20
- `quatre-vingt-dix` = 4×20+10

### ⚠️ ПЕДАГОГИЧЕСКИ ДЕЛИКАТЕН МОМЕНТ
Alia живее в Париж. Учим **само парижката норма**. Белгийско/швейцарско `septante`, `huitante`, `nonante` са посочени само като "забавен факт" — не се изискват, не се тестват.

### Специфика за имплант
`quatre-vingts` е 3-сричкова дума + сложна графема `ng`. Разбиваме: `qua|tre-ving|ts`. Финалното `s` в `quatre-vingts` е НЯМО в изолация, ПРОИЗНАСЯ СЕ при liaison (`quatre-vingts ans`).

### Съдържание

| Число | Дума | Логика | Бележка |
|-------|------|--------|---------|
| 70 | soixante-dix | 60+10 | — |
| 71 | soixante et onze | 60+11 | `et` без дефис! |
| 72 | soixante-douze | 60+12 | дефис |
| 73–79 | soixante-treize... | 60+13...19 | — |
| 80 | quatre-vingts | 4×20 | `s` финал — нямо! |
| 81 | quatre-vingt-un | 4×20+1 | БЕЗ `s` (81, 82...89) |
| 82–89 | quatre-vingt-deux... | — | БЕЗ `s`! |
| 90 | quatre-vingt-dix | 4×20+10 | — |
| 91 | quatre-vingt-onze | 4×20+11 | — |
| 99 | quatre-vingt-dix-neuf | 4×20+10+9 | 6 срички! |

### ⚠️ КАПАНЪТ: `quatre-vingts` vs `quatre-vingt-un`
`quatre-vingts` (80 в изолация) = с `s`
`quatre-vingt-un` (81) = БЕЗ `s`
Това е едно от най-честите грешки дори при носители на езика. Специален визуален маркер: `s` при `quatre-vingts` = ОЦВЕТЯВАНЕ в специален розов цвят + надпис "seulement quand il est seul!"

### Упражнения N4

**N4-EX1: `logique_decoder`** *(ново упражнение — геймификация)*
- Визуален интерфейс: "Помогни на Rémi да разгадае математическата формула!"
- На екрана: `60 + 12 = ?`
- Alia избира между: `soixante-douze` / `septante-deux` / `soixante-et-douze`
- Хумор: Rémi е объркан (илюстрация) — само Alia може да му помогне

**N4-EX2: `quatre_vingts_trap`** *(критично упражнение)*
- Специален модул САМО за `quatre-vingts` vs `quatre-vingt-...`
- Показва се число → Alia пише думата → системата проверява присъствието на `s`
- 10 последователни верни = завършен

**N4-EX3: `belgique_vs_france`** *(информационна карта + quiz)*
- Информационна карта: "En Belgique et en Suisse, ils disent 'septante' !"
- Малък quiz: Alia трябва да преведе `septante-deux` на "parisian French"
- Цел: разширяване на хоризонта + хумор + разбиране на контекст

**N4-EX4: `dictée_numbers_70_99`**
- Системата произнася числото (бавно, rate: 0.6) → Alia пише думата
- Проверка: автоматична + визуална разбивка на грешките

### Критерий за напредване към N5
- 70–79: ≥ 8/10
- 80–89: `s` правило ≥ 9/10 (без нито една грешка при `quatre-vingts`)
- 90–99: ≥ 7/10 (приемаме по-нисък праг — много дълги думи)

---

## НИВО N5 — LES CENTAINES ET MILLIERS (100–1 000 000)

### Педагогическа цел
Alia разбира системата за стотиците и хилядите. Употреба в реален живот: цени, години, телефонни номера, адреси.

### Специфика за имплант
При многосричните числа (`deux-cent-cinquante-trois`) обработката е значително по-тежка. Стратегия: разбиваме числото на **блокове** и показваме всеки блок отделно преди цялото.

### Съдържание

**Стотиците:**
```
100 = cent
200 = deux cents    ← s при кратно в изолация
201 = deux cent un  ← без s при следваща цифра!
300 = trois cents
1000 = mille        ← НИКОГА "milles" (за разлика от cent)
2000 = deux mille   ← без s!
```

**Правилото за `cent`:**
- `deux cents` (200) = с `s` ← изолация
- `deux cent trois` (203) = БЕЗ `s` ← следвано от цифра

**Правилото за `mille`:**
- `mille` никога не получава `s` (за разлика от `cent`)
- `deux mille`, `trois mille` — без `s`

**Години (употреба):**
```
1995 = mil neuf cent quatre-vingt-quinze
2003 = deux mille trois
2026 = deux mille vingt-six
```

### Упражнения N5

**N5-EX1: `price_reader`** *(real-life приложение)*
- Показва се "ценово табло" от магазин (илюстрация)
- Alia чете цените на глас (микрофон) или ги пише
- Реалистичен контекст: Rémi иска да купи нещо → Alia чете цената
- Хумор: Rémi избира много скъпи неща, Alia трябва да го спре

**N5-EX2: `year_builder`** *(ново упражнение)*
- Показва се година (напр. 1998, 2015, 2026)
- Alia строи думата блок по блок
- Специален фокус: годините около Alia (2011 = годината, в която е родена? — персонализация!)

**N5-EX3: `cent_ou_cents`** *(критично)*
- Аналог на `quatre_vingts_trap`
- Правилото за `s` при `cent` в 10 упражнения

**N5-EX4: `telephone_number`** *(real-life приложение)*
- Показва се телефонен номер (по 2 цифри — французски стил)
- `06 12 34 56 78` → "zéro six, douze, trente-quatre, cinquante-six, soixante-dix-huit"
- Alia чете на глас → микрофон проверява
- Хумор: "C'est le numéro de Rémi! Il a perdu son téléphone!"

### Критерий за завършен сектор
- 100–999: ≥ 80%
- `cent` правилото: ≥ 9/10
- `mille` правилото: ≥ 9/10
- `year_builder`: ≥ 4 години правилно

---

## ХУМОРИСТИЧНО СЪДЪРЖАНИЕ ЗА ВСИЧКИ НИВА

*(в стила на Apili — абсурдно, запомнящо се)*

```
N1:
"Rémi a mangé 9 chats. C'est 'neuf chats', Éva, pas 'deux poulets'."
"Éva a commandé 5 pizzas. Le livreur a dit: cinq pizzas? Et il a pleuré."
"Il y a 8 araignées dans le lit de Rémi. Huit. Il les a comptées."

N2:
"Rémi a 11 chaussettes mais 2 pieds. C'est onze chaussettes de trop, Rémi."
"Éva a attendu Rémi pendant 15 minutes. Quinze. Il était dans le frigo."
"Rémi a invité 20 girafes. Vingt girafes dans l'appartement. Maman était furieuse."

N3:
"Il y a 42 biscuits sur la table. Rémi en a mangé 41. Quarante et un. Il a laissé un pour Éva. Elle était touchée."
"Éva a compté 67 moutons pour s'endormir. Soixante-sept. Le 67ème avait une écharpe."

N4:
"Rémi a 80 problèmes. Quatre-vingts. Mais ce soir il en a 81. Quatre-vingt-un. Il a renversé le jus sur la maîtresse."
"L'école de Rémi a 99 règles. Quatre-vingt-dix-neuf. La règle numéro 99: ne pas mettre le chat dans le cartable."

N5:
"Le téléphone de Rémi a 1000 photos du chat. Mille photos. Éva en a supprimé 999. Il lui reste une. La plus moche."
"Maman a demandé à Rémi combien coûtait son nouveau jeu: deux cent cinquante euros. Elle a failli s'évanouir."
```

---

## ТЕХНИЧЕСКИ СПЕЦИФИКАЦИИ ЗА КК

### Нови компоненти за имплементация

```javascript
// 1. NumberDisplay — показва число с Apili цветове + liaison маркер
<NumberDisplay 
  word="vingt-et-un"
  liaisons={["t"]}         // оранжево
  silent={["t"]}           // за "vingt" в изолация = сиво
  rate={0.6}               // TTS скорост
/>

// 2. NumberCard — карта с цифра + дума + произношение
<NumberCard 
  digit={21}
  word="vingt et un"
  illustration="remi_count.png"
  humor="Rémi compte ses problèmes..."
/>

// 3. DizaineBuilder — drag & drop конструктор
<DizaineBuilder 
  target={47}
  availableParts={["quarante", "sept", "et", "-"]}
  showConnector={true}    // показва et/дефис зона
/>

// 4. TrapDetector — за quatre-vingts / cent правилото
<TrapDetector 
  ruleType="quatre-vingts"  // или "cent"
  number={80}
  expectedForm="quatre-vingts"  // с s
/>
```

### База данни — нова таблица

```sql
CREATE TABLE numbers_progress (
  id INT AUTO_INCREMENT PRIMARY KEY,
  level VARCHAR(10),           -- N1, N2, N3, N4, N5
  number_value INT,            -- 0-9999
  word_form VARCHAR(100),      -- "quatre-vingts"
  attempts INT DEFAULT 0,
  correct INT DEFAULT 0,
  last_error_type VARCHAR(50), -- "liaison", "s_rule", "et_vs_tiret"
  mastered BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Критерии за mastered (по ниво)

```javascript
const MASTERY_CRITERIA = {
  N1: { minCorrect: 3, minAccuracy: 0.90 },
  N2: { minCorrect: 3, minAccuracy: 0.80 },
  N3: { minCorrect: 5, minAccuracy: 0.80 },
  N4: { minCorrect: 5, minAccuracy: 0.80, 
        trapRule: { quatre_vingts: 0.90 } },  // по-висок праг за капана
  N5: { minCorrect: 3, minAccuracy: 0.75 },
};
```

### Speech Recognition — специфики

```javascript
// Числителните изискват специален речник за Web Speech API
const NUMBER_RECOGNITION_HINTS = [
  "zéro", "un", "deux", "trois", "quatre", "cinq",
  "six", "sept", "huit", "neuf", "dix",
  "onze", "douze", "treize", "quatorze", "quinze", "seize",
  "vingt", "trente", "quarante", "cinquante", "soixante",
  "soixante-dix", "quatre-vingts", "quatre-vingt-dix",
  "cent", "mille"
];

// grammer за по-добро разпознаване (ако браузърът поддържа)
const recognition = new SpeechRecognition();
recognition.lang = 'fr-FR';
```

### TTS произношение — проверени форми

```javascript
// ВНИМАНИЕ: speechSynthesis произнася правилно:
// "vingt" [vɛ̃] ✓
// "quatre-vingts" [katʀəvɛ̃] ✓
// НО: "soixante-dix" понякога се произнася грешно в някои гласове
// Тест задължителен преди deploy!
const testTTS = (word) => {
  const utterance = new SpeechSynthesisUtterance(word);
  utterance.lang = 'fr-FR';
  utterance.rate = 0.6;
  window.speechSynthesis.speak(utterance);
};
```

---

## РОДИТЕЛСКИ КАБИНЕТ — NUMBERS DASHBOARD

Нов раздел в `/parent` → **"Les nombres"**

```
📊 Прогрес по нива:
├── N1 (0–10):    ████████░░ 80%
├── N2 (11–20):   ██████░░░░ 60%  ← текущо ниво
├── N3 (21–69):   🔒 заключено
├── N4 (70–99):   🔒 заключено
└── N5 (100+):    🔒 заключено

⚠️ Трудности:
- "vingt" liaison: 3 грешки тази седмица
- "quatre-vingts" s-правило: 2 грешки
→ Совет за мама: "Упражнявайте устно: питайте Alia колко коства нещо!"
```

---

## ИНТЕГРАЦИЯ С ОСНОВНИЯ CURRICULUM

Секторът "Nombres" се **отключва постепенно**, свързан с нивата на основния курс:

```
N1 (0–10)     → отключва се след Ниво 3 (mots_simples)
N2 (11–20)    → отключва се след Ниво 10 (ou) — защото "douze" изисква ou
N3 (21–69)    → отключва се след Ниво 12 (an/en) — "trente" = [tʀɑ̃t]
N4 (70–99)    → отключва се след Ниво 13 (in/ain) — "vingt" = [vɛ̃]
N5 (100+)     → отключва се след Ниво 15 (eu/œu) — "deux cents" = [dø sɑ̃]
```

---

## ФАЙЛОВА СТРУКТУРА (предложение за КК)

```
/static/numbers/
├── illustrations/
│   ├── remi_count_1.png      ← Rémi брои нещо смешно
│   ├── remi_count_2.png
│   └── eva_price.png         ← Ева чете цена
├── data/
│   └── numbers_fr.json       ← всички форми с метаданни
templates/
├── numbers/
│   ├── index.html            ← меню на сектора
│   ├── level_n1.html
│   ├── level_n2.html
│   ├── level_n3.html
│   ├── level_n4.html
│   └── level_n5.html
routes/
└── numbers.py                ← Flask blueprint
```

---

## БЕЛЕЖКА ЗА КК — ПРИОРИТЕТ НА ИМПЛЕМЕНТАЦИЯ

```
🔴 Задължително за MVP на сектора:
  - N1 пълен (0–10) + number_match + tap_to_hear + spell_the_number
  - N2 irregular_gallery (11–16 са ключови — напълно неправилни)
  - vingt_trainer (liaison капанът)

🟡 Важно — втора итерация:
  - N3 dizaine_builder (drag & drop)
  - N4 quatre_vingts_trap
  - price_reader (real-life контекст)

🟢 Полезно — трета итерация:
  - N5 year_builder
  - telephone_number
  - belgique_vs_france (информационна карта)
```

---

*NOMBRES_METHODOLOGY.md — Lire avec Alia — v1.0 — 2026-06-03*  
*Разработено по метода Apili, адаптирано за кохлеарен имплант*  
*Алия, ти можеш! 🌟*
