import pytest
from utils.driver_factory import get_driver
from utils.excel_reader import excel_reader
from pages.register_page import RegisterPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

register_data = excel_reader(r"F:\DoAn4\data\Timkiemdata.xlsx", sheet_name="Đăng ký")

@pytest.mark.parametrize("data", register_data)
def test_register_invalid(driver, data):
    page = RegisterPage(driver)
    page.open()
    page.open_register_form()
    page.fill_register_form(
        fullname=data["FullName"],
        email=data["Email"],
        phone=data["Phone"],
        password=data["Password"],
        repassword=data["RePassword"],
        agree=data["AgreeTerm"]
    )
    page.submit()
    message = page.get_alert_message()

    print("\n----------------------------------")
    print(f"FullName   : {data['FullName']}")
    print(f"Email      : {data['Email']}")
    print(f"Phone      : {data['Phone']}")
    print(f"Password   : {data['Password']}")
    print(f"RePassword : {data['RePassword']}")
    print(f"Expected   : {data['ExpectedResult']}")
    print(f"Actual     : {message}")

    result = "PASS" if data["ExpectedResult"] in message else "FAIL"
    print(f"Result     : {result}")
    print("----------------------------------\n")

    assert data["ExpectedResult"] in message, (
        f"Mong đợi: {data['ExpectedResult']}\nThực tế: {message}"
    )
