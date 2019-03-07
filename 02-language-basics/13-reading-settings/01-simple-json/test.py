#DEMO: reading settings from a JSON file
from config import settings, dbsettings #custom module to read config/settings

print(f"db = {settings['db']['database']}")
#or
print(f"db = {dbsettings['database']}")
