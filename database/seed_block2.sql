-- seed_block2.sql — Block 2 levels
-- consonnes_2 already seeded, add lecture_rapide_2, mots_2, phrases_2

-- ── Update consonnes_2 name ──
UPDATE levels SET name_fr = 'Les consonnes 2' WHERE level_key = 'consonnes_2';

-- ── New levels ──
INSERT INTO levels (level_key, block, order_index, name_fr, exercise_type, is_unlocked) VALUES
  ('lecture_rapide_2', 2, 6,  'Lecture rapide 2', 'rapid_read',     FALSE),
  ('mots_2',           2, 7,  'Les mots 2',        'word_tap',       FALSE),
  ('phrases_2',        2, 8,  'Les phrases 2',     'sentence_read',  FALSE)
ON DUPLICATE KEY UPDATE
  block=VALUES(block), order_index=VALUES(order_index),
  name_fr=VALUES(name_fr), exercise_type=VALUES(exercise_type);

-- ── lecture_rapide_2: no content (JS generates from consonnes_2 consonants) ──

-- ── mots_2: words ──
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('mots_2','word','{"word":"jupe","silent":["e"]}',0),
  ('mots_2','word','{"word":"jambe","silent":["e"]}',1),
  ('mots_2','word','{"word":"jardin","silent":[]}',2),
  ('mots_2','word','{"word":"jouet","silent":["t"]}',3),
  ('mots_2','word','{"word":"joli","silent":[]}',4),
  ('mots_2','word','{"word":"vélo","silent":[]}',5),
  ('mots_2','word','{"word":"valise","silent":["e"]}',6),
  ('mots_2','word','{"word":"verre","silent":["e"]}',7),
  ('mots_2','word','{"word":"vitre","silent":["e"]}',8),
  ('mots_2','word','{"word":"voile","silent":["e"]}',9),
  ('mots_2','word','{"word":"papa","silent":[]}',10),
  ('mots_2','word','{"word":"patte","silent":["e"]}',11),
  ('mots_2','word','{"word":"poire","silent":["e"]}',12),
  ('mots_2','word','{"word":"pile","silent":["e"]}',13),
  ('mots_2','word','{"word":"table","silent":["e"]}',14),
  ('mots_2','word','{"word":"tapis","silent":["s"]}',15),
  ('mots_2','word','{"word":"tigre","silent":["e"]}',16),
  ('mots_2','word','{"word":"tube","silent":["e"]}',17),
  ('mots_2','word','{"word":"balle","silent":["e"]}',18),
  ('mots_2','word','{"word":"bateau","silent":["x"]}',19),
  ('mots_2','word','{"word":"bébé","silent":[]}',20);

-- ── phrases_2: sentences ──
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('phrases_2','sentence','Rémi a mis sa jupe sur la tête du chat.',0),
  ('phrases_2','sentence','Éva a volé le vélo de Rémi et elle l''a jeté dans la rivière.',1),
  ('phrases_2','sentence','Le bébé de Rémi a mordu la table.',2),
  ('phrases_2','sentence','Papa a mis le tigre dans le bain.',3),
  ('phrases_2','sentence','La jupe de Éva vole dans le jardin.',4),
  ('phrases_2','sentence','Rémi a bu la soupe du voisin par erreur.',5),
  ('phrases_2','sentence','Éva a jeté le tapis par la fenêtre.',6),
  ('phrases_2','sentence','Le chat a mis la balle dans la valise de Rémi.',7),
  ('phrases_2','sentence','Papa a trouvé un puma sous son lit.',8),
  ('phrases_2','sentence','Rémi a peint le bateau en rose avec les pattes du chat.',9);

-- ── lecture_rapide_2 needs consonants/vowels so JS can generate syllables ──
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('lecture_rapide_2','letter',   'j', 0),
  ('lecture_rapide_2','letter',   'v', 1),
  ('lecture_rapide_2','letter',   'p', 2),
  ('lecture_rapide_2','letter',   't', 3),
  ('lecture_rapide_2','letter',   'b', 4),
  ('lecture_rapide_2','syllable', 'a', 10),
  ('lecture_rapide_2','syllable', 'é', 11),
  ('lecture_rapide_2','syllable', 'i', 12),
  ('lecture_rapide_2','syllable', 'o', 13),
  ('lecture_rapide_2','syllable', 'u', 14);
