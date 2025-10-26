import pytest
import openpyxl
from pages.search_page import SearchPage

# ===== HÀM ĐỌC DỮ LIỆU EXCEL =====
def read_excel_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Bỏ dòng tiêu đề
        if row[0] and row[1]:
            data.append({"Keyword": row[0].strip(), "Expected": row[1].strip()})
    workbook.close()
    return data

excel_path = "data/Timkiemdata.xlsx"
search_data = read_excel_data(excel_path, "Timkiem")
base_url = "https://viettien.vn/"

# ===== TEST CASE =====
@pytest.mark.parametrize("data", search_data)
def test_search_products(driver, data):
    keyword = data["Keyword"]
    expected_products = [p.strip() for p in data["Expected"].split(",")]

    page = SearchPage(driver)
    page.open_home(base_url)
    page.perform_search(keyword)

    product_names = page.get_product_names()
    print(f"Từ khóa: {keyword}")
    print("Sản phẩm tìm thấy:", product_names)
    print("Sản phẩm mong muốn:", expected_products)

    # Kiểm tra tất cả sản phẩm mong muốn xuất hiện trong kết quả
    for p in expected_products:
        assert any(p.lower() in name.lower() for name in product_names), f"Không tìm thấy sản phẩm '{p}'"
