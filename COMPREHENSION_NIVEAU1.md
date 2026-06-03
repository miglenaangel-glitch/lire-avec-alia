# COMPRÉHENSION DE TEXTE — NIVEAU 1
## Lire avec Alia — Textes + Questions

**Niveau :** Bloc 1 uniquement (f, s, ch, l, m, r + voyelles)  
**Mots autorisés :** chat, ami, lave, rame, joli, vache, lama, vélo, mari, fume, mamie, mur, lire, rue, mare, vis, rire, avalé, fil, lime, mal, surimi, folie, cheval, lavé, olive, safari, carafe, famille, soleil, merci, farine, virage, couloir, musée, marché, village, rivière, château  
**Personnages :** Rémi, Éva, le chat, la vache, le lama, mamie  
**Style :** Apili — absurde, drôle, mémorable  
**Version :** 1.0 — 2026-06-03

---

## COMMENT ÇA MARCHE (pour КК)

Chaque texte contient :
- **Le texte** — court, colorié selon Apili (consonnes=bleu, voyelles=rouge, muettes=gris)
- **Questions à choix multiple (QCM)** — 3 choix, 1 bonne réponse, tap sur l'écran
- **Questions ouvertes au micro** — Alia répond avec sa voix, réponse libre acceptée

### Format JSON pour l'implémentation

```json
{
  "id": "texte_01",
  "titre": "Le Chat de Rémi",
  "texte": "...",
  "questions": [
    {
      "type": "qcm",
      "question": "Qui lave la vache ?",
      "choix": ["Rémi", "Éva", "le chat"],
      "bonne_reponse": 0,
      "illustration": "remi_lave.png"
    },
    {
      "type": "micro",
      "question": "Pourquoi Éva rit ?",
      "mots_cles_acceptes": ["vache", "lavabo", "drôle", "rigolo", "rit"],
      "reponse_modele": "Parce que Rémi a mis la vache dans le lavabo."
    }
  ]
}
```

---

---

# TEXTE 1 — Le Chat de Rémi
### *(2 phrases — très facile — premier texte)*

---

## Le texte

> **Rémi lave la vache.**
> **Le chat rit.**

---

## Illustration suggérée
Rémi avec un seau d'eau, lavant une vache. La vache a l'air furieux. Le chat est assis à côté et se tient les côtes de rire.

---

## Questions QCM (choix multiple — tap)

**Q1.** Qui lave la vache ?
- 🔵 Rémi ✅
- 🔵 Éva
- 🔵 le chat

**Q2.** Qu'est-ce que Rémi lave ?
- 🔵 le chat
- 🔵 la vache ✅
- 🔵 le vélo

**Q3.** Qui rit ?
- 🔵 Rémi
- 🔵 la vache
- 🔵 le chat ✅

---

## Questions ouvertes au micro 🎤

**Q4.** *"Que fait Rémi ?"*
> Mots-clés acceptés : `lave`, `vache`, `Rémi`
> Réponse modèle : *"Rémi lave la vache."*

**Q5.** *"Le chat est triste ou content ?"*
> Mots-clés acceptés : `content`, `rit`, `rigolo`, `drôle`, `heureux`
> Réponse modèle : *"Le chat est content. Il rit."*

---

---

# TEXTE 2 — La Vache et le Vélo
### *(3 phrases — facile)*

---

## Le texte

> **La vache a volé le vélo de Rémi.**
> **Rémi est furieux.**
> **Éva rit.**

---

## Illustration suggérée
Une vache pédalant sur un vélo dans la rue. Rémi court derrière avec les bras levés, l'air très fâché. Éva est pliée de rire sur le trottoir.

---

## Questions QCM (choix multiple — tap)

**Q1.** Qui a volé le vélo ?
- 🔵 Rémi
- 🔵 Éva
- 🔵 la vache ✅

**Q2.** C'est le vélo de qui ?
- 🔵 Éva
- 🔵 Rémi ✅
- 🔵 le chat

