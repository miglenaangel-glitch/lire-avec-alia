CREATE DATABASE IF NOT EXISTS lire_avec_alia CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE lire_avec_alia;

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
