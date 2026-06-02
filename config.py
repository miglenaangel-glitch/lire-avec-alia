import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-in-prod')
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'lire_avec_alia')
    CLAUDE_MODEL = 'claude-sonnet-4-20250514'
    CLAUDE_MAX_TOKENS = 1000
    REWARD_MIN_ACCURACY = 0.70
