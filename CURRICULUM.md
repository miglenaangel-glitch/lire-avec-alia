# CURRICULUM.md — Lire avec Alia
## Методологична прогресия по метода Apili

**Версия:** 1.0  
**Дата:** 2026-06-03  
**Автор:** Методологичен екип на проекта  
**Статус:** Готов за имплементация

---

## Как се чете този документ

Всяко ниво съдържа:
- **Педагогическа цел** — какво усвоява Alia
- **Специфики за имплант** — адаптации спрямо кохлеарния имплант
- **Съдържание** — точните букви, срички, думи, изречения
- **Упражнения** — типовете от Exercise Engine
- **Критерий за напредване** — кога се преминава към следващото ниво
- **Примерни хумористични изречения** — в стила на Apili

**Цветова система (абсолютна — не се нарушава никога):**
```
Съгласни → #1a3a6b (тъмносин)
Гласни   → #c0392b (тъмночервен)
Неми     → #b0a090 (светлосив)
```

---

## ПРИНЦИПИ НА АДАПТАЦИЯ ЗА КОХЛЕАРЕН ИМПЛАНТ

Alia чува добре, но обработката на фонеми е по-бавна и различна от тази при чуващи деца. Това изисква специфични адаптации:

**1. Повторението е приятел, не наказание.**
Всяка нова графема се среща минимум 15–20 пъти преди да се счете за усвоена. Системата не казва "вече го знаеш" — тя просто го среща по-рядко.

**2. Визуалното предшества слуховото.**
Преди да чуе звука, Alia вижда буквата с цвета си. Зрителният канал е по-надежден при имплант — използваме го като основа.

**3. Артикулацията е опора.**
"Les bouches" (изображенията на устата от учебника) са задължителни за всяка нова графема. Alia може да "прочете" устните дори когато слуховото е неясно.

**4. Паузата след произнасяне е 1 секунда (не 3).**
При кохлеарен имплант обработката е реалновременна — дългата пауза дезориентира. 1 секунда е достатъчна.

**5. Темпото е регулируемо.**
Web Speech API на `rate: 0.6` е задължително за новото съдържание. За упражнения за скорост (lecture rapide) — `rate: 0.8`.

**6. Никога не се смесват нов звук и нова графема едновременно.**
Ако звукът е нов → графемата трябва да е позната (и обратно). Принципът "apprentissage sans erreur" е особено важен при имплант.

**7. Хуморът е терапевтичен.**
При 13-годишна Alia смехът е и социална нужда, и неврологичен инструмент. Абсурдните изречения са задължителни — те правят паметовия отпечатък по-дълбок.

---

## КАРТА НА ПРОГРЕСИЯТА (пълен преглед)

```
БЛОК 1 — ОСНОВИ (Нива 0–4) ← вече изградено в MVP
├── Ниво 0: Гласни (voyelles)
├── Ниво 1: Първи съгласни — f, s, ch, l, m, r
├── Ниво 2: Бързо четене — таблица с срички
├── Ниво 3: Първи думи (с неми букви)
└── Ниво 4: Първи изречения (Rémi & Éva)

БЛОК 2 — РАЗШИРЕНИЕ НА СЪГЛАСНИТЕ (Нива 5–9)
├── Ниво 5: j, v, p, t, b
├── Ниво 6: d, n, c/k/qu, z, g (твърдо)
├── Ниво 7: Гласна + съгласна (типове VС: ar, al, or, er...)
├── Ниво 8: h (нямо) + h aspiré
└── Ниво 9: Затвърдяване — думи и изречения с всички съгласни

БЛОК 3 — СЛОЖНИ ГРАФЕМИ (Нива 10–16)
├── Ниво 10: ou [u]
├── Ниво 11: on/om [õ]
├── Ниво 12: an/am/en/em [ã]
├── Ниво 13: in/ain/ein [ɛ̃] + oin [wɛ̃]
├── Ниво 14: au/eau = o
├── Ниво 15: eu/œu [ø/œ]
└── Ниво 16: ph = f

БЛОК 4 — ФИНАЛНИ ГРАФЕМИ (Нива 17–21)
├── Ниво 17: -et = -è / -er = -é / -ez = -é
├── Ниво 18: -ette / -er- = ère / -enne / -esse / -erre
├── Ниво 19: ec/es/ef/el/er/ep (финални съгласни, произнасяни)
├── Ниво 20: gn [ɲ] + il y a (locution)
└── Ниво 21: elle / -ille / -ien

БЛОК 5 — КОНТЕКСТУАЛНИ ПРАВИЛА (Нива 22–26)
├── Ниво 22: ce/ci = se/si + ça/ço/çu
├── Ниво 23: gi/ge = ji/je + gea/geo
├── Ниво 24: ti = si (в -tion, -tiel)
├── Ниво 25: s intervocalique = z
└── Ниво 26: -ail/-aille + -eil/-eille + -ouil/-ouille + -euil/-euille

БЛОК 6 — ФИНАЛИЗАЦИЯ (Ниво 27)
└── Ниво 27: y + x (= cs или gz)
```

---

## БЛОК 1 — ОСНОВИ
### (Нива 0–4, вече изградени — документирани за референция)

### Ниво 0 — Les voyelles

**Педагогическа цел:** Alia разпознава и произнася 7-те основни гласни. Усвоява жеста за всяка.

**Съдържание:**
| Буква | Звук | Жест | Пример-дума |
|-------|------|------|-------------|
| a | [a] | Разтваряш ръцете настрани | ami |
| é | [e] | Вдигаш пръст | été |
| i | [i] | Показваш с пръст и се смееш | île |
| o | [o] | Слагаш ръка пред устата | oiseau |
| u | [y] | Ръцете като волан | lune |
| e | [ə] | Показалец под устата | le |
| y | [i] | Като "i" + усмивка | yeux |

**Упражнения:** `tap_to_hear` — задача "Appuie sur le [буква]!"  
**Критерий:** 5/5 правилни разпознавания за всяка гласна.

---

### Ниво 1 — Consonnes 1 (f, s, ch, l, m, r)

**Педагогическа цел:** Сливане на съгласна + гласна (La combinatoire). Alia разбира механизма на сричката.

**Съдържание — срички:**
```
fa fé fi fo fu
sa sé si so su
cha ché chi cho chu
la lé li lo lu
ma mé mi mo mu
ra ré ri ro ru
```

**Специфика за имплант:** Звукът "r" [ʀ] е труден при имплант (гърлен). Използвай изображението на устата. Ако Alia произнася [r] като [l] — приемай и продължавай, не корегирай насилствено.

**Упражнения:** `slide_to_merge` (основният Apili механизъм)  
**Критерий:** Всяка сричка ≥ 4/5 правилни.

---

### Ниво 2 — Lecture rapide (таблица)

**Педагогическа цел:** Автоматизация — четенето да стане рефлекс, не мислене.

