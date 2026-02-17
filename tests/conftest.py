
import sys
import os
from pathlib import Path
import pytest

# Add project root to python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

@pytest.fixture(scope="session")
def mock_shared():
    """Mock shared module arguments to avoid loading actual models"""
    import modules.shared as shared
    
    # Mock args
    class MockArgs:
        model = "mock_model"
        lora = None
        model_dir = "models"
        lora_dir = "loras"
        api = False
        public_api = False
        nowebui = False
        multi_user = False
        headless = True
        verbose = False
        chat = True
        loader = "llama.cpp"
        
    shared.args = MockArgs()
    shared.settings = {
        'dark_theme': True,
        'show_controls': True,
        'start_with': '',
        'mode': 'chat',
        'chat_style': 'cai-chat',
        'instruction_template_str': '',
        'chat-instruct_command': '',
        'character': 'Assistant',
        'name1': 'You',
        'name2': 'Assistant',
        'context': 'This is a test context.',
        'greeting': 'Hello!',
        'user_bio': '',
        'custom_system_message': '',
        'chat_template_str': '',
        'instruction_template_str': '',
        'auto_max_new_tokens': False,
        'max_new_tokens': 200,
        'seed': -1,
        "default_extensions": []
    }
    
    return shared
