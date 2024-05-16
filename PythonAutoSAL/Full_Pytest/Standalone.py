from playwright.sync_api import Page, sync_playwright
import pytest
import logging

logger = logging.getLogger('___Tesst___')
logger.setLevel(logging.INFO)

@pytest.fixture(scope="function", autouse=True)
def set_up_page(page: Page):
    logger.info(msg="Open dev.saladin.vn")
    page.goto("https://dev.saladin.vn")
    #return page
    yield page
    logger.info(msg="Close Browser")
    page.close()

def test_Bike_TPL_PVI(set_up_page: Page):
    product_detail = "Bảo hiểm xe máy"
    insurer_detail = "PVI"

    # Homepage Saladin
    product_cat = set_up_page.get_by_title(product_detail)
    product_cat.click()

    # Landing page Bảo hiểm ô tô
    flow_mua = set_up_page.get_by_text("Mua ngay")
    flow_mua.click()

    # Page Thời hạn bảo hiểm
    # Chọn nhà cung cấp
    insurer = set_up_page.get_by_text(insurer_detail)
    insurer.click()
    # Click btn Điền thông tin
    btn_Dienthongtin = set_up_page.get_by_text("Điền thông tin")
    btn_Dienthongtin.click()

    # Page Điền thông tin
    # Click icon meo meo
    icon_meow = set_up_page.get_by_title("Meow meow")
    icon_meow.click()
    # Click btn Hoàn tất
    btn_Hoantat = set_up_page.get_by_text("Hoàn tất")
    btn_Hoantat.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    btn_Tienhanhthanhtoan = set_up_page.get_by_role("button", name="Tiến hành thanh toán")
    btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Chọn thanh toán thẻ nội địa
    payment_thenoidia = set_up_page.get_by_title("Thẻ Nội Địa")
    payment_thenoidia.click()
    # Click Xác nhận
    btn_Xacnhan = set_up_page.get_by_role("button", name="Xác nhận")
    btn_Xacnhan.click()

    # Page Onepay Thẻ nội địa
    # Chọn ABBANK
    bank_ABBANK = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div.bank-list > div > div:nth-child(17) > a > div > img")
    bank_ABBANK.click()
    # Nhập thông tin thẻ
    card_number = set_up_page.locator("#card_number")
    card_number.fill("9704250000000001")
    issue_date = set_up_page.locator("#exp_date")
    issue_date.fill("0113")
    card_name = set_up_page.locator("#card_name")
    card_name.fill("NGUYEN VAN A")

    btn_Thanhtoan = set_up_page.locator("#domescard-radio > div > domescard-main > div > div > div > app-vietcombank > form.ng-touched.ng-dirty.ng-invalid > div.nd-bank-card > div.action > button")
    btn_Thanhtoan.click()

    input_otp = set_up_page.locator("#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.nd-form-input > div > input")
    input_otp.fill("123456")

    btn_ThanhtoanOTP = set_up_page.locator("#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.action > div > button")
    btn_ThanhtoanOTP.click()

    result_payment = set_up_page.locator("//div[@class='mt-[20px] mb-[4px] px-[16px] text-[20px] text-on-surface-dark-high-emphasis']")
    assert "Bạn đã thanh toán và xuất hợp đồng thành công" in result_payment.text_content()