**Q3.** Comment est Rémi ?
- 🔵 furieux ✅
- 🔵 content
- 🔵 fatigué

**Q4.** Qu'est-ce qu'Éva fait ?
- 🔵 Elle court
- 🔵 Elle rit ✅
- 🔵 Elle lave

---

## Questions ouvertes au micro 🎤

**Q5.** *"Qu'est-ce que la vache a fait ?"*
> Mots-clés acceptés : `volé`, `vélo`, `pris`, `vache`
> Réponse modèle : *"La vache a volé le vélo de Rémi."*

**Q6.** *"Pourquoi Éva rit ?"*
> Mots-clés acceptés : `vache`, `vélo`, `drôle`, `rigolo`, `marrant`, `Rémi`
> Réponse libre — toute réponse cohérente est acceptée ✅

---

---

# TEXTE 3 — Le Lama de Mamie
### *(4 phrases — moyen)*

---

## Le texte

> **Mamie a un lama.**
> **Le lama a avalé le sac de farine.**
> **Mamie est mal.**
> **Rémi rit. Éva rit. Le lama rit aussi.**

---

## Illustration suggérée
Mamie (petite dame âgée, l'air catastrophé) regarde un lama avec le museau blanc de farine. Le sac de farine est vide par terre. Rémi et Éva se tordent de rire. Le lama a l'air très satisfait de lui-même.

---

## Questions QCM (choix multiple — tap)

**Q1.** C'est le lama de qui ?
- 🔵 Rémi
- 🔵 Éva
- 🔵 mamie ✅

**Q2.** Qu'est-ce que le lama a avalé ?
- 🔵 le vélo
- 🔵 le sac de farine ✅
- 🔵 le chat

**Q3.** Comment est mamie ?
- 🔵 contente
- 🔵 mal ✅
- 🔵 furieuse

**Q4.** Qui rit à la fin ?
- 🔵 Rémi seulement
- 🔵 Rémi et Éva
- 🔵 Rémi, Éva et le lama ✅

**Q5.** Est-ce que le lama est triste ?
- 🔵 Oui, il pleure
- 🔵 Non, il rit aussi ✅
- 🔵 On ne sait pas

---

## Questions ouvertes au micro 🎤

**Q6.** *"Qu'est-ce que le lama a mangé ?"*
> Mots-clés acceptés : `farine`, `sac`, `avalé`, `mangé`
> Réponse modèle : *"Le lama a avalé le sac de farine."*

**Q7.** *"Est-ce que mamie est contente ?"*
> Mots-clés acceptés : `non`, `mal`, `pas contente`, `fâchée`, `triste`
> Réponse modèle : *"Non, mamie est mal."*

**Q8.** *"Qui rit dans ce texte ?"*
> Mots-clés acceptés : `Rémi`, `Éva`, `lama`, `tout le monde`
> Réponse modèle : *"Rémi rit, Éva rit et le lama rit aussi."*

---

---

# TEXTE 4 — Safari Raté
### *(5 phrases — assez difficile)*

---

## Le texte

> **Rémi a lu un livre sur le safari.**
> **Il a mis le lama, la vache et le chat dans la voiture.**
> **La famille a ri.**
> **Le chat a sali le couloir.**
> **Rémi a dit : c'est le safari de la rue !**

---

## Illustration suggérée
Une petite voiture avec un lama qui sort la tête par la fenêtre, une vache à l'arrière et le chat sur le toit. Rémi est au volant, très fier. Dans le couloir de l'immeuble, il y a des traces de pattes partout. La famille (Éva, mamie) regarde avec des yeux ronds.

---

## Questions QCM (choix multiple — tap)

**Q1.** Qu'est-ce que Rémi a lu ?
- 🔵 un livre sur le safari ✅
- 🔵 un livre sur la vache
- 🔵 un livre sur la famille

**Q2.** Qu'est-ce que Rémi a mis dans la voiture ?
- 🔵 le lama et la vache
- 🔵 le chat seulement
- 🔵 le lama, la vache et le chat ✅

**Q3.** Qui a ri ?
- 🔵 Rémi
- 🔵 le lama
- 🔵 la famille ✅

**Q4.** Qu'est-ce que le chat a fait ?
- 🔵 il a ri
- 🔵 il a sali le couloir ✅
- 🔵 il a lu le livre

**Q5.** Où est le safari de Rémi ?
- 🔵 en Afrique
- 🔵 au marché
- 🔵 dans la rue ✅

---

## Questions ouvertes au micro 🎤

**Q6.** *"Qu'est-ce que Rémi a lu ?"*
> Mots-clés acceptés : `livre`, `safari`, `lu`
> Réponse modèle : *"Rémi a lu un livre sur le safari."*

**Q7.** *"Qu'est-ce que Rémi a mis dans la voiture ?"*
> Mots-clés acceptés : `lama`, `vache`, `chat`, `animaux`
> Réponse modèle : *"Il a mis le lama, la vache et le chat dans la voiture."*

**Q8.** *"Pourquoi c'est drôle ?"*
> Question ouverte — réponse libre ✅
> Mots-clés acceptés : toute explication logique et cohérente
> But : vérifier la compréhension globale + encourager l'expression

**Q9.** *"Est-ce que le safari de Rémi est en Afrique ?"*
> Mots-clés acceptés : `non`, `rue`, `pas en Afrique`, `chez lui`
> Réponse modèle : *"Non, c'est le safari de la rue."*

---

---

# TEXTE 5 — Le Musée du Lama
### *(6-7 phrases — difficile pour ce niveau)*

---

## Le texte

> **Rémi a amené le lama au musée.**
> **Le lama a vu une vache sur un tableau.**
> **Il a ri. Il a sali le mur.**
> **La maîtresse a vu le mur sale.**
> **Elle a dit : Rémi, le musée n'est pas un safari !**
> **Rémi a souri. Le lama aussi.**

---

## Illustration suggérée
Un lama majestueux dans un musée élégant, regardant un grand tableau représentant une vache. Le mur à côté est maculé. Une maîtresse sévère (air très choqué) pointe le mur du doigt. Rémi se tient derrière le lama avec un air innocent. Le lama sourit.

---

## Questions QCM (choix multiple — tap)

**Q1.** Où est-ce que Rémi a amené le lama ?
- 🔵 au marché
- 🔵 au musée ✅
- 🔵 au château

**Q2.** Qu'est-ce que le lama a vu sur le tableau ?
- 🔵 un chat
- 🔵 Rémi
- 🔵 une vache ✅

**Q3.** Qu'est-ce que le lama a sali ?
- 🔵 le tableau
- 🔵 le mur ✅
- 🔵 la maîtresse

**Q4.** Qui a vu le mur sale ?
- 🔵 Éva
- 🔵 mamie
- 🔵 la maîtresse ✅

**Q5.** Qu'est-ce que la maîtresse a dit ?
- 🔵 le musée n'est pas un safari ✅
- 🔵 le lama est joli
- 🔵 Rémi est un ami

**Q6.** À la fin, Rémi est comment ?
- 🔵 furieux
- 🔵 triste
- 🔵 souriant ✅

---

## Questions ouvertes au micro 🎤

**Q7.** *"Où est-ce que Rémi a amené le lama ?"*
> Mots-clés acceptés : `musée`
> Réponse modèle : *"Rémi a amené le lama au musée."*

**Q8.** *"Qu'est-ce que le lama a fait au mur ?"*
> Mots-clés acceptés : `sali`, `sale`, `mur`
> Réponse modèle : *"Le lama a sali le mur."*

**Q9.** *"Qu'est-ce que la maîtresse a dit ?"*
> Mots-clés acceptés : `safari`, `musée`, `pas un safari`
> Réponse modèle : *"Elle a dit : le musée n'est pas un safari."*

**Q10.** *"Est-ce que Rémi est triste à la fin ?"*
> Mots-clés acceptés : `non`, `souriant`, `content`, `rit`, `souri`
> Réponse modèle : *"Non, Rémi a souri."*

**Q11 — QUESTION BONUS** 🌟 *"Tu penses que le lama a aimé le musée ?"*
> Question ouverte totalement libre
> But : aller au-delà du texte, imaginer, s'exprimer
> Toute réponse argumentée = ✅ 
> Réponse idéale (exemple) : *"Oui, parce qu'il a ri et il a souri."*

---

---

# NOTES TECHNIQUES POUR КК

## Structure de progression

| Texte | Phrases | Difficulté | Nouveauté pédagogique |
|-------|---------|-----------|----------------------|
| T1 | 2 | ⭐ | Qui fait quoi ? (sujet + verbe) |
| T2 | 3 | ⭐⭐ | Qui fait quoi à qui ? (sujet + verbe + objet) |
| T3 | 4 | ⭐⭐⭐ | Plusieurs personnages — qui ressent quoi ? |
| T4 | 5 | ⭐⭐⭐⭐ | Séquence d'actions — reconstituer l'histoire |
| T5 | 6–7 | ⭐⭐⭐⭐⭐ | Inférence — comprendre ce qui n'est pas dit |

## Types de questions par objectif

| Type | Objectif | Format |
|------|---------|--------|
| "Qui ?" | Identifier le sujet/personnage | QCM |
| "Quoi ?" | Identifier l'action ou l'objet | QCM |
| "Comment ?" | Émotion, état | QCM |
| "Où ?" | Lieu | QCM |
| "Que fait... ?" | Reformuler une action | Micro |
| "Pourquoi... ?" | Expliquer — inférence | Micro libre |
| "Est-ce que... ?" | Vrai/faux en phrase | Micro |
| Question BONUS | Expression libre | Micro libre |

## Règles d'évaluation pour le micro

```javascript
// Évaluation souple — ne pas bloquer Alia sur la forme
// Vérifier la présence des mots-clés, pas la structure parfaite

function evaluerReponse(reponseAlia, motsClesReqis) {
  const reponseLower = reponseAlia.toLowerCase();
  const motsPresents = motsClesRequis.filter(mot => 
    reponseLower.includes(mot.toLowerCase())
  );
  
  // ≥ 1 mot-clé = réponse acceptée (encouragement)
  // ≥ 2 mots-clés = bonne réponse (bravo)
  if (motsPresents.length >= 2) return 'bravo';
  if (motsPresents.length === 1) return 'accept';
  return 'retry'; // propose d'écouter le modèle, pas d'erreur
}

// JAMAIS de "faux" ou "mauvaise réponse" — toujours:
// "Bravo !" / "Bien essayé !" / "Écoute la réponse..."
```

## Feedback vocal (TTS) après chaque question

```javascript
const FEEDBACK_QCM = {
  correct: [
    "Super Alia, c'est ça !",
    "Bravo, tu as bien lu !",
    "Excellent !"
  ],
  incorrect: [
    "Pas tout à fait — relis le texte !",
    "Essaie encore une fois !"
  ]
};

const FEEDBACK_MICRO = {
  bravo: "Bravo Alia, très bonne réponse !",
  accept: "Bien ! Tu as compris l'essentiel.",
  retry: "Écoute la réponse..." // puis TTS lit la réponse modèle
};
```

## Ordre d'implémentation recommandé

```
🔴 Priorité 1 : T1 + T2 (2-3 phrases, QCM seulement d'abord)
🟡 Priorité 2 : T3 + questions micro
🟢 Priorité 3 : T4 + T5 + question bonus libre
```

---

*COMPREHENSION_NIVEAU1.md — Lire avec Alia — v1.0 — 2026-06-03*
*Textes écrits avec les seuls graphèmes du Bloc 1 (f, s, ch, l, m, r + voyelles)*
*Alia, tu lis et tu comprends ! 🌟*
