from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://viettien.vn/"
        # Các phần tử
        self.icon_account = "//div[@class='btn-account-management']//i[@class='icon icon-user']"
        self.register_menu = "//div[@onclick='handleHeaderRegister();']"
        self.name_input = "//input[@id='txtFullNameRegister']"
        self.email_input = "//input[@id='txtEmailRegister']"
        self.phone_input = "//input[@id='txtPhoneRegister']"
        self.password_input = "//input[@id='txtPassRegister']"
        self.repassword_input = "//input[@id='txtRePassRegister']"
        self.agree_checkbox = "//input[@id='chkTermRegister']"
        self.register_button = "//button[contains(text(),'Đăng Ký')]"
        # Thông báo có thể ở alert hoặc span ẩn
        self.alert_message = "//div[contains(@class,'alert') or @id='lblError']"
        self.hidden_error_message = "//span[@class='not-visible is-visible']"

    # 🟢 Mở trang
    def open(self):
        self.driver.get(self.url)

    # 🟢 Bước 1: Mở form đăng ký
    def open_register_form(self):
        wait = WebDriverWait(self.driver, 10)
        icon = wait.until(EC.element_to_be_clickable((By.XPATH, self.icon_account)))
        icon.click()
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, self.register_menu)))
        menu.click()

    # 🟢 Bước 2: Điền form
    def fill_register_form(self, fullname, email, phone, password, repassword, agree):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.name_input)))

        # điền dữ liệu nếu có
        if fullname:
            self.driver.find_element(By.XPATH, self.name_input).send_keys(fullname)
        if email:
            self.driver.find_element(By.XPATH, self.email_input).send_keys(email)
        if phone:
            self.driver.find_element(By.XPATH, self.phone_input).send_keys(phone)
        if password:
            self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        if repassword:
            self.driver.find_element(By.XPATH, self.repassword_input).send_keys(repassword)
        if agree.lower() == "có":
            checkbox = self.driver.find_element(By.XPATH, self.agree_checkbox)
            if not checkbox.is_selected():
                checkbox.click()

    # 🟢 Bước 3: Nhấn nút “Đăng Ký”
    def submit(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.register_button))
        )
        btn.click()

    # 🟢 Lấy thông báo lỗi hoặc thông báo hệ thống
    def get_alert_message(self):
        wait = WebDriverWait(self.driver, 5)
        message = ""

        # 1️⃣ Thử tìm alert thông thường
        try:
            alert = wait.until(EC.presence_of_element_located((By.XPATH, self.alert_message)))
            if alert.is_displayed():
                message = alert.text.strip()
        except:
            pass

        # 2️⃣ Nếu không có alert, thử tìm span lỗi ẩn
        if not message:
            try:
                hidden_error = wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.hidden_error_message))
                )
                if hidden_error:
                    message = hidden_error.text.strip()
            except:
                pass

        # 3️⃣ Nếu vẫn không có gì → trả về mặc định
        if not message:
            message = "Không có thông báo lỗi hiển thị"

        return message
