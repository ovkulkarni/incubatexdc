import os

APP_NAME = "IncubateX DC Project"
SECRET_KEY = "key"
DB_PATH = "database.db"
DISPLAY_DEBUG_INFO = True
ENVIRONMENT = "dev"
TEMPLATES_AUTO_RELOAD = True
FB_APP_ID = os.getenv("FB_APP_ID", "")
FB_APP_SECRET = os.getenv("FB_APP_SECRET", "")
