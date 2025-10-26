import pytest
from utils.driver_factory import get_driver
from utils.excel_reader import excel_reader
from pages.login_page import LoginPage
import time

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

# Đường dẫn tới file Excel và sheet chứa dữ liệu login
excel_path = r"F:\DoAn4\data\Timkiemdata.xlsx"
sheet_name = "Đăng nhập"
login_data = excel_reader(excel_path, sheet_name=sheet_name)

@pytest.mark.parametrize("data", login_data)
def test_login(driver, data):
    """
    Test login dựa trên:
    - Login thành công → lấy tên user từ header
    - Login thất bại → lấy popup Notification!
    """
    page = LoginPage(driver)
    page.open_url("https://viettien.vn/")
    page.open_login_form()
    page.login(data["Phone"], data["Password"])

    # Lấy kết quả login
    actual_result = page.get_login_result()

    # So sánh với ExpectedResult trong Excel
    expected_result = data.get("ExpectedResult", "").strip()
    test_pass = expected_result.lower() in actual_result.lower()

    # In log chi tiết
    print("\n----------------------------")
    print(f"Phone          : {data.get('Phone')}")
    print(f"Password       : {data.get('Password')}")
    print(f"ExpectedResult : {expected_result}")
    print(f"ActualResult   : {actual_result}")
    print(f"Result         : {'PASS' if test_pass else 'FAIL'}")
    print("----------------------------\n")

    # Assert để test fail nếu không khớp
    assert test_pass, f"Expected: {expected_result} | Actual: {actual_result}"
