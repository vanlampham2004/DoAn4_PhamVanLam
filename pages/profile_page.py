import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage:
    def __init__(self, driver, base_url="https://viettien.vn/"):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.base_url = base_url.rstrip("/") + "/"

        # login header
        self.icon_account = (By.XPATH, "//div[@class='btn-account-management']//i[@class='icon icon-user']")
        self.login_menu = (By.XPATH, "//div[@onclick='handleHeaderLogin();']")

        # login modal
        self.phone_input = (By.XPATH, "//input[@id='txtPhoneLogin']")
        self.pass_input = (By.XPATH, "//input[@id='txtPassLogin']")
        self.login_button = (By.XPATH, "//button[contains(text(),'Đăng nhập')]")

        # account page
        self.account_url = self.base_url + "quan-ly-tai-khoan/"
        self.fullname_input = (By.XPATH, "//*[@id='txtFullName']")
        self.email_input = (By.XPATH, "//*[@id='txtEmail']")
        self.address_input = (By.XPATH, "//*[@id='txtAddress']")
        self.update_button = (By.XPATH, "//button[contains(text(),'Cập nhật')]")

        # popup title
        self.popup_title = (By.XPATH, "//h6[contains(@class, 'stitle')]")

    def open_home(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def open_login_form(self):
        icon = self.wait.until(EC.element_to_be_clickable(self.icon_account))
        icon.click()
        menu = self.wait.until(EC.element_to_be_clickable(self.login_menu))
        menu.click()

    def login(self, phone, password):
        try:
            self.open_login_form()
            phone_el = self.wait.until(EC.visibility_of_element_located(self.phone_input))
            phone_el.clear()
            phone_el.send_keys(phone)
            self.driver.find_element(*self.pass_input).clear()
            self.driver.find_element(*self.pass_input).send_keys(password)
            self.driver.find_element(*self.login_button).click()
            time.sleep(3)
        except Exception:
            self.driver.get(self.base_url + "dang-nhap/")
            time.sleep(1)
            self.wait.until(EC.visibility_of_element_located(self.phone_input)).send_keys(phone)
            self.driver.find_element(*self.pass_input).send_keys(password)
            self.driver.find_element(*self.login_button).click()
            time.sleep(3)

    def open_account_page(self):
        self.driver.get(self.account_url)
        self.wait.until(EC.visibility_of_element_located(self.fullname_input))

    def update_account(self, fullname="", email="", address=""):
        if fullname:
            el = self.wait.until(EC.visibility_of_element_located(self.fullname_input))
            el.clear()
            el.send_keys(fullname)
        if email:
            el = self.driver.find_element(*self.email_input)
            el.clear()
            el.send_keys(email)
        if address:
            el = self.driver.find_element(*self.address_input)
            el.clear()
            el.send_keys(address)

        # click Cập nhật
        self.driver.find_element(*self.update_button).click()
        time.sleep(1)

    def get_popup_title(self):
        try:
            title_el = self.wait.until(EC.visibility_of_element_located(self.popup_title))
            return title_el.text.strip()
        except:
            return ""
