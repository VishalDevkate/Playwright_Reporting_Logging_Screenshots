import pytest
import yaml

def load_config(env="qa"):
    with open("config.yaml") as f:
        data = yaml.safe_load(f)
    return data["environments"][env]

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")

@pytest.fixture(scope="session")
def config(pytestconfig):
    env = pytestconfig.getoption("--env")
    return load_config(env)

@pytest.fixture(scope="session")
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()