import pytest
import yaml
import allure

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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            # Attach screenshot
            allure.attach(
                page.screenshot(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            # Attach console logs
            logs = "\n".join([f"{msg.type}: {msg.text}" for msg in page.context.on("console")])
            allure.attach(
                logs,
                name="console logs",
                attachment_type=allure.attachment_type.TEXT
            )