import pytest

@pytest.fixture(scope="function")
def dropdown_page(page, config):
    page.goto(config["base_url"] + "/dropdown")
    yield page