**Таблица (примерна, разбърква се при всяко зареждане):**
```
la  lu  li  lé  lo
mo  ma  mu  mi  mé
ré  ro  ri  ra  ru
fa  si  cho lu  mé
ro  mé  li  so  chu
ra  fé  su  cho ri
fé  la  mo  mé  li
so  chu ra  fé  mo
```

**Специфика за имплант:** Темпо rate: 0.8. Целта е Alia да чете без да се замисля — автоматизацията е особено важна при имплант, където фонологичната обработка изисква повече ресурс.

**Упражнения:** `rapid_read`  
**Критерий:** Цяла таблица (40 срички) без грешка.

---

### Ниво 3 — Mots simples (48 думи)

**Съдържание — пълен списък:**
```
chat    ami     lave    rame    joli    vache
lama    vélo    mari    rémi    fume    mamie
mur     lire    rue     mare    vis     rire
avalé   fil     lime    mal     surimi  folie
cheval  lavé    olive   safari  carafe  famille
camion  soleil  merci   farine  virage  couloir
cheminée musée  marché  village rivière château
voiture fumée   liberté miracle chimie  salami
```

**Правило за неми букви (визуално — без обяснение):**
- chat → **ch**=синьо, **a**=червено, **t**=сиво
- rue → **r**=синьо, **u**=червено, **e**=сиво

**Упражнения:** `word_tap`  
**Критерий:** 40/48 думи ≥ 80% точност при произнасяне.

---

### Ниво 4 — Phrases (40 изречения с Rémi & Éva)

**Педагогическа цел:** Четене на цялостни изречения. Разбиране на смисъла.

**Пълен списък:**
```
Rémi lave la vache.
Éva va lire.
Rémi a sali le lit.
Rémi a volé le rat.
Rémi a vomi par la fenêtre.
Éva dort sur un sac de patates.
Rémi a mordu la patte du chat.
Éva a mis du sel dans le café de Rémi.
Le chat de Rémi a avalé le vélo de Éva.
Rémi a mis la vache sur le canapé.
Éva a lire une fiche sur les lamas.
Rémi a fumé une carafe de limonade.
Le lama de Éva a sali la robe de la maîtresse.
Rémi a ri si fort qu'il a vomi sur le chat.
Éva a volé le surimi de Rémi et elle a fui.
Rémi a mis le chat dans le lavabo.
La vache a lu le livre de Rémi.
Éva a salé le vélo de Rémi par erreur.
Rémi a avalé une lime par accident.
Le chat a ri de Rémi.
La maîtresse a vu Rémi manger la vache.
Éva chante si fort que le chat s'est enfui.
Rémi a colorié la vache en vert.
Le chat de Éva a mis du sel partout.
Rémi a choisi de dormir sur le lama.
La vache a volé le vélo de Rémi et elle a filé.
Éva a mis le lama dans le réfrigérateur.
Rémi a rit jusqu'à vomir sur la maîtresse.
Le chat a sali le livre de Rémi avec les pattes.
Éva a fait la course avec une vache et elle a perdu.
Rémi a mis le chat dans le sac de Éva.
La vache a mordu le livre de la maîtresse.
Rémi a avalé le stylo de Éva.
Éva a ri si fort qu'elle a réveillé le voisin.
Rémi a mis le lama sur le toit de la voiture.
Le chat a lu le livre de Rémi et il a ri.
Éva a mis la vache dans le sac à dos de Rémi.
Rémi a salé le café du directeur.
La vache et le chat ont ri de Rémi.
Éva a mis le surimi dans les chaussures de Rémi.
```

**Упражнения:** `sentence_read`  
**Критерий:** 32/40 изречения произнесени с ≥ 80% точност.

---

## БЛОК 2 — РАЗШИРЕНИЕ НА СЪГЛАСНИТЕ

### Ниво 5 — Consonnes 2: j, v, p, t, b

**Педагогическа цел:** 5 нови съгласни. Alia вече знае механизма на сричката — сега го прилага автоматично.

**Специфика за имплант:**
- **[j]** (жур) — лесно за имплант, звучен, дълъг
- **[v]** — разграничаване от [f]: устните вибрират при [v], не при [f]. Изображението на устата е задължително
- **[p]** — взривна, трудна за имплант (кратка). Показвай движението на устните
- **[t]** — също взривна. Да се практикува с ta/ti/tu, не само изолирано
- **[b]** — разграничаване от [p]: [b] е звучно (гласните струни вибрират)

**Жестове:**
| Буква | Жест |
|-------|------|
| j | Правиш "зи-зи" с пръстите |
| v | Правиш знак "виктория" (V) |
| p | Духаш в шепата си |
| t | Почукваш с пръст по масата |
| b | Пляскаш с ръце |

**Срички:**
```
ja  jé  ji  jo  ju
va  vé  vi  vo  vu
pa  pé  pi  po  pu
ta  té  ti  to  tu
ba  bé  bi  bo  bu
```

**Думи (само с вече познати звукове + новите):**
```
jupe    jambe   jardin  jouet   joli
vélo    valise  verre   vitre   voile
papa    patte   poire   pile    puma
table   tapis   tigre   tube    toit
balle   bateau  bouche  bureau  bébé
```

**Таблица за бързо четене (нова — включва всичко до тук):**
```
ja  li  vo  tu  bé
pa  ri  ji  mu  so
ta  fa  bo  ché vi
bu  sa  pé  lo  ju
to  ma  bi  ra  pi
```

**Изречения (хумористични, в стила на Apili):**
```
Rémi a mis sa jupe sur la tête du chat.
Éva a volé le vélo de Rémi et elle l'a jeté dans la rivière.
Le bébé de Rémi a mordu la table.
Papa a mis le tigre dans le bain.
La jupe de Éva vole dans le jardin.
Rémi a bu la soupe du voisin par erreur.
Éva a jeté le tapis par la fenêtre.
Le chat a mis la balle dans la valise de Rémi.
Papa a trouvé un puma sous son lit.
Rémi a peint le bateau en rose avec les pattes du chat.
```

**Упражнения:** `slide_to_merge` → `rapid_read` → `word_tap` → `sentence_read`  
**Критерий:** Всяка нова сричка ≥ 4/5. Таблицата без грешка. 8/10 изречения.

---

### Ниво 6 — Consonnes 3: d, n, c/k/qu, z, g (твърдо)

**Педагогическа цел:** Финалните прости съгласни. Въвеждане на първото контекстуално правило: c/k/qu са един звук.

**Специфика за имплант:**
- **[d]** vs **[t]**: [d] е звучно. Използвай "вибрационното" правило — слагаш ръка на гърлото: при [d] вибрира, при [t] — не
- **[n]**: назален звук — при имплант може да звучи нечисто. Нормално
- **c/k/qu**: трите пишат един звук [k]. Важно педагогическо откритие — показва на Alia, че буквите са инструмент, не магия
- **[z]**: лесно — дълъг, звучен
- **g твърдо** (ga, go, gu): само в тези позиции! Меко g се учи по-късно

**Жестове:**
| Буква | Жест |
|-------|------|
| d | Барабаниш с пръсти (d-d-d) |
| n | Поставяш пръст на носа си |
| c/k/qu | Правиш знак ОК с ръка |
| z | Движиш ръката като змия |
| g | Свиваш юмрук |

**Срички:**
```
da  dé  di  do  du
na  né  ni  no  nu
ca  co  cu / ka  ki / que qui
za  zé  zi  zo  zu
ga  go  gu
```

**ВАЖНО за c/k/qu:**
- `ca` = [ka], `co` = [ko], `cu` = [ky]
- `ki` = [ki], `ké` = [ke]
- `que` = [kə], `qui` = [ki]
- Визуалното правило: **c** пред a/o/u → синьо; пред e/i → НЯМО (ще учим по-късно в Ниво 22)

**Думи:**
```
dame    dodo    dune    dent    droit
nuit    nappe   neige   nœud    niche
café    canard  coton   cube    cœur
zèbre   zéro    zone    zigzag  zoo
gâteau  garage  gorille gomme   guitare
kilo    karaté  képi    kangourou koala
```

**Изречения:**
```
Le canard de Rémi a mangé le gâteau du directeur.
Éva a mis le zèbre dans le garage.
Rémi a commandé un kilo de kangourous au café.
La dame du bureau a trouvé un gorille dans son café.
Éva a dessiné un koala sur la nappe du restaurant.
Rémi a mis du coton dans les oreilles du canard.
Le zèbre a fait du karaté dans le garage.
Éva a commandé un gâteau en forme de zèbre.
Le canard a volé le képi de Rémi et il a sauté dans le zoo.
Rémi a mis le gorille dans la guitare de Éva.
```

**Упражнения:** `slide_to_merge` → `rapid_read` → `word_tap` → `sentence_read`  
**Критерий:** Разграничава c/k/qu правилно ≥ 8/10 пъти. Таблицата без грешка.

---

### Ниво 7 — Syllabes VC (Voyelle + Consonne)

**Педагогическа цел:** Alia усвоява обратната сричка — гласна + съгласна. Сега може да чете думи с CVC структура.

**Специфика за имплант:** Обратните срички са по-трудни при имплант — затворената сричка има по-кратка продължителност. Повторението е удвоено спрямо CV сричките.

**Срички VC (нови):**
```
ar  er  ir  or  ur
al  el  il  ol  ul
an  en  in  on  un  (само C — назалите са в Блок 3)
am  em  im  om  um
af  ef  if  of
as  es  is  os  us
av  ev  iv  ov
ab  ob
ad  ed  id  od
ag  eg  og
```

**Думи CVC (затворена сричка):**
```
arc     art     arbre   armoire  article
sel     sel     selle   service  serpent
fil     film    filtre  village  kilomètre
port    porte   portail portable portrait
mur     muraille muscle  murmure  musique
bal     ballon  ballet  baleine  balance
gel     gelée   général général  gélatine
col     colle   collier colline  couloir
```

**Изречения:**
```
Rémi a mis l'arc de Éva dans l'armoire du directeur.
Le village de Rémi a un portail en forme de baleine.
Éva a trouvé un film sur les kangourous dans le sel.
Rémi a mis le ballon dans le portail et ça a explosé.
Le serpent de Éva a avalé le collier de la directrice.
Rémi a collé des gels de couleur sur le mur du couloir.
Éva a peint un article sur le musique du sel.
Le film de Rémi dure moins d'une minute et c'est nul.
Rémi a mis de la gelée dans les chaussures du directeur.
Éva a trouvé un ballon dans son armoire et elle a pleuré.
```

**Упражнения:** `slide_to_merge` (с VC) → `rapid_read` → `word_tap` → `sentence_read`  
**Критерий:** Срички VC ≥ 4/5. 8/10 думи. 8/10 изречения.

---

### Ниво 8 — Le H

**Педагогическа цел:** h нямо vs h aspiré. Визуалното правило: h = сиво (нямо) в повечето позиции.

**Правило (визуално — без обяснение):**
```
habit → h=СИВО, a=червено, b=синьо, i=червено, t=СИВО
héros → h=СИВО, é=червено, r=синьо, o=червено, s=СИВО
thé   → t=синьо, h=СИВО (= "t" + безмълвно h), é=червено
```

**Специфика за имплант:** h е невидимо за ухото — при имплант Alia може вече да го е усвоила слухово, без да знае правилото. Играем на "намери скритата буква" — хуморна игра.

**Думи с h нямо:**
```
hé      ha      hi      ho      hu
hamac   hé      habitat habit   huile
haricot homme   hache   hameau  hibou
héros   histoire hiver   hôtel   honnête
rhume   rhinocéros
```

**Думи с th (= t):**
```
thé     théâtre  thermomètre  théorie  thym
```

**Изречения:**
```
Rémi a mis le hibou dans le hamac de Éva.
L'homme a fait trop d'huile dans la salade, il crie hi-han.
Éva a vu un homme qui coupait des haricots à l'aide d'une hache.
Le héros de l'histoire habite dans un hôtel en forme de hamac.
Rémi a commandé un rhinocéros au restaurant de l'hôtel.
Le hibou a bu tout le thé du directeur en une nuit.
Éva a mis le hamac dans l'histoire de Rémi.
Rémi a peint un héros avec un haricot géant.
```

**Упражнения:** `tap_to_hear` (разпознай h) → `word_tap` → `sentence_read`  
**Критерий:** h правилно оцветено ≥ 9/10 пъти. 7/8 изречения.

---

### Ниво 9 — Затвърдяване: Всички прости съгласни

**Педагогическа цел:** Alia може да чете всяка дума, съставена само от прости графеми. Това е голям момент — отбелязва се!

**Таблица за бързо четене (финална за Блок 2):**
```
ja  li  vo  tu  bé  do  na  ké  zi  ga
pa  ri  ji  mu  so  ni  da  fo  bi  gu
ta  fa  bo  ché vi  za  no  pi  ro  co
bu  sa  pé  lo  ju  go  di  vu  ra  né
to  ma  bi  ra  pi  du  ta  ki  zo  la

bar  sol  fil  car  mis  bol  dur  val  sir  nor
```

**Думи за финален тест (50 думи — всичко до тук):**
```
jambe    voiture   pluie    tableau   bureau
danger   nuage     qualité   zèbre    garage
dame     nuit      café      zéro     gâteau
girafe   jardin    vélo      piano    tapis
bonjour  dragon    caraffe   jungle   koala
hibou    hamac     haricot   thé      histoire
armoire  village   portail   ballon   serpent
collier  couloir   musique   article  service
kilomètre baleine  gelée     musée    général
marché   château   rivière   liberté  miracle
```

