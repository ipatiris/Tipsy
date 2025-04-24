import os

CONFIG_FILE = "pump_config.json"
COCKTAILS_FILE = "cocktails.json"
LOGO_FOLDER = "drink_logos"

try:
    OZ_COEFFICIENT = float(os.getenv("ONE_OZ_COEFFICIENT", "8"))
except ValueError:
    OZ_COEFFICIENT = 8.0