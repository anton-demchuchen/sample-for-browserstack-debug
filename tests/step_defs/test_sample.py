import time

from pytest_bdd import scenarios, given, when, then, parsers
import pytest

scenarios('../features/sample.feature')

@given("Open google page in a new browser tab")
def open_google_page(web_driver):
    web_driver.get("https://www.google.com")
    assert "Google" in web_driver.title, "Google page did not load correctly"
    time.sleep(3)