**Изречения (финални за Блок 2 — по-сложни):**
```
Le zèbre de Rémi a mangé le tableau du directeur au bureau.
Éva a mis le dragon dans la voiture et ça a pris feu.
Le hibou du zoo a volé la valise de la dame dans le jardin.
Rémi a commande une girafe au restaurant et il l'a mis dans sa chambre.
Le koala de Éva habite dans le garage depuis le mois de janvier.
Rémi a dessiné un tableau avec du café et une brosse à dents.
La baleine a fait du vélo dans le couloir du musée.
Éva a mis un kilomètre de collier autour du cou du chat.
Le château de Rémi est gardé par un koala et un zèbre en pyjama.
Rémi a trouvé un miracle dans le village: le café était gratuit.
```

**Финална награда при завършен Блок 2:** Специална анимация + нова фраза от Karumi: *"Alia, tu peux lire tous les sons simples ! C'est INCROYABLE !"*

**Критерий за преминаване към Блок 3:** 45/50 думи ≥ 80% точност + 8/10 финални изречения.

---

## БЛОК 3 — СЛОЖНИ ГРАФЕМИ

> **Педагогически принцип за целия Блок 3:**
> Всяка нова графема се въвежда САМО с думи, в които всичко друго е познато.
> "ou" се въвежда с думи като "chou", "roue", "mouton" — без нови съгласни.
> Никога не се смесват две нови неща в един урок.

---

### Ниво 10 — OU [u]

**Педагогическа цел:** Двойката ou = звукът [u], различен от u = [y]. Това е едно от най-честите объркания при четене на френски.

**Цветово правило:**
```
ou → o=синьо + u=СИВО (=двете заедно = един звук [u])
```
*Двете букви се подчертават заедно с обща линия отдолу.*

**Специфика за имплант:** [u] (ou) и [y] (u) са много близки звуци — при имплант Alia може да ги бърка. Упражнение за разграничаване: "ou" като "уу" в "пу" / "у" като "ю" на български.

**Срички:**
```
chou   rou   mou   sou   vou   lou   fou   pou   tou   bou
choua  roue  moue  soue  voue  loue  foue  poue  tour  bour
```

**Думи:**
```
chou    roue    mouton  poulet  tourteau
coucou  bijoux  genou   hibou   caillou
pouce   bouche  douche  louche  touche
fourmi  journal bonjour couleur toujours
cousine pouvoir vouloir couloir poumon
mouche  louche  douche  couche  souche
```

**Изречения:**
```
Rémi a mis le chou dans la douche et ça sent partout.
Le mouton de Éva a avalé la roue du vélo de Rémi.
Rémi a trouvé un coucou dans sa chaussure du mardi.
Éva a mis les bijoux du directeur dans la bouche du mouton.
Le hibou de Rémi lit le journal tous les jours sur le genou.
Rémi a commandé un poulet qui fait coucou au restaurant.
La mouche a fait du tourteau dans la douche de Éva.
Éva a dit bonjour au mouton qui dormait sur le couloir.
Le caillou de Rémi a avalé la fourmi et il était choqué.
Rémi a mis le chou dans son cartable pour manger au cours.
```

**Упражнения:** `slide_to_merge` (ou + consonnes) → `rapid_read` → `word_tap` → `sentence_read`  
**Критерий:** ou произнесено правилно (не като u) ≥ 9/10.

---

### Ниво 11 — ON/OM [õ]

**Педагогическа цел:** Назален звук [õ]. Alia научава, че "n" и "m" след "o" не се произнасят отделно — те "назализират" гласната.

**Цветово правило:**
```
on → o=червено + n=СИВО (= заедно = [õ])
om → o=червено + m=СИВО (= пред b/p = [õ])
```

**Специфика за имплант:** Назалните звуци са особено трудни при кохлеарен имплант — вибрациите са насочени към носната кухина и резонансът е различен. Не изискваме перфектна назализация — приемаме [o+n] и [õ] еднакво. Важното е да РАЗПОЗНАВА знака, не да назализира идеално.

**Срички:**
```
bon  son  mon  ton  don  ron  lon  von  pon  con
bomb sont mont tond donc ronde londe vonde
```

**Думи:**
```
bon     son     maison  bonbon  garçon
mouton  ballon  melon   citron  cochon
pomme   bombe   nombre  ombre   trombone
fond    monde   ronde   blonde  seconde
montagne fontaine  bonheur  consonne  jonquille
poisson  saison   boisson  maison   raison
```

**Изречения:**
```
Le cochon de Rémi a mangé tous les bonbons du garçon.
Éva a mis le citron dans le ballon et ça a explosé.
Rémi a trouvé un mouton dans la maison de sa voisine.
Le garçon a mis une bombe de citron dans la fontaine.
Éva a commandé un melon avec du poisson au restaurant.
Rémi a fait une chanson sur le cochon qui mange du melon.
Le bonbon de Éva est tombé dans le fond de la fontaine.
Rémi a mis du citron dans la boisson de son cochon.
La montagne de Rémi est en forme de cochon rose et c'est sa fierté.
Éva a dessiné un trombone sur le monde entier avec un ballon.
```

**Критерий:** on/om = [õ] ≥ 9/10 разпознавания.

---

### Ниво 12 — AN/AM/EN/EM [ã]

**Педагогическа цел:** Вторият назален звук [ã]. Alia разбира, че an/am/en/em са ЕДИН звук.

**Цветово правило:**
```
an → a=червено + n=СИВО (= [ã])
am → a=червено + m=СИВО (= [ã] пред b/p)
en → e=червено + n=СИВО (= [ã])
em → e=червено + m=СИВО (= [ã] пред b/p)
```

**Специфика за имплант:** Разграничаване [ã] vs [õ] е трудно при имплант. Правим специално упражнение: "an se tient debout [a-boca-aberta], on est rond comme un ballon [o-уста-кръгли]". Визуалният образ помага.

**Срички:**
```
an  am  en  em  ant ent  ans ens
pan  man  fan  ran  lan  van  tan  ban
pend mend fend rend lend vend tend bend
```

**Думи:**
```
enfant  parents  pendant  semaine  maintenant
maman   marchand  roman    commande  exemple
temps   ensemble  ventre   septembre  novembre
champ   chambre   chanter  champion  chocolat
banque  danger    manger   ranger    partager
orange  étrange   blanc    grand     printemps
```

**Изречения:**
```
Les parents de Rémi ont mangé l'enfant du roman.
Éva a attendu pendant toute la semaine que le chat mange.
Rémi a chanté en novembre dans le champ des champions.
Maman a commande un chameau en exemple pour les enfants.
Éva et Rémi ensemble ont mangé l'orange du danger.
Le marchand a vendu du temps à Rémi pour ranger sa chambre.
Rémi a mis le printemps dans une banque pour le garder.
Les enfants de septembre ont chanté pour les manchots.
Éva a trouvé un blanc bizarre dans la commande de Rémi.
La chambre de Rémi sentait l'orange, le champ et le danger.
```

