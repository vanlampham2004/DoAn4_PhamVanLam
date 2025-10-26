# pages/search_page.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys

class SearchPage(BasePage):
    SEARCH_ICON = (By.XPATH, "//div[@class='header-search-fake']")
    SEARCH_INPUT = (By.XPATH, "//input[@id='txtSearchHeader']")
    PRODUCT_TITLES = (By.XPATH, "//a[contains(@class, 'product9-title')]")  # tất cả sản phẩm hiển thị

    def open_home(self, base_url: str):
        self.go_to_url()  # nếu base_url đã đúng trong BasePage
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.SEARCH_ICON)
        )



    def perform_search(self, keyword: str):
        input_el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_ICON)
        )
        input_el.click()
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ENTER)

    def get_product_names(self):
        """Trả về danh sách tên tất cả sản phẩm hiển thị sau khi tìm kiếm"""
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.PRODUCT_TITLES)
            )
            names = [el.text.strip() for el in elements if el.text.strip()]
            return names
        except TimeoutException:
            print("❌ Không tìm thấy sản phẩm nào.")
            return []
