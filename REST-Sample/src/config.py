# we can use various ways to read config files
# in order to make it simple, we use built-in "json" module to read json file

import json  # to read json file

with open('config.json') as f:
    settings = json.load(f)  # "settings" contain all json parsed

# "dbsettings" -> subset of "settings" (just for "db")
dbsettings = settings["db"]
