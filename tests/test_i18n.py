
import pytest
from modules import i18n

def test_i18n_loading():
    """Test that translations are loaded correctly"""
    i18n.load_translations()
    assert 'en' in i18n.TRANSLATIONS
    assert 'th' in i18n.TRANSLATIONS
    
    assert i18n.TRANSLATIONS['en']['Generate'] == 'Generate'
    assert i18n.TRANSLATIONS['th']['Generate'] == 'สร้างข้อความ'

def test_translation_function():
    """Test the t() function"""
    i18n.set_locale('en')
    assert i18n.t('Generate') == 'Generate'
    
    i18n.set_locale('th')
    assert i18n.t('Generate') == 'สร้างข้อความ'
    
    # Test fallback
    assert i18n.t('Unknown Key') == 'Unknown Key'
