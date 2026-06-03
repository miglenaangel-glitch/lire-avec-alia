-- seed_levels.sql — Lire avec Alia
-- Source: CURRICULUM.md v1.0
-- Run AFTER schema.sql

-- ────────────────────────────────────────────────
-- LEVELS META
-- ────────────────────────────────────────────────
INSERT INTO levels (level_key, block, order_index, name_fr, exercise_type, is_unlocked) VALUES
  ('voyelles',       1, 0, 'Les voyelles',     'tap_to_hear',    TRUE),
  ('consonnes_1',    1, 1, 'Les consonnes 1',  'slide_to_merge', TRUE),
  ('lecture_rapide', 1, 2, 'Lecture rapide',   'rapid_read',     TRUE),
  ('mots_simples',   1, 3, 'Les mots',         'word_tap',       TRUE),
  ('phrases',        1, 4, 'Les phrases',      'sentence_read',  TRUE),
  ('consonnes_2',    2, 5, 'Les consonnes 2',  'slide_to_merge', FALSE)
ON DUPLICATE KEY UPDATE
  block=VALUES(block), order_index=VALUES(order_index),
  name_fr=VALUES(name_fr), exercise_type=VALUES(exercise_type);

-- ────────────────────────────────────────────────
-- NIVEAU 0 — VOYELLES
-- type='letter', value = JSON {letter, color, gesture}
-- ────────────────────────────────────────────────
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('voyelles', 'letter', '{"letter":"a","color":"vowel","gesture":"Tu écartes les mains"}',          0),
  ('voyelles', 'letter', '{"letter":"é","color":"vowel","gesture":"Tu lèves le doigt"}',             1),
  ('voyelles', 'letter', '{"letter":"i","color":"vowel","gesture":"Montre du doigt et ris"}',        2),
  ('voyelles', 'letter', '{"letter":"o","color":"vowel","gesture":"Mets ta main devant ta bouche"}', 3),
  ('voyelles', 'letter', '{"letter":"u","color":"vowel","gesture":"Mets tes mains comme un volant"}',4),
  ('voyelles', 'letter', '{"letter":"e","color":"vowel","gesture":"Mets ton index sous ta bouche"}', 5),
  ('voyelles', 'letter', '{"letter":"y","color":"vowel","gesture":"Comme i, avec un sourire"}',      6);

-- ────────────────────────────────────────────────
-- NIVEAU 1 — CONSONNES 1 (f, s, ch, l, m, r)
-- type='letter' for consonants (order 0–5)
-- type='syllable' for vowels (order 10–14)
-- ────────────────────────────────────────────────
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('consonnes_1', 'letter',   'f',  0),
  ('consonnes_1', 'letter',   's',  1),
  ('consonnes_1', 'letter',   'ch', 2),
  ('consonnes_1', 'letter',   'l',  3),
  ('consonnes_1', 'letter',   'm',  4),
  ('consonnes_1', 'letter',   'r',  5),
  ('consonnes_1', 'syllable', 'a',  10),
  ('consonnes_1', 'syllable', 'é',  11),
  ('consonnes_1', 'syllable', 'i',  12),
  ('consonnes_1', 'syllable', 'o',  13),
  ('consonnes_1', 'syllable', 'u',  14);

-- ────────────────────────────────────────────────
-- NIVEAU 2 — LECTURE RAPIDE
-- No content rows needed — syllables generated in JS from consonnes_1
-- ────────────────────────────────────────────────

