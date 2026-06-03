CREATE TABLE IF NOT EXISTS levels (
  id            INT PRIMARY KEY AUTO_INCREMENT,
  level_key     VARCHAR(50) UNIQUE NOT NULL,
  block         TINYINT NOT NULL,
  order_index   TINYINT NOT NULL,
  name_fr       VARCHAR(100) NOT NULL,
  exercise_type ENUM('tap_to_hear','slide_to_merge','rapid_read','word_tap','sentence_read') NOT NULL,
  is_unlocked   BOOLEAN DEFAULT FALSE,
  unlocked_at   TIMESTAMP NULL
);

CREATE TABLE IF NOT EXISTS level_content (
  id          INT PRIMARY KEY AUTO_INCREMENT,
  level_key   VARCHAR(50) NOT NULL,
  type        ENUM('letter','syllable','word','sentence') NOT NULL,
  value       VARCHAR(500) NOT NULL,
  order_index INT DEFAULT 0,
  INDEX idx_level_key (level_key)
);

CREATE TABLE IF NOT EXISTS sessions (
  id INT PRIMARY KEY AUTO_INCREMENT,
  started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  ended_at TIMESTAMP NULL,
  level VARCHAR(50),
  total_exercises INT DEFAULT 0,
  correct_answers INT DEFAULT 0,
  reward_shown BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS progress (
  id INT PRIMARY KEY AUTO_INCREMENT,
  element_type ENUM('voyelle', 'consonne', 'syllabe', 'mot', 'phrase'),
  element_value VARCHAR(50),
  attempts INT DEFAULT 0,
  correct INT DEFAULT 0,
  status ENUM('nouveau', 'en_cours', 'difficile', 'maitrise') DEFAULT 'nouveau',
  last_seen TIMESTAMP NULL,
  UNIQUE KEY unique_element (element_type, element_value)
);

CREATE TABLE IF NOT EXISTS characters (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  image_path VARCHAR(255),
  is_active BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reward_phrases (
  id INT PRIMARY KEY AUTO_INCREMENT,
  phrase TEXT,
  is_active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Level locks (parent controls which levels are accessible)
CREATE TABLE IF NOT EXISTS level_locks (
  id INT PRIMARY KEY AUTO_INCREMENT,
  level_key VARCHAR(50) UNIQUE,
  is_locked BOOLEAN DEFAULT FALSE,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Postcards for Alia's mailbox
CREATE TABLE IF NOT EXISTS postcards (
  id INT PRIMARY KEY AUTO_INCREMENT,
  image_path VARCHAR(255),
  label VARCHAR(100),
  is_active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Mailbox — postcards earned by Alia
CREATE TABLE IF NOT EXISTS mailbox (
  id INT PRIMARY KEY AUTO_INCREMENT,
  postcard_id INT,
  earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  downloaded BOOLEAN DEFAULT FALSE,
  FOREIGN KEY (postcard_id) REFERENCES postcards(id)
);

-- Daily progress reports
CREATE TABLE IF NOT EXISTS daily_reports (
  id INT PRIMARY KEY AUTO_INCREMENT,
  report_date DATE UNIQUE,
  worked BOOLEAN DEFAULT FALSE,
  summary TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Default level locks (all unlocked)
INSERT IGNORE INTO level_locks (level_key, is_locked) VALUES
  ('voyelles', FALSE),
  ('consonnes_1', FALSE),
  ('lecture_rapide', FALSE),
  ('mots_simples', FALSE),
  ('phrases', FALSE);

-- Default characters
INSERT IGNORE INTO characters (name, image_path, is_active) VALUES
  ('Karumi', 'characters/karumi.png', TRUE),
  ('Cinnamon', 'characters/cinnamon.png', FALSE);

-- Default reward phrases
INSERT IGNORE INTO reward_phrases (phrase) VALUES
  ('Alia, je t\'aime !'),
  ('Alia, bravo, tu es incroyable !'),
  ('Alia, tu as travaillé super bien aujourd\'hui !'),
  ('Alia, je suis tellement fière de toi !'),
  ('Alia, tu es la meilleure !'),
  ('Alia, continue comme ça, tu es fantastique !');

-- Parent password (hashed)
CREATE TABLE IF NOT EXISTS parent_settings (
  id INT PRIMARY KEY AUTO_INCREMENT,
  setting_key VARCHAR(50) UNIQUE,
  setting_value TEXT
);
INSERT IGNORE INTO parent_settings (setting_key, setting_value)
VALUES ('password', 'maman');