**Критерий:** an/am/en/em = [ã] ≥ 9/10. Разграничаване от [õ] ≥ 8/10.

---

### Ниво 13 — IN/AIN/EIN [ɛ̃] + OIN [wɛ̃]

**Педагогическа цел:** Третият назален звук. in/ain/ein са три правописни форми на ЕДИН звук.

**Цветово правило:**
```
in  → i=червено + n=СИВО (= [ɛ̃])
ain → a=червено + i=СИВО + n=СИВО (= [ɛ̃])  [ai = двугласна → частично правило]
ein → e=червено + i=СИВО + n=СИВО (= [ɛ̃])
oin → o=червено + i=СИВО + n=СИВО (= [wɛ̃])
```

**Думи:**
```
main    pain    train   bain    gain
lapin   cousin  dessin  jardin  moulin
peinture  ceindre  reinventer  reine  teindre
loin    coin    poing   point   besoin
```

**Изречения:**
```
Rémi a mis le lapin dans le bain et il a crié au loin.
Éva a peint le cousin de Rémi en couleur de pain.
Le train du jardin a raté le coin de la peinture.
Rémi a besoin d'un lapin pour finir son dessin.
La reine a mis le poing dans le gâteau du moulin.
Éva a dessiné un lapin sur le train avec de la peinture de cerise.
Rémi a trouvé un point dans le jardin et il était ravi.
Le cousin de Éva habite loin, au coin d'un moulin bizarre.
Le lapin a fait la cuisine du pain en chantant au bain.
Éva a mis les peintures dans le besoin de Rémi.
```

**Критерий:** in/ain/ein/oin правилно произнесени ≥ 8/10.

---

### Ниво 14 — AU/EAU = O [o]

**Педагогическа цел:** au и eau са два правописни начина да се напише [o]. Нямат нова фонетика — само ортографично правило.

**Цветово правило:**
```
au  → a=червено + u=СИВО (= [o])
eau → e=СИВО + a=червено + u=СИВО (= [o])
```

**Думи:**
```
eau     beau    gâteau  bateau  chapeau
peau    veau    bureau  tableau manteau
château fauteuil  autobus  autour   autrement
chaud   faux    haut    saut    taux
```

**Изречения:**
```
Rémi a mis le chapeau du bateau dans le gâteau d'eau.
Éva a peint le bureau en beau avec de l'eau chaude.
Le bateau de Rémi est en forme de gâteau au chocolat.
Maman a trouvé un fauteuil dans l'autobus du château.
Éva a sauté du haut du tableau sur le manteau de Rémi.
Rémi a mis de l'eau chaude dans le chapeau du veau.
Le château de Éva est gardé par un veau en manteau.
Rémi a fait un saut de l'autobus sur le tableau de bord.
L'eau du beau château sentait le gâteau, c'était bizarre.
Éva a mis le bureau dans l'eau pour le nettoyer. Ça n'a pas marché.
```

**Критерий:** au/eau = [o] ≥ 9/10.

---

### Ниво 15 — EU/ŒU [ø/œ]

**Педагогическа цел:** Специфичен за французски звук, труден за произнасяне. Apili го показва с изображение на устата — устните се набират напред.

**Цветово правило:**
```
eu  → e=червено + u=СИВО (= [ø] или [œ])
œu  → o=СИВО + e=червено + u=СИВО (= [œ])  [напр. cœur, sœur]
```

**Специфика за имплант:** [ø/œ] е звук, много рядък в другите езици. Ако Alia произнася нещо близко до "ü" на немски или "ö" — приемаме. Не изискваме перфектно артикулиране.

**Думи:**
```
feu     jeu     bleu    nœud    peu
peur    sœur    cœur    beurre  fleur
heure   malheur  bonheur  meilleur  ailleurs
jeudi   jeune   neuf    seul    peuple
fauteuil  creux  vieux   milieu  mieux
```

**Изречения:**
```
Rémi a mis du beurre dans le feu pour faire un jeu.
Éva a trouvé sa sœur dans le cœur du nœud du bleu.
Le vieux monsieur a pleuré parce que la fleur était seule.
Rémi a allumé le feu avec le cœur du beurre.
Éva a dit à sa sœur qu'il y a du feu dans le milieu de la peur.
Rémi a cherché la sœur de Éva dans le meilleur des jeux.
Le jeune bonhomme du feu de jeudi voulait être meilleur.
Éva a trouvé un malheur dans sa fleur de cœur.
Rémi a mis le vieux nœud dans le feu du milieu. Ça sentait.
La sœur de Éva pleurait parce que le beurre était bleu.
```

**Критерий:** eu/œu правилно произнесено ≥ 7/10 (звукът е труден — по-нисък праг).

---

### Ниво 16 — PH = F [f]

**Педагогическа цел:** ph е друг начин да се напише [f]. Кратко ниво — само разширение.

**Цветово правило:**
```
ph → p=синьо + h=СИВО (= заедно = [f]) → и двете букви образуват един звук
```

**Думи:**
```
photo    phoque    phrase    physique   alphabet
pharmacie  philosophe  téléphone   phare      typhon
éléphant   triomphe   Joseph    Sophie    Philippe
```

**Изречения:**
```
Rémi a mis un éléphant dans la pharmacie pour une photo.
Éva a fait une phrase sur le phoque avec l'alphabet.
Sophie a trouvé le phare de Joseph dans la pharmacie.
Rémi a pris une photo du triomphe de l'éléphant au téléphone.
Philippe a mis le typhon dans sa phrase de physique.
```

**Критерий:** ph = [f] ≥ 9/10.

---

## БЛОК 4 — ФИНАЛНИ ГРАФЕМИ

### Ниво 17 — -ET = -È / -ER = -É / -EZ = -É

**Педагогическа цел:** Финалните "et", "er", "ez" се произнасят като [ɛ] или [e]. Три правописни форми — един звук.

**Цветово правило:**
```
-et → e=червено + t=СИВО (= [ɛ])  → finalement = [è]
-er → e=червено + r=СИВО (= [e])  → manger = [é]
-ez → e=червено + z=СИВО (= [e])  → mangez = [é]
```

**Думи:**
```
jouet   carnet  filet   billet  bonnet
manger  chanter  donner  trouver  aimer
allez   mangez  chantez donnez  trouvez
```

**Изречения:**
```
Rémi a perdu son carnet avec le billet du jouet.
Éva a demandé: Allez, mangez le bonnet du filet!
Le chanteur a chanté: Donnez-moi le jouet du bonnet!
Rémi et Éva ont trouvé le filet dans le carnet du chanteur.
Éva a aimé le jouet que Rémi a trouvé dans son carnet.
Mangez vite, dit Rémi, car le carnet va chanter tout seul.
```

