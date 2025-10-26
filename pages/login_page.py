from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # locators
        self.icon_login = "//div[@class='btn-account-management']//i[@class='icon icon-user']"
        self.login_button_header = "//div[@onclick='handleHeaderLogin();']"
        self.phone_input = "//input[@id='txtPhoneLogin']"
        self.password_input = "//input[@id='txtPassLogin']"
        self.login_button = "//button[contains(text(),'Đăng nhập')]"
        self.popup_title = "//h6[contains(@class,'stitle')]"
        self.user_icon = "//i[@class='icon icon-user']"
        self.user_name_header = "//div[@class='header-middle-right']//li[1]"

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def open_login_form(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.icon_login))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button_header))).click()

    def login(self, phone, password):
        wait = WebDriverWait(self.driver, 15)
        phone_input = wait.until(EC.presence_of_element_located((By.XPATH, self.phone_input)))
        phone_input.clear()
        phone_input.send_keys(phone)

        password_input = self.driver.find_element(By.XPATH, self.password_input)
        password_input.clear()
        password_input.send_keys(password)

        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(2)  # chờ popup hiển thị

    def get_popup_title(self, timeout=5):
        """Lấy title của popup Notification! nếu có"""
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                el = self.driver.find_element(By.XPATH, self.popup_title)
                text = el.text.strip()
                if text:
                    return text
            except:
                pass
            time.sleep(0.2)
        return ""

    def get_user_name_from_header(self, timeout=5):
        """Click vào icon user, lấy text tên hiển thị ở header"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.element_to_be_clickable((By.XPATH, self.user_icon))).click()
            name_el = wait.until(EC.visibility_of_element_located((By.XPATH, self.user_name_header)))
            return name_el.text.strip()
        except:
            return ""

    def get_login_result(self):
        """Ưu tiên popup, nếu thành công fallback lấy tên user từ header"""
        popup = self.get_popup_title()
        if popup:
            if "thành công" in popup.lower():
                # login thành công → lấy tên từ header
                user_name = self.get_user_name_from_header()
                return user_name or popup
            else:
                return popup
        else:
            # fallback khi popup không hiện
            return self.get_user_name_from_header() or ""
