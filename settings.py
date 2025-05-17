import os
from dotenv import load_dotenv


load_dotenv()


CONFIG_FILE = "pump_config.json"
COCKTAILS_FILE = "cocktails.json"
LOGO_FOLDER = "drink_logos"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

try:
    OZ_COEFFICIENT = float(os.getenv("OZ_COEFFICIENT", "8"))
except ValueError:
    OZ_COEFFICIENT = 8.0

INVERT_PUMP_PINS = os.getenv('INVERT_PUMP_PINS', 'false') == 'true'
PUMP_CONCURRENCY = int(os.getenv('PUMP_CONCURRENCY', 3))
FULL_SCREEN = os.getenv('FULL_SCREEN', 'true') == 'true'
SHOW_RELOAD_COCKTAILS_BUTTON = os.getenv('SHOW_RELOAD_COCKTAILS_BUTTON', 'false') == 'true'
RELOAD_COCKTAILS_TIMEOUT = int(os.getenv('RELOAD_COCKTAILS_TIMEOUT', 0))