**Критерий:** Разграничаване на трите форми ≥ 8/10.

---

### Ниво 18 — -ETTE / -ER- = ÈRE / -ENNE / -ESSE / -ERRE

**Педагогическа цел:** Удвоените съгласни в края на думата. Те "отварят" предходната гласна [e] → [ɛ].

**Цветово правило:**
```
-ette → e=червено + tt=синьо (двойно) + e=СИВО (= [ɛt])
-erre → e=червено + rr=синьо (двойно) + e=СИВО (= [ɛʀ])
-enne → e=червено + nn=синьо (двойно) + e=СИВО (= [ɛn])
-esse → e=червено + ss=синьо (двойно) + e=СИВО (= [ɛs])
-er- (в средата) → er = [ɛʀ] (напр. mère, père, frère)
```

**Думи:**
```
fillette  tablette  assiette  baguette  cigarette
mère     père      frère     Pierre    sévère
Parisienne Italienne citoyenne ancienne    chrétienne
adresse  tristesse  princesse  richesse   politesse
guerre   erre      verre     parterre   erre
```

**Изречения:**
```
La fillette a mis la baguette dans l'assiette de Pierre.
Mère a dit à père que frère a volé la tablette.
La Parisienne sévère a mis la tristesse dans la richesse.
Pierre a cassé le verre sur le parterre de la fillette.
La princesse de la guerre s'appelle Éva et elle mange des baguettes.
Rémi a mis la cigarette dans l'assiette de sa mère. C'était une erreur.
Le frère de la fillette vit dans la politesse d'une adresse bizarre.
```

**Критерий:** Удвоените съгласни правилно четени ≥ 8/10.

---

### Ниво 19 — EC/ES/EF/EL/ER/EP (финални съгласни, произнасяни)

**Педагогическа цел:** Финалните съгласни C, S, F, L, R, P в определени позиции СЕ ПРОИЗНАСЯТ. Контраст с по-рано усвоеното "финалните са неми".

**Правило (без обяснение — само примери с цветове):**
```
lac  → l=синьо + a=червено + c=СИНЬО (произнася се!)
bras → b=синьо + r=синьо + a=червено + s=СИВО (не се произнася!)
bref → b=синьо + r=синьо + e=червено + f=СИНЬО (произнася се!)
```

**Думи:**
```
lac     arc    sac    bec    choc    duc
bras    dos    bois   fois   voix    croix
bref    chef   clef   naïf   actif   vif
bal     mal    sel    gel    col     vol
car     mer    for    bar    sur     cuir
cap     loup   sirop  galop  trop    beaucoup
```

**Изречения:**
```
Rémi a mis le sac dans le bec du canard du lac.
Éva a trouvé le chef du bref roman dans le gel du bar.
Le vol du bal du sel a fait beaucoup de bruit dans le car.
Rémi a vu le cuir du chef dans le lac de galop.
La clef du sel du lac était dans le mal du bar.
```

**Критерий:** Разграничаване "произнася се / не се произнася" ≥ 7/10 (трудно ниво).

---

### Ниво 20 — GN [ɲ] + IL Y A (locution)

**Педагогическа цел:** gn е диграф = [ɲ]. il y a е фиксирана локуция — учи се като цяло.

**Цветово правило:**
```
gn → g=синьо + n=синьо (двете заедно = [ɲ]) → И ДВЕТЕ СИНИ
```

**Думи с gn:**
```
vigne    signe    ligne   montagne  campagne
champignon  saigner  soigner  gagner   peigner
Espagne  Bretagne  Allemagne  Pologne  Bourgogne
```

**il y a (локуция):**
```
il y a → il=синьо + y=червено + a=червено (= "иля")
```
Учи се наизуст като дума. Не се разбира по части.

**Изречения:**
```
Rémi est allé faire une randonnée en montagne, accompagné d'une vache et de sa poule préférée.
Il y a un champignon dans la campagne de Bretagne.
Éva roulait à vélo sur la route quand un lutin lui fit un signe de la main.
Il y a une vigne en Espagne qui fait du vin de champignon.
La montagne signe l'Allemagne de la Pologne selon la ligne de Rémi.
En plein hiver, Luc s'est baigné dans la rivière, il s'est fait mordre par des poissons et est ressorti plein de boutons.
Il y a une araignée sous la robe de nuit de Charlotte depuis mardi.
Éva soigne un chaton très mignon qu'elle a trouvé dans la campagne.
Rémi a oublié son peigne dans ses cheveux après avoir fait son chignon.
Il y a un vigneron en Bourgogne qui signe ses vignes avec du champignon.
```

**Критерий:** gn = [ɲ] ≥ 9/10. il y a = "иля" ≥ 5/5.

---

### Ниво 21 — ELLE / -ILLE / -IEN

**Педагогическа цел:** elle = [ɛl]; -ille = [ij]; -ien = [jɛ̃]. Сложни финали.

**Цветово правило:**
```
elle  → e=червено + ll=синьо + e=СИВО (= [ɛl])
-ille → i=червено + ll=синьо + e=СИВО (= [ij]) — quand "ill" est précédé d'une voyelle
-ien  → i=червено + e=СИВО + n=СИВО (= [jɛ̃])
```

**Думи:**
```
elle    belle   selle   uelle   uelle
fille   bille   ville   mille   famille
tille   grille  brille  guille  trille
chien   bien    mien    tien    viens
lien    rien    soutien  ancien  pharmacien
```

**Изречения:**
```
Elle a mis la fille de la ville dans la selle du chien.
Le chien de la pharmacienne brillait dans la grille.
Rémi a dit: mille fois rien ne vaut bien mieux.
La belle fille du pharmacien habitait une villa brillante.
Elle a mis le lien du chien dans la famille de ville.
Éva: rien de rien ne soutient l'ancien bien du chien.
```

---

## БЛОК 5 — КОНТЕКСТУАЛНИ ПРАВИЛА

> **Педагогически принцип за Блок 5:**
> Тук Alia научава, че ЕДИН ЗНАК може да се произнася по различен начин
> в зависимост от контекста. Това е напреднало ниво — изисква сигурна база.

---

### Ниво 22 — CE/CI = SE/SI + ÇA/ÇO/ÇU

**Педагогическа цел:** "c" пред e/i = [s]. Cedille (ç) = [s] пред a/o/u.

**Правило (визуално):**
```
ca → [ka] (без седила)
ce → [sə] (c меко пред e)
ci → [si] (c меко пред i)
ça → [sa] (c с cedille)
```

**Думи:**
```
cerise   ceinture  cent    cela    ceci
cinéma   cigale    ciel    citron  cirque
garçon   façon     leçon   maçon   reçu
ça       çà-et-là  ça va   comme-ci comme-ça
```

