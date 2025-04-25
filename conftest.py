from datetime import datetime
import getpass
import platform
from pytest_metadata.plugin import metadata_key
import pytest
from playwright.sync_api import sync_playwright


def pytest_configure(config):
    config.stash[metadata_key]["Datetime"] = str(datetime.now())
    config.stash[metadata_key]["Designer"] = 'Tester'
    config.stash[metadata_key]["Test Type"] = 'Automated'
    config.stash[metadata_key]["Tester"] = getpass.getuser()
    config.stash[metadata_key]["Environment"] = 'TEST'
    config.stash[metadata_key]["System Version"] = platform.platform()


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000, args=['--start-maximized'])
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()

