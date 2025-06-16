from idlelib.browser import file_open

import pytest
import json
from web_driver import WebDriver

@pytest.fixture(scope='session')
def config():
    file_name = 'config.json'
    try:
        with open(file_name, 'r') as file:
            config = json.load(file)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error reading JSON file '{file_name}': {e}")


    assert config['browser'] in ['firefox', 'chrome', 'headless firefox', 'headless chrome', 'safari']
    assert config['platform'] in ['desktop', 'mobile', 'ios', 'android']
    assert isinstance(config['timeout'], int)
    assert config['environment'] in ['local', 'dev', 'prod']
    assert config['experiment'] in ['enrollment_hycs_v1', 'enrollment_hycs_v2']
    assert config['timeout'] > 0
    assert config['loglevel'] in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    assert config['device'] in ['simulator', 'real device']
    assert isinstance(config['appium_port'], int)
    return config

@pytest.fixture
def web_driver(config):
    web_driver = WebDriver.setup_driver(config)
    # web_driver = webdriver.Chrome()
    yield web_driver
    web_driver.quit()