**Изречения:**
```
Rémi a mis la cerise du cinéma dans le cirque du ciel.
Éva a demandé: ça va le garçon de la façon bizarre?
La cigale a chanté cent leçons sur la ceinture du maçon.
Rémi a reçu un citron du ciel par la façon du garçon.
Le garçon du cinéma a dit comme ça: ça va la cerise?
```

**Критерий:** c пред e/i = [s] ≥ 9/10. ç = [s] ≥ 9/10.

---

### Ниво 23 — GI/GE = JI/JE + GEA/GEO = JA/JO

**Педагогическа цел:** "g" пред e/i = [ʒ] (меко). Аналогично на c/s правилото.

**Правило:**
```
ga → [ga] (твърдо)
ge → [ʒə] (меко)
gi → [ʒi] (меко)
gea → [ʒa] (e = безмълвно между g и a)
geo → [ʒo]
```

**Думи:**
```
girafe   gilet    gitan   givre   giron
genou   geôle    gel     gelée   gêne
pigeon  plongeon bourgeon mangeons orangeade
géant   génial   général géographie  géologie
```

**Изречения:**
```
Rémi a mis la girafe dans le genou du géant.
Éva a dessiné le général de la géologie sur le gilet du gitan.
Le pigeon de Rémi a mangé le gel du genou du géant.
La girafe géante a fait de la géographie dans la geôle.
Rémi a ordonné au pigeon: mange l'orangeade du bourgeon!
```

---

### Ниво 24 — TI = SI (в -tion, -tiel, -tieux)

**Педагогическа цел:** "ti" в суфикс -tion = [sj]. Важно за четенето на многосрични думи.

**Правило:**
```
-tion  → [sjõ]  (nation, action, position)
-tiel  → [sjɛl] (essentiel, partiel)
-tieux → [sjø]  (ambitieux, prétentieux)
```

**Думи:**
```
nation   action   station   position   solution
ambition  attention  invitation  félicitation  conversation
essentiel  partiel   confidentiel  potentiel  différentiel
ambitieux  prétentieux  consciencieux  minutieux  sérieux
```

**Изречения:**
```
Rémi a invité une nation entière à sa station de train.
Éva a expliqué la solution de la position ambiguë à l'attention de tous.
Le conscientieux Rémi a mis l'attention dans sa conversation.
L'action de la nation a créé une commotion dans la station.
Éva: la solution essentielle de la position est la félicitation!
```

---

### Ниво 25 — S INTERVOCALIQUE = Z

**Педагогическа цел:** "s" между две гласни се произнася [z].

**Правило:**
```
maison → mai[z]on (s между две гласни = z)
rose   → ro[z]e
```
*Контраст: soupe → [s] (s в началото = [s] нормално)*

**Думи:**
```
maison   rose    saison  raison  poison
voisin   cuisine  bison   désert  musée
résultat  présent  visage  mosaïque  besoin
```

**Изречения:**
```
Rémi a mis du poison dans la maison du voisin par saison.
Éva a fait une mosaïque en rose dans la cuisine de la maison.
Le bison du désert a besoin de la raison du musée.
Rémi a présenté le résultat du visage du bison à la saison.
La rose de la voisine pousse dans la cuisine depuis la saison dernière.
```

---

### Ниво 26 — -AIL/-AILLE + -EIL/-EILLE + -OUIl/-OUILLE + -EUIl/-EUILLE

**Педагогическа цел:** Поредица от диграфи с "ill" след гласна = [j].

**Правило:**
```
-ail  → [aj]   (travail, rail)
-aille → [aj]  (taille, paille)
-eil  → [ɛj]   (soleil, réveil)
-eille → [ɛj]  (abeille, bouteille)
-ouil → [uj]   (fenouil)
-ouille → [uj] (grenouille, rouille)
-euil → [œj]   (feuille, deuil)
-euille → [œj] (portefeuille)
```

**Думи:**
```
travail    rail     taille    paille    médaille
soleil     réveil   oreille   abeille   bouteille
grenouille rouille  mouille   brouille  fouille
feuille    deuil    fauteuil  seuil     portefeuille
```

**Изречения:**
```
Rémi s'est réveillé au réveil du soleil en pyjama de paille.
L'abeille de Éva a mis du miel dans la bouteille du travail.
La grenouille a trouvé l'oreille de Rémi sous le fauteuil.
Éva a mis les feuilles du portefeuille dans la bouteille de l'abeille.
Rémi a fait la taille de la paille avec la médaille du soleil.
La grenouille mouillée a brouillé les tailles de la paille.
```

---

## БЛОК 6 — ФИНАЛИЗАЦИЯ

### Ниво 27 — Y + X (= CS или GZ)

**Педагогическа цел:** Финалните две сложни графеми.

#### Y:

**Правило:**
```
y между две гласни → [j] + i (= удвоява се)
  payer → pay[j]er
y в началото → [j]  (yeux, yoga)
y след съгласна → [i] (crayon, tuyau)
```

**Думи:**
```
yeux    yoga    yaourt  yankee  yoyo
crayon  tuyau   payer   rayer   essuyer
voyage  royal   moyen   foyer   loyer
rayon   noyau   joyeux  soyeux  voyelle
```

#### X:

**Правило:**
```
x = [ks] в повечето позиции (extra, boxe, taxi)
x = [gz] между гласни (exemple, examen, exact)
x = [s] в certains mots (six, dix, soixante)
x = СИВО в многобройни позиции (voix, croix)
```

**Думи:**
```
extra    boxe    taxi    exposition  excursion
exemple  examen  exact   exact       exigeant
six      dix     soixante  dixième   sixième
voix     croix   paix     noix       index
```

**Финални изречения за Ниво 27:**
```
Victor est capable d'aboyer aussi bien qu'un vrai chien, c'est incroyable !
Salomé a rattrappe Émilie qui tombait de la barre fixe, elle a d'excellents réflexes.
À l'aide d'un extincteur, Paul a éteint la bougie qui était sur la tab,elle a dû présenter ses excuses.
Charlotte s'est coincé l'index dans la portière du taxi.
Émilie est partie en excursion avec sa classe, ils sont allés voir une exposition de peinture, elle a fait tomber plusieurs tableaux.
Paul va devoir nettoyer la fenêtre du salon, car on ne voit plus à travers.
Marc a perdu son dernier match, il n'aime plus la boxe.
Florence est allée à la boulangerie pour acheter une baguette ; en rentrant chez elle, elle s'est rendu compte qu'elle avait oublié de la payer.
Éva a mis son yoyo dans les yeux de Rémi et il a crié : extra !
Rémi a fait un examen sur les six voyelles devant soixante personnes.
```

---

## ФИНАЛЕН ТЕСТ — GRADUATION DE LECTURE

След завършен Блок 6, Alia преминава "Graduation Test" — специален модул:

**Текст 1 (Niveau élémentaire — само Блок 1–2):**
> Le chat de Rémi a mangé la vache de Éva. La vache était furieuse. Elle a mis le chat dans le jardin. Rémi a ri.