-- ────────────────────────────────────────────────
-- NIVEAU 3 — MOTS SIMPLES (48 mots)
-- type='word', value = JSON {word, silent:[]}
-- ────────────────────────────────────────────────
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('mots_simples','word','{"word":"chat","silent":["t"]}',0),
  ('mots_simples','word','{"word":"ami","silent":[]}',1),
  ('mots_simples','word','{"word":"lave","silent":["e"]}',2),
  ('mots_simples','word','{"word":"rame","silent":["e"]}',3),
  ('mots_simples','word','{"word":"joli","silent":[]}',4),
  ('mots_simples','word','{"word":"vache","silent":["e"]}',5),
  ('mots_simples','word','{"word":"lama","silent":[]}',6),
  ('mots_simples','word','{"word":"vélo","silent":[]}',7),
  ('mots_simples','word','{"word":"mari","silent":[]}',8),
  ('mots_simples','word','{"word":"rémi","silent":[]}',9),
  ('mots_simples','word','{"word":"fume","silent":["e"]}',10),
  ('mots_simples','word','{"word":"mamie","silent":["e"]}',11),
  ('mots_simples','word','{"word":"mur","silent":[]}',12),
  ('mots_simples','word','{"word":"lire","silent":["e"]}',13),
  ('mots_simples','word','{"word":"rue","silent":["e"]}',14),
  ('mots_simples','word','{"word":"mare","silent":["e"]}',15),
  ('mots_simples','word','{"word":"vis","silent":["s"]}',16),
  ('mots_simples','word','{"word":"rire","silent":["e"]}',17),
  ('mots_simples','word','{"word":"avalé","silent":[]}',18),
  ('mots_simples','word','{"word":"fil","silent":["l"]}',19),
  ('mots_simples','word','{"word":"lime","silent":["e"]}',20),
  ('mots_simples','word','{"word":"mal","silent":[]}',21),
  ('mots_simples','word','{"word":"surimi","silent":[]}',22),
  ('mots_simples','word','{"word":"folie","silent":["e"]}',23),
  ('mots_simples','word','{"word":"cheval","silent":["l"]}',24),
  ('mots_simples','word','{"word":"lavé","silent":[]}',25),
  ('mots_simples','word','{"word":"olive","silent":["e"]}',26),
  ('mots_simples','word','{"word":"safari","silent":[]}',27),
  ('mots_simples','word','{"word":"carafe","silent":["e"]}',28),
  ('mots_simples','word','{"word":"famille","silent":["e"]}',29),
  ('mots_simples','word','{"word":"camion","silent":[]}',30),
  ('mots_simples','word','{"word":"soleil","silent":[]}',31),
  ('mots_simples','word','{"word":"merci","silent":[]}',32),
  ('mots_simples','word','{"word":"farine","silent":["e"]}',33),
  ('mots_simples','word','{"word":"virage","silent":["e"]}',34),
  ('mots_simples','word','{"word":"couloir","silent":[]}',35),
  ('mots_simples','word','{"word":"musée","silent":["e"]}',36),
  ('mots_simples','word','{"word":"marché","silent":[]}',37),
  ('mots_simples','word','{"word":"village","silent":["e"]}',38),
  ('mots_simples','word','{"word":"rivière","silent":["e"]}',39),
  ('mots_simples','word','{"word":"château","silent":[]}',40),
  ('mots_simples','word','{"word":"voiture","silent":["e"]}',41),
  ('mots_simples','word','{"word":"fumée","silent":["e"]}',42),
  ('mots_simples','word','{"word":"liberté","silent":[]}',43),
  ('mots_simples','word','{"word":"miracle","silent":["e"]}',44),
  ('mots_simples','word','{"word":"chimie","silent":["e"]}',45),
  ('mots_simples','word','{"word":"salami","silent":[]}',46),
  ('mots_simples','word','{"word":"sale","silent":["e"]}',47);

-- ────────────────────────────────────────────────
-- NIVEAU 4 — PHRASES (40 phrases)
-- type='sentence', value = sentence text
-- ────────────────────────────────────────────────
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('phrases','sentence','Rémi lave la vache.',0),
  ('phrases','sentence','Éva va lire.',1),
  ('phrases','sentence','Rémi a sali le lit.',2),
  ('phrases','sentence','Rémi a volé le rat.',3),
  ('phrases','sentence','Rémi a vomi par la fenêtre.',4),
  ('phrases','sentence','Éva dort sur un sac de patates.',5),
  ('phrases','sentence','Rémi a mordu la patte du chat.',6),
  ('phrases','sentence','Éva a mis du sel dans le café de Rémi.',7),
  ('phrases','sentence','Le chat de Rémi a avalé le vélo de Éva.',8),
  ('phrases','sentence','Rémi a mis la vache sur le canapé.',9),
  ('phrases','sentence','Éva a lire une fiche sur les lamas.',10),
  ('phrases','sentence','Rémi a fumé une carafe de limonade.',11),
  ('phrases','sentence','Le lama de Éva a sali la robe de la maîtresse.',12),
  ('phrases','sentence','Rémi a ri si fort qu''il a vomi sur le chat.',13),
  ('phrases','sentence','Éva a volé le surimi de Rémi et elle a fui.',14),
  ('phrases','sentence','Rémi a mis le chat dans le lavabo.',15),
  ('phrases','sentence','La vache a lu le livre de Rémi.',16),
  ('phrases','sentence','Éva a salé le vélo de Rémi par erreur.',17),
  ('phrases','sentence','Rémi a avalé une lime par accident.',18),
  ('phrases','sentence','Le chat a ri de Rémi.',19),
  ('phrases','sentence','La maîtresse a vu Rémi manger la vache.',20),
  ('phrases','sentence','Éva chante si fort que le chat s''est enfui.',21),
  ('phrases','sentence','Rémi a colorié la vache en vert.',22),
  ('phrases','sentence','Le chat de Éva a mis du sel partout.',23),
  ('phrases','sentence','Rémi a choisi de dormir sur le lama.',24),
  ('phrases','sentence','La vache a volé le vélo de Rémi et elle a filé.',25),
  ('phrases','sentence','Éva a mis le lama dans le réfrigérateur.',26),
  ('phrases','sentence','Rémi a rit jusqu''à vomir sur la maîtresse.',27),
  ('phrases','sentence','Le chat a sali le livre de Rémi avec les pattes.',28),
  ('phrases','sentence','Éva a fait la course avec une vache et elle a perdu.',29),
  ('phrases','sentence','Rémi a mis le chat dans le sac de Éva.',30),
  ('phrases','sentence','La vache a mordu le livre de la maîtresse.',31),
  ('phrases','sentence','Rémi a avalé le stylo de Éva.',32),
  ('phrases','sentence','Éva a ri si fort qu''elle a réveillé le voisin.',33),
  ('phrases','sentence','Rémi a mis le lama sur le toit de la voiture.',34),
  ('phrases','sentence','Le chat a lu le livre de Rémi et il a ri.',35),
  ('phrases','sentence','Éva a mis la vache dans le sac à dos de Rémi.',36),
  ('phrases','sentence','Rémi a salé le café du directeur.',37),
  ('phrases','sentence','La vache et le chat ont ri de Rémi.',38),
  ('phrases','sentence','Éva a mis le surimi dans les chaussures de Rémi.',39);

