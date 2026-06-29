from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASE_URL = "sqlite:///./raizes.db"

API_TITLE = "Raízes do Nordeste API"
API_VERSION = "1.0.0"

SECRET_KEY = "raizes-do-nordeste-2026"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60