**Текст 2 (Niveau intermédiaire — Блок 3–4):**
> En automne, les feuilles tombent des arbres comme une chanson. Rémi a ramassé cent feuilles, une bouteille d'eau et un champignon géant. Il les a mis dans son sac et il est parti à l'école. La maîtresse n'était pas contente.

**Текст 3 (Niveau avancé — Блок 5–6):**
> L'exposition de peinture avait lieu dans une station de train abandonnée. Soixante visiteurs sont arrivés, dont un voisin ambitieux avec un portefeuille de grenouilles. L'organisation était sérieuse mais la solution de l'architecte était exceptionnelle: les tableaux se trouvaient sur le plafond.

**Критерий за graduation:** Текст 3 произнесен с ≥ 75% точност при speech recognition.

**Финална награда:** Специална анимация с Karumi, фраза: *"Alia, tu sais lire ! TOUTES les lettres du français ! Tu es une CHAMPIONNE absolue !"*

---

## АДАПТИВЕН АЛГОРИТЪМ (за разработчика)

```python
# При всеки елемент се пази:
# attempts: int
# correct: int
# status: 'nouveau' | 'en_cours' | 'difficile' | 'maitrise'

def update_status(element):
    rate = element.correct / element.attempts if element.attempts > 0 else 0
    
    if element.attempts < 3:
        return 'nouveau'
    elif rate >= 0.85 and element.attempts >= 5:
        return 'maitrise'
    elif rate < 0.50:
        return 'difficile'
    else:
        return 'en_cours'

# Честота на поява:
# 'difficile'  → 3× по-често от 'en_cours'
# 'maitrise'   → 1× на 10 упражнения (за запазване)
# 'nouveau'    → всяко ново ниво въвежда max 5 нови елемента наведнъж

# Специално за Alia (кохлеарен имплант):
# Минимален брой повторения преди 'maitrise': 15 (вместо стандартните 5)
# Причина: фонологичната консолидация отнема повече итерации
```

---

## ПРОМПТИ ЗА CLAUDE API (разширени)

### Генериране на изречения по ниво

```python
PROMPT_SENTENCES = """
Tu es un assistant pédagogique pour Alia, 13 ans, avec un implant cochléaire, qui apprend à lire en français avec la méthode Apili.

NIVEAU ACTUEL: {niveau_nom}
GRAPHÈMES MAÎTRISÉS: {graphemes_maitrisees}
MOTS CONNUS: {mots_connus}

Génère 5 phrases COURTES (max 10 mots) et TRÈS AMUSANTES avec les personnages Rémi et Éva.
CONTRAINTES ABSOLUES:
- N'utilise QUE les graphèmes maîtrisés listés ci-dessus
- Les phrases doivent être absurdes et drôles (humour = principe central Apili)
- Une phrase par ligne, sans numérotation
- Pas de ponctuation complexe sauf le point final

Exemples du style voulu:
"Rémi a mis le chat dans le frigo pour le garder au frais."
"Éva a commandé une girafe par téléphone et elle l'a mise dans sa valise."
"""
```

### Génération de mots par niveau

```python
PROMPT_WORDS = """
Tu es un assistant pour créer du matériel pédagogique Apili pour Alia.

GRAPHÈMES DISPONIBLES: {graphemes}
Génère 20 mots en français qui:
- N'utilisent QUE les graphèmes listés
- Sont des vrais mots courants (fréquents en français)
- Sont variés (noms, verbes, adjectifs)
- Format: un mot par ligne, minuscules

Réponds UNIQUEMENT avec la liste de mots, sans commentaire.
"""
```

---

## CHECKLIST D'IMPLÉMENTATION

| Ниво | Ключ в БД | Статус | Приоритет |
|------|-----------|--------|-----------|
| 0 | `voyelles` | ✅ MVP | — |
| 1 | `consonnes_1` | ✅ MVP | — |
| 2 | `lecture_rapide` | ✅ MVP | — |
| 3 | `mots_simples` | ✅ MVP | — |
| 4 | `phrases` | ✅ MVP | — |
| 5 | `consonnes_2` | 📋 | 🔴 Следващ |
| 6 | `consonnes_3` | 📋 | 🔴 |
| 7 | `syllabes_vc` | 📋 | 🔴 |
| 8 | `lettre_h` | 📋 | 🟡 |
| 9 | `consolidation_b2` | 📋 | 🟡 |
| 10 | `ou` | 📋 | 🟡 |
| 11 | `on_om` | 📋 | 🟢 |
| 12 | `an_en` | 📋 | 🟢 |
| 13 | `in_ain` | 📋 | 🟢 |
| 14 | `au_eau` | 📋 | 🟢 |
| 15 | `eu_oeu` | 📋 | 🟢 |
| 16 | `ph` | 📋 | 🟢 |
| 17 | `finales_er_ez_et` | 📋 | 🟢 |
| 18 | `finales_doubles` | 📋 | 🟢 |
| 19 | `finales_prononcees` | 📋 | 🟢 |
| 20 | `gn_ilya` | 📋 | 🟢 |
| 21 | `elle_ille_ien` | 📋 | 🟢 |
| 22 | `c_cedille` | 📋 | 🟢 |
| 23 | `g_doux` | 📋 | 🟢 |
| 24 | `ti_si` | 📋 | 🟢 |
| 25 | `s_intervocalique` | 📋 | 🟢 |
| 26 | `ail_eil_ouil_euil` | 📋 | 🟢 |
| 27 | `y_x` | 📋 | 🟢 |

---

## ПЕДАГОГИЧЕСКИ БЕЛЕЖКИ ЗА МАЙКАТА

**Как да използваш приложението с Alia:**

1. **15–20 минути на ден** са достатъчни — не повече. Мозъкът консолидира знанията по време на сън.

2. **Никога не принуждавай.** Ако Alia откаже — отлагате за утре. Мотивацията е всичко.

3. **Смейте се заедно.** Изреченията са абсурдни нарочно. Смехът = по-дълбоко запаметяване.

4. **Не корегирай артикулацията по телефон.** Оставяй на логопеда произносителните въпроси. Ти помагаш с ЧЕТЕНЕТО — разпознаването на знаците.

5. **Хвали УСИЛИЕТО, не резултата.** "Alia, tu as vraiment essayé fort!" е по-ценно от "Bravo, c'est juste!"

6. **При трудно ниво — не се паникьосвай.** Може да остане на едно ниво 2–3 седмици. Нормално е. Напредъкът не е линеен.

7. **Следи дашборда** — той ще ти покаже кои елементи затрудняват Alia. Можеш да ги практикувате устно в ежедневието.

---

*CURRICULUM.md — Lire avec Alia — v1.0 — 2026-06-03*
*Документът се актуализира при нови педагогически открития от работата с Alia.*
