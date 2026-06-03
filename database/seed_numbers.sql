-- seed_numbers.sql — Les Nombres sector
-- Source: NOMBRES_METHODOLOGY.md v1.0

-- New progress table for numbers
CREATE TABLE IF NOT EXISTS numbers_progress (
  id INT AUTO_INCREMENT PRIMARY KEY,
  level VARCHAR(10),
  number_value INT,
  word_form VARCHAR(100),
  attempts INT DEFAULT 0,
  correct INT DEFAULT 0,
  last_error_type VARCHAR(50),
  mastered BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY unique_number (level, number_value)
);

-- Add numbers levels (all locked)
INSERT INTO levels (level_key, block, order_index, name_fr, exercise_type, is_unlocked) VALUES
  ('nombres_n1', 10, 0, 'Les nombres 0–10',   'number_match', FALSE),
  ('nombres_n2', 10, 1, 'Les nombres 11–20',  'number_match', FALSE),
  ('nombres_n3', 10, 2, 'Les dizaines 21–69', 'number_match', FALSE),
  ('nombres_n4', 10, 3, 'Les nombres 70–99',  'number_match', FALSE),
  ('nombres_n5', 10, 4, 'Les centaines',      'number_match', FALSE)
ON DUPLICATE KEY UPDATE name_fr=VALUES(name_fr);

-- N1: 0–10
-- value = JSON {digit, word, silent:[], pronunciation hint}
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('nombres_n1','word','{"digit":0,"word":"zéro","silent":[]}',0),
  ('nombres_n1','word','{"digit":1,"word":"un","silent":["n"]}',1),
  ('nombres_n1','word','{"digit":2,"word":"deux","silent":["x"]}',2),
  ('nombres_n1','word','{"digit":3,"word":"trois","silent":["i","s"]}',3),
  ('nombres_n1','word','{"digit":4,"word":"quatre","silent":["e"]}',4),
  ('nombres_n1','word','{"digit":5,"word":"cinq","silent":[]}',5),
  ('nombres_n1','word','{"digit":6,"word":"six","silent":[]}',6),
  ('nombres_n1','word','{"digit":7,"word":"sept","silent":["p"]}',7),
  ('nombres_n1','word','{"digit":8,"word":"huit","silent":["h"]}',8),
  ('nombres_n1','word','{"digit":9,"word":"neuf","silent":[]}',9),
  ('nombres_n1','word','{"digit":10,"word":"dix","silent":[]}',10);

-- N2: 11–20
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('nombres_n2','word','{"digit":11,"word":"onze","silent":["e"]}',0),
  ('nombres_n2','word','{"digit":12,"word":"douze","silent":["e"]}',1),
  ('nombres_n2','word','{"digit":13,"word":"treize","silent":["e"]}',2),
  ('nombres_n2','word','{"digit":14,"word":"quatorze","silent":["e"]}',3),
  ('nombres_n2','word','{"digit":15,"word":"quinze","silent":["e"]}',4),
  ('nombres_n2','word','{"digit":16,"word":"seize","silent":["e"]}',5),
  ('nombres_n2','word','{"digit":17,"word":"dix-sept","silent":["s"]}',6),
  ('nombres_n2','word','{"digit":18,"word":"dix-huit","silent":["x","h"]}',7),
  ('nombres_n2','word','{"digit":19,"word":"dix-neuf","silent":["x"]}',8),
  ('nombres_n2','word','{"digit":20,"word":"vingt","silent":["t"]}',9);

-- N3: key dizaines
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('nombres_n3','word','{"digit":21,"word":"vingt et un","silent":[]}',0),
  ('nombres_n3','word','{"digit":22,"word":"vingt-deux","silent":["x"]}',1),
  ('nombres_n3','word','{"digit":30,"word":"trente","silent":["e"]}',2),
  ('nombres_n3','word','{"digit":31,"word":"trente et un","silent":[]}',3),
  ('nombres_n3','word','{"digit":40,"word":"quarante","silent":["e"]}',4),
  ('nombres_n3','word','{"digit":41,"word":"quarante et un","silent":[]}',5),
  ('nombres_n3','word','{"digit":50,"word":"cinquante","silent":["e"]}',6),
  ('nombres_n3','word','{"digit":60,"word":"soixante","silent":["e"]}',7),
  ('nombres_n3','word','{"digit":61,"word":"soixante et un","silent":[]}',8),
  ('nombres_n3','word','{"digit":65,"word":"soixante-cinq","silent":[]}',9);

-- N4: 70–99
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('nombres_n4','word','{"digit":70,"word":"soixante-dix","silent":[]}',0),
  ('nombres_n4','word','{"digit":71,"word":"soixante et onze","silent":[]}',1),
  ('nombres_n4','word','{"digit":72,"word":"soixante-douze","silent":["e"]}',2),
  ('nombres_n4','word','{"digit":80,"word":"quatre-vingts","silent":[]}',3),
  ('nombres_n4','word','{"digit":81,"word":"quatre-vingt-un","silent":[]}',4),
  ('nombres_n4','word','{"digit":90,"word":"quatre-vingt-dix","silent":[]}',5),
  ('nombres_n4','word','{"digit":91,"word":"quatre-vingt-onze","silent":[]}',6),
  ('nombres_n4','word','{"digit":99,"word":"quatre-vingt-dix-neuf","silent":[]}',7);

-- N5: 100+
INSERT INTO level_content (level_key, type, value, order_index) VALUES
  ('nombres_n5','word','{"digit":100,"word":"cent","silent":["t"]}',0),
  ('nombres_n5','word','{"digit":200,"word":"deux cents","silent":["s"]}',1),
  ('nombres_n5','word','{"digit":201,"word":"deux cent un","silent":[]}',2),
  ('nombres_n5','word','{"digit":1000,"word":"mille","silent":["e"]}',3),
  ('nombres_n5','word','{"digit":2000,"word":"deux mille","silent":["e"]}',4),
  ('nombres_n5','word','{"digit":2026,"word":"deux mille vingt-six","silent":[]}',5);
