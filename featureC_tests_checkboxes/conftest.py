import pytest

@pytest.fixture(scope="function")
def checkbox_page(page, config):
    page.goto(config["base_url"] + "/checkboxes")
    yield page