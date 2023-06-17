import json

default_settings = {
    "placeholder": "_",
    "min_len": 0,
    "max_len": 100,
    "max_tries": 10,
    "hints": True
}

settings_file = "settings.json"
with open(settings_file, 'w') as f:
    json.dump(default_settings, f)

print("Resetted back to default settings")
input("Press ENTER to continue ")
