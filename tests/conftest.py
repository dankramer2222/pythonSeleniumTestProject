import pytest
from selenium import webdriver


# @pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Создание драйвера {browser}")

    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Ожидался 'chrome' или 'firefox', но получено {browser}")

    my_driver.maximize_window()
    my_driver.get("https://practicetestautomation.com/practice-test-login/")
    my_driver.implicitly_wait(10)
    yield my_driver

    print(f"Закрытие драйвера {browser}")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )
