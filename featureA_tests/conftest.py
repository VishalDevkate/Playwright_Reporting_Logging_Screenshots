import pytest

@pytest.fixture(scope="function")
def login_user(page, config):
    page.goto(config["base_url"] + "/login")
    page.fill("#username", config["username"])
    page.fill("#password", config["password"])
    page.click("button[type='submit']")
    yield page