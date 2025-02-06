# Overlaying production
from cvat.settings.production import *

UI_SCHEME = os.environ.get("UI_SCHEME", "http")
UI_HOST = os.environ.get("UI_HOST", "localhost")
UI_URL = "{}://{}".format(UI_SCHEME, UI_HOST)
CSRF_TRUSTED_ORIGINS = [UI_URL]