def test_Bike_TPL_VNI(set_up_page: Page):
    product_detail = "Bảo hiểm xe máy"
    insurer_detail = "VNI"

    # Homepage Saladin
    product_cat = set_up_page.get_by_title(product_detail)
    product_cat.click()

    # Landing page Bảo hiểm ô tô
    flow_mua = set_up_page.get_by_text("Mua ngay")
    flow_mua.click()

    # Page Thời hạn bảo hiểm
    # Chọn nhà cung cấp
    insurer = set_up_page.get_by_text(insurer_detail)
    insurer.click()
    # Click btn Điền thông tin
    btn_Dienthongtin = set_up_page.get_by_text("Điền thông tin")
    btn_Dienthongtin.click()

    # Page Điền thông tin
    # Click icon meo meo
    icon_meow = set_up_page.get_by_title("Meow meow")
    icon_meow.click()
    # Click btn Hoàn tất
    btn_Hoantat = set_up_page.get_by_text("Hoàn tất")
    btn_Hoantat.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    btn_Tienhanhthanhtoan = set_up_page.get_by_role("button", name="Tiến hành thanh toán")
    btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Chọn thanh toán thẻ nội địa
    payment_thenoidia = set_up_page.get_by_title("Thẻ Nội Địa")
    payment_thenoidia.click()
    # Click Xác nhận
    btn_Xacnhan = set_up_page.get_by_role("button", name="Xác nhận")
    btn_Xacnhan.click()

    # Page Onepay Thẻ nội địa
    # Chọn ABBANK
    bank_ABBANK = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div.bank-list > div > div:nth-child(17) > a > div > img")
    bank_ABBANK.click()
    # Nhập thông tin thẻ
    card_number = set_up_page.locator("#card_number")
    card_number.fill("9704250000000001")
    issue_date = set_up_page.locator("#exp_date")
    issue_date.fill("0113")
    card_name = set_up_page.locator("#card_name")
    card_name.fill("NGUYEN VAN A")

    btn_Thanhtoan = set_up_page.locator("#domescard-radio > div > domescard-main > div > div > div > app-vietcombank > form.ng-touched.ng-dirty.ng-invalid > div.nd-bank-card > div.action > button")
    btn_Thanhtoan.click()

    input_otp = set_up_page.locator("#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.nd-form-input > div > input")
    input_otp.fill("123456")

    btn_ThanhtoanOTP = set_up_page.locator("#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.action > div > button")
    btn_ThanhtoanOTP.click()

    result_payment = set_up_page.locator("//div[@class='mt-[20px] mb-[4px] px-[16px] text-[20px] text-on-surface-dark-high-emphasis']")
    assert "Bạn đã thanh toán và xuất hợp đồng thành công" in result_payment.text_content()

def test_Bike_TPL_BaoMinh(set_up_page: Page):
    product_detail = "Bảo hiểm xe máy"
    insurer_detail = "Bảo Minh"

    # Homepage Saladin
    product_cat = set_up_page.get_by_title(product_detail)
    product_cat.click()

    # Landing page Bảo hiểm ô tô
    flow_mua = set_up_page.get_by_text("Mua ngay")
    flow_mua.click()

    # Page Thời hạn bảo hiểm
    # Chọn nhà cung cấp
    insurer = set_up_page.get_by_text(insurer_detail)
    insurer.click()
    # Click btn Điền thông tin
    btn_Dienthongtin = set_up_page.get_by_text("Điền thông tin")
    btn_Dienthongtin.click()

    # Page Điền thông tin
    # Click icon meo meo
    icon_meow = set_up_page.get_by_title("Meow meow")
    icon_meow.click()
    # Click btn Hoàn tất
    btn_Hoantat = set_up_page.get_by_text("Hoàn tất")
    btn_Hoantat.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    btn_Tienhanhthanhtoan = set_up_page.get_by_role("button", name="Tiến hành thanh toán")
    btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Chọn thanh toán thẻ nội địa
    payment_thenoidia = set_up_page.get_by_title("Thẻ Nội Địa")
    payment_thenoidia.click()
    # Click Xác nhận
    btn_Xacnhan = set_up_page.get_by_role("button", name="Xác nhận")
    btn_Xacnhan.click()

    # Page Onepay Thẻ nội địa
    # Chọn ABBANK
    bank_ABBANK = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div.bank-list > div > div:nth-child(17) > a > div > img")
    bank_ABBANK.click()
    # Nhập thông tin thẻ
    card_number = set_up_page.locator("#card_number")
    card_number.fill("9704250000000001")
    issue_date = set_up_page.locator("#exp_date")
    issue_date.fill("0113")
    card_name = set_up_page.locator("#card_name")
    card_name.fill("NGUYEN VAN A")

    btn_Thanhtoan = set_up_page.locator("#domescard-radio > div > domescard-main > div > div > div > app-vietcombank > form.ng-touched.ng-dirty.ng-invalid > div.nd-bank-card > div.action > button")
    btn_Thanhtoan.click()

    input_otp = set_up_page.locator("#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.nd-form-input > div > input")
    input_otp.fill("123456")

    btn_ThanhtoanOTP = set_up_page.locator("#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.action > div > button")
    btn_ThanhtoanOTP.click()

    result_payment = set_up_page.locator("//div[@class='mt-[20px] mb-[4px] px-[16px] text-[20px] text-on-surface-dark-high-emphasis']")
    assert "Bạn đã thanh toán và xuất hợp đồng thành công" in result_payment.text_content()