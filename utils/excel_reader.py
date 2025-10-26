import openpyxl

def excel_reader(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path, data_only=True)
    sheet = workbook[sheet_name]
    data = []

    # Lấy hàng tiêu đề (Case, Phone, Password, ExpectedResult)
    headers = [cell.value for cell in sheet[1]]

    # Duyệt từ hàng 2 trở đi
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = {}

        for key, value in zip(headers, row):
            if value is None:
                row_data[key] = ""
            else:
                # Ép tất cả về chuỗi để giữ nguyên dữ liệu
                value_str = str(value).strip()

                # Xử lý riêng cột Phone (đề phòng bị mất số 0)
                if key.lower() == "phone":
                    # Nếu Excel đọc thành số dạng float (986096064.0)
                    value_str = value_str.replace(".0", "")
                    # Nếu bị mất số 0 đầu, thêm lại
                    if len(value_str) == 9 and not value_str.startswith("0"):
                        value_str = "0" + value_str

                row_data[key] = value_str

        data.append(row_data)

    return data
