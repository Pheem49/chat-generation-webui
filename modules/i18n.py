
import json
import os
from pathlib import Path
from modules import shared

# Global localization state
LOCALE = 'en'
TRANSLATIONS = {}

def load_translations():
    """Load translation files from i18n directory"""
    global TRANSLATIONS
    i18n_path = Path(__file__).resolve().parent.parent / 'i18n'
    
    # Load all json files
    try:
        if i18n_path.exists():
            for file_path in i18n_path.glob('*.json'):
                lang_code = file_path.stem
                with open(file_path, 'r', encoding='utf-8') as f:
                    TRANSLATIONS[lang_code] = json.load(f)
    except Exception as e:
        print(f"Error loading translations: {e}")

def get_available_languages():
    """Get list of available language codes"""
    return list(TRANSLATIONS.keys()) if TRANSLATIONS else ['en']

def set_locale(locale):
    """Set the current locale"""
    global LOCALE
    if locale in TRANSLATIONS:
        LOCALE = locale
    else:
        print(f"Locale {locale} not found, falling back to 'en'")
        LOCALE = 'en'

def t(key):
    """Translate a key to the current locale"""
    if LOCALE not in TRANSLATIONS:
        return key
    
    return TRANSLATIONS[LOCALE].get(key, key)

# Initialize
load_translations()
