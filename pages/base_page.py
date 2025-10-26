# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException

class BasePage:
    
    def __init__(self, driver: WebDriver):
        """Hàm khởi tạo, thiết lập WebDriver và URL cơ sở."""
        self.driver = driver
        self.base_url = "https://viettien.vn/" 
    
    def go_to_url(self, url=""):
        """Điều hướng đến URL."""
        full_url = self.base_url + url
        self.driver.get(full_url)
        # Tùy chọn: Chờ trang tải hoàn toàn (hoặc chờ body xuất hiện)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def find_element(self, by_locator, timeout=10):
        """Tìm và chờ phần tử có mặt trong DOM (Presence)."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_locator))

    def click(self, by_locator):
        """Chờ phần tử có thể click được và thực hiện click."""
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        element.click()

    def send_keys(self, by_locator, text):
        """Điền giá trị vào phần tử."""
        element = self.find_element(by_locator)
        element.clear()
        element.send_keys(text)

    # 💡 PHƯƠNG THỨC GÂY LỖI TRƯỚC ĐÓ - ĐÃ ĐỊNH NGHĨA
    def get_text(self, by_locator):
        """Lấy văn bản từ phần tử sau khi chờ nó hiển thị."""
        return self.find_element(by_locator).text 

    # 💡 PHƯƠNG THỨC GÂY LỖI TRƯỚC ĐÓ - ĐÃ ĐỊNH NGHĨA
    def is_element_present(self, by_locator, timeout=5) -> bool:
        """Kiểm tra xem phần tử có hiển thị/có mặt trong DOM hay không (trả về True/False)."""
        try:
            self.find_element(by_locator, timeout=timeout)
            return True
        except TimeoutException:
            return False
        except Exception:
            return False