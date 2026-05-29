"""
Day 10: JSON Config Manager
Concept: Loading and saving configuration dictionaries using the 'json' module.
"""

import json

config_file = "settings.json"

# 1. Dictionary to be saved as JSON
app_settings = {
    "app_name": "Python Daily Tracker",
    "version": "1.0.0",
    "theme": "Dark",
    "notifications": True,
    "user_prefs": {
        "auto_save": True,
        "backup_interval": 3600
    }
}

# 2. Writing JSON to a file (Serialization)
with open(config_file, "w") as f:
    json.dump(app_settings, f, indent=4)

print(f"Configuration saved to {config_file}")

# 3. Reading JSON from a file (Deserialization)
with open(config_file, "r") as f:
    loaded_config = json.load(f)

print("\nLoaded Settings:")
print(f"App Name: {loaded_config['app_name']}")
print(f"Theme: {loaded_config.get('theme')}")
print(f"Auto-Save: {loaded_config['user_prefs']['auto_save']}")