-- ────────────────────────────────────────────────
-- NIVEAU 5 — CONSONNES 2 (j, v, p, t, b) — LOCKED
-- type='letter' for consonants, type='syllable' for vowels
-- ────────────────────────────────────────────────
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('consonnes_2', 'letter',   'j',  0),
  ('consonnes_2', 'letter',   'v',  1),
  ('consonnes_2', 'letter',   'p',  2),
  ('consonnes_2', 'letter',   't',  3),
  ('consonnes_2', 'letter',   'b',  4),
  ('consonnes_2', 'syllable', 'a',  10),
  ('consonnes_2', 'syllable', 'é',  11),
  ('consonnes_2', 'syllable', 'i',  12),
  ('consonnes_2', 'syllable', 'o',  13),
  ('consonnes_2', 'syllable', 'u',  14),
  -- Words for consonnes_2
  ('consonnes_2', 'word', '{"word":"jupe","silent":["e"]}', 20),
  ('consonnes_2', 'word', '{"word":"jambe","silent":["e"]}', 21),
  ('consonnes_2', 'word', '{"word":"jardin","silent":[]}', 22),
  ('consonnes_2', 'word', '{"word":"jouet","silent":["t"]}', 23),
  ('consonnes_2', 'word', '{"word":"joli","silent":[]}', 24),
  ('consonnes_2', 'word', '{"word":"vélo","silent":[]}', 25),
  ('consonnes_2', 'word', '{"word":"valise","silent":["e"]}', 26),
  ('consonnes_2', 'word', '{"word":"verre","silent":["e"]}', 27),
  ('consonnes_2', 'word', '{"word":"vitre","silent":["e"]}', 28),
  ('consonnes_2', 'word', '{"word":"voile","silent":["e"]}', 29),
  ('consonnes_2', 'word', '{"word":"papa","silent":[]}', 30),
  ('consonnes_2', 'word', '{"word":"patte","silent":["e"]}', 31),
  ('consonnes_2', 'word', '{"word":"poire","silent":["e"]}', 32),
  ('consonnes_2', 'word', '{"word":"pile","silent":["e"]}', 33),
  ('consonnes_2', 'word', '{"word":"table","silent":["e"]}', 34),
  ('consonnes_2', 'word', '{"word":"tapis","silent":["s"]}', 35),
  ('consonnes_2', 'word', '{"word":"tigre","silent":["e"]}', 36),
  ('consonnes_2', 'word', '{"word":"tube","silent":["e"]}', 37),
  ('consonnes_2', 'word', '{"word":"balle","silent":["e"]}', 38),
  ('consonnes_2', 'word', '{"word":"bateau","silent":["x"]}', 39),
  ('consonnes_2', 'word', '{"word":"bébé","silent":[]}', 40),
  -- Sentences for consonnes_2
  ('consonnes_2', 'sentence', 'Rémi a mis sa jupe sur la tête du chat.', 50),
  ('consonnes_2', 'sentence', 'Éva a volé le vélo de Rémi et elle l''a jeté dans la rivière.', 51),
  ('consonnes_2', 'sentence', 'Le bébé de Rémi a mordu la table.', 52),
  ('consonnes_2', 'sentence', 'Papa a mis le tigre dans le bain.', 53),
  ('consonnes_2', 'sentence', 'La jupe de Éva vole dans le jardin.', 54),
  ('consonnes_2', 'sentence', 'Rémi a bu la soupe du voisin par erreur.', 55),
  ('consonnes_2', 'sentence', 'Éva a jeté le tapis par la fenêtre.', 56),
  ('consonnes_2', 'sentence', 'Le chat a mis la balle dans la valise de Rémi.', 57),
  ('consonnes_2', 'sentence', 'Papa a trouvé un puma sous son lit.', 58),
  ('consonnes_2', 'sentence', 'Rémi a peint le bateau en rose avec les pattes du chat.', 59);
