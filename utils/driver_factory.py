# utils/driver_factory.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def get_driver(browser="chrome"):
    """
    Hàm khởi tạo WebDriver cho trình duyệt được chỉ định.
    Hỗ trợ: chrome, edge, firefox
    """
    browser = browser.lower()
    driver = None

    if browser == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"⚠️ Browser '{browser}' không được hỗ trợ!")

    # Thiết lập thời gian chờ ngầm định
    driver.implicitly_wait(10)
    return driver
