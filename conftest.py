# conftest.py

import pytest
from utils.driver_factory import get_driver # Đảm bảo import này đúng

# ...

@pytest.fixture(scope="function")
def driver(request):
    # Lấy tùy chọn trình duyệt (hoặc mặc định là chrome)
    browser = request.config.getoption("--browser", default="chrome") 

    web_driver = get_driver(browser)
    yield web_driver
    # Dọn dẹp
    web_driver.quit()

# Cần thiết nếu bạn dùng tùy chọn --browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Trình duyệt để chạy test"
    )