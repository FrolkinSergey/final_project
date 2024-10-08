import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOption
from selenium.webdriver.safari.options import Options as SafariOption


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox", "safari"])
    parser.addoption("--remote", default="true", choices=["false", "true"])
    parser.addoption("--panel", default="client", choices=["client", "adm"])
    parser.addoption("--stand", default="dev", choices=["dev", "test", "pre"])
    parser.addoption("--url", default=f"192.168.0.100")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv", default="124.0")
    parser.addoption("--component_id", default=1000)
    parser.addoption("--employee", default="severus_snape@rt.ru")
    parser.addoption("--login_type", default="local", choices=["local", "sso"])


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


@pytest.fixture()
def base_url(request):
    panel = request.config.getoption("--panel")
    stand = request.config.getoption("--stand")
    base_url = f"https://{panel}.{stand}.ru/"
    return base_url


@pytest.fixture()
def browser(request, base_url):
    browser_name = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    # remote = request.config.getoption("--remote")
    url = request.config.getoption("--url")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")

    executor_url = f"http://{url}:4444/wd/hub"

    logger = logging.getLogger(request.node.name)
    ch = logging.FileHandler(filename=f"tests/logs/{request.node.name}.log")
    ch.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.setLevel(level=log_level)
    logger.addHandler(ch)

    if browser_name == "chrome":
        options = ChromeOptions()
    elif browser_name == "firefox":
        options = FirefoxOption()
    elif browser_name == "safari":
        options = SafariOption()
    else:
        raise ValueError(f"Browser {browser_name} not supported")

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "name": request.node.name,
            "screenResolution": "1280x720",
            "enableVideo": video,
            "enableLog": logs,
            "sessionTimeout": "30m"
        },
        "acceptInsecureCerts": True,
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    # if remote == "false":
    #     if browser_name == "chrome":
    #         driver = webdriver.Chrome(options=options)
    #     elif browser_name == "safari":
    #         driver = webdriver.Safari()
    #     else:
    #         raise ValueError(f"Browser {browser_name} not supported local run")
    # elif remote == "true":
    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )

    driver.maximize_window()

    driver.get(base_url)
    driver.url = base_url

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    yield driver

    if request.node.status == 'failed':
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )

    driver.quit()


@pytest.fixture
def stand(request):
    stand = request.config.getoption("--stand")
    return stand


@pytest.fixture
def login_type(request):
    return request.config.getoption("--login_type")


@pytest.fixture
def base_esb_api_url(request):
    stand = request.config.getoption("--stand")
    if stand == 'dev':
        base_esb_api_url = "http://ip:9999"
        return base_esb_api_url
    elif stand == 'test':
        base_esb_api_url = "http://ip:9999"
        return base_esb_api_url
    elif stand == 'pre':
        base_esb_api_url = "http://ip:9999"
        return base_esb_api_url
    else:
        pass


@pytest.fixture
def headers(request):
    component_id = request.config.getoption("--component_id")
    employee = request.config.getoption("--employee")
    headers = {"Content-Type": "application/json", "X-CallerID": f"{component_id}", "X-employee": f"{employee}"}
    return headers
