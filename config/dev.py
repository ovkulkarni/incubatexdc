import os

APP_NAME = "IncubateX DC Project"
SECRET_KEY = "key"
DB_PATH = "database.db"
ENVIRONMENT = "dev"
DISPLAY_DEBUG_INFO = "False"
TEMPLATES_AUTO_RELOAD = True
FB_APP_ID = os.getenv("FB_APP_ID", "")
FB_APP_SECRET = os.getenv("FB_APP_SECRET", "")
