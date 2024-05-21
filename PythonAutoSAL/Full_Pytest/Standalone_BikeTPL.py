from playwright.sync_api import Page, sync_playwright, Locator, expect
import pytest
import logging

logger = logging.getLogger('___Test___')
logger.setLevel(logging.INFO)

@pytest.fixture
def set_up_page(page: Page):
    logger.info(msg="Open dev.saladin.vn")
    page.goto("https://dev.saladin.vn")
    # return page
    yield page
    logger.info(msg="Close Browser")
    page.close()

@pytest.fixture
def set_up_page_admin(page: Page):
    logger.info(msg="Open dev-admin.saladin.vn")
    page.goto("https://dev-admin.saladin.vn/login")
    logger.info(msg="Input account")
    textbox_email = page.locator("//input[@name='email']")
    textbox_email.fill('saladin_writer@tenxtenx.com')
    textbox_password = page.locator("//input[@name='password']")
    textbox_password.fill("123456")
    btn_Dangnhap = page.get_by_role("button", name="Đăng nhập")
    btn_Dangnhap.click()
    
def old_order_management(set_up_page_admin: Page) -> object:
    # menu BH thông thường
    set_up_page_admin.locator("//span[@class='mantine-Text-root mantine-NavLink-label mantine-1w1oj6o' and contains(text(), 'BH thông thường')]").click()
    # menu đơn hàng
    old_order = set_up_page_admin.locator("//span[@class='mantine-Text-root mantine-NavLink-label mantine-1w1oj6o' and contains(text(), 'Đơn hàng')]")
    old_order.click()
    # filter sản phẩm
    set_up_page_admin.locator("//*[@id='mantine-vbvq00933']").click()
    filter_bikeTPL = set_up_page_admin.locator("//*[@id='mantine-vbvq00933-5']")
    filter_bikeTPL.click()

#@pytest.fixture(scope="function", autouse=True)
#def payment_provider(set_up_page: Page):

def test_Bike_TPL_PVI(set_up_page: set_up_page_admin):
    product_detail = "Bảo hiểm xe máy"
    insurer_detail = "PVI"

    # Homepage Saladin
    logger.info(msg="Choose product cats")
    product_cat = set_up_page.get_by_title(product_detail)
    product_cat.click()

    # Landing page Bảo hiểm ô tô
    logger.info(msg="Open landing page")
    flow_mua = set_up_page.get_by_text("Mua ngay")
    flow_mua.click()

    # Page Thời hạn bảo hiểm
    # Chọn nhà cung cấp
    logger.info(msg="Choose insurer PVI")
    insurer = set_up_page.get_by_text(insurer_detail)
    insurer.click()
    # Click btn Điền thông tin
    btn_dienthongtin = set_up_page.get_by_text("Điền thông tin")
    btn_dienthongtin.click()

    # Page Điền thông tin
    # Click icon meo meo
    logger.info(msg="Input random buyer information")
    icon_meow = set_up_page.get_by_title("Meow meow")
    icon_meow.click()
    # Click btn Hoàn tất
    btn_hoantat = set_up_page.get_by_text("Hoàn tất")
    btn_hoantat.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    logger.info(msg="Review order")
    btn_Tienhanhthanhtoan = set_up_page.get_by_role("button", name="Tiến hành thanh toán")
    btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Chọn thanh toán thẻ nội địa
    logger.info(msg="Review payment")
    payment_thenoidia = set_up_page.get_by_title("Thẻ Nội Địa")
    payment_thenoidia.click()
    # Click Xác nhận
    btn_xacnhan = set_up_page.get_by_role("button", name="Thanh toán")
    btn_xacnhan.click()

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

    btn_Thanhtoan = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div > app-vietcombank > form.ng-touched.ng-dirty.ng-invalid > div.nd-bank-card > div.action > button")
    btn_Thanhtoan.click()

    input_otp = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.nd-form-input > div > input")
    input_otp.fill("123456")

    btn_ThanhtoanOTP = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.action > div > button")
    btn_ThanhtoanOTP.click()


    #return set_up_page.url
    logger.info(msg="Payment success")
    result_payment = set_up_page.wait_for_selector("//div[@class='text-nds-para-small font-semibold sm:text-nds-desktop-h6']")
    expect_result: str = "Thanh toán thành công"
    assert expect_result in result_payment.text_content()

    #old_order_management()

def test_Bike_TPL_VNI(set_up_page: Page):
    product_detail = "Bảo hiểm xe máy"
    insurer_detail = "VNI"

    # Homepage Saladin
    logger.info(msg="Choose product cats")
    product_cat = set_up_page.get_by_title(product_detail)
    product_cat.click()

    # Landing page Bảo hiểm ô tô
    logger.info(msg="Open landing page")
    flow_mua = set_up_page.get_by_text("Mua ngay")
    flow_mua.click()

    # Page Thời hạn bảo hiểm
    # Chọn nhà cung cấp
    logger.info(msg="Choose insurer VNI")
    insurer = set_up_page.get_by_text(insurer_detail)
    insurer.click()
    # Click btn Điền thông tin
    btn_dienthongtin = set_up_page.get_by_text("Điền thông tin")
    btn_dienthongtin.click()

    # Page Điền thông tin
    # Click icon meo meo
    logger.info(msg="Input random buyer information")
    icon_meow = set_up_page.get_by_title("Meow meow")
    icon_meow.click()
    # Click btn Hoàn tất
    btn_hoantat = set_up_page.get_by_text("Hoàn tất")
    btn_hoantat.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    logger.info(msg="Review order")
    btn_Tienhanhthanhtoan = set_up_page.get_by_role("button", name="Tiến hành thanh toán")
    btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Chọn thanh toán thẻ nội địa
    logger.info(msg="Review payment")
    payment_thenoidia = set_up_page.get_by_title("Thẻ Nội Địa")
    payment_thenoidia.click()
    # Click Xác nhận
    btn_xacnhan = set_up_page.get_by_role("button", name="Thanh toán")
    btn_xacnhan.click()

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

    btn_Thanhtoan = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div > app-vietcombank > form.ng-touched.ng-dirty.ng-invalid > div.nd-bank-card > div.action > button")
    btn_Thanhtoan.click()

    input_otp = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.nd-form-input > div > input")
    input_otp.fill("123456")

    btn_ThanhtoanOTP = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.action > div > button")
    btn_ThanhtoanOTP.click()

    logger.info(msg="Payment success")
    result_payment = set_up_page.wait_for_selector("//div[@class='text-nds-para-small font-semibold sm:text-nds-desktop-h6']")
    expect_result: str = 'Thanh toán thành công'
    assert expect_result in result_payment.text_content()

def test_Bike_TPL_BaoMinh(set_up_page: Page):
    product_detail = "Bảo hiểm xe máy"
    insurer_detail = "Bảo Minh"

    # Homepage Saladin
    logger.info(msg="Choose product cats")
    product_cat = set_up_page.get_by_title(product_detail)
    product_cat.click()

    # Landing page Bảo hiểm ô tô
    logger.info(msg="Open landing page")
    flow_mua = set_up_page.get_by_text("Mua ngay")
    flow_mua.click()

    # Page Thời hạn bảo hiểm
    # Chọn nhà cung cấp
    logger.info(msg="Choose insurer Bảo Minh")
    insurer = set_up_page.get_by_text(insurer_detail)
    insurer.click()
    # Click btn Điền thông tin
    btn_dienthongtin = set_up_page.get_by_text("Điền thông tin")
    btn_dienthongtin.click()

    # Page Điền thông tin
    # Click icon meo meo
    logger.info(msg="Input random buyer information")
    icon_meow = set_up_page.get_by_title("Meow meow")
    icon_meow.click()
    # Click btn Hoàn tất
    btn_hoantat = set_up_page.get_by_text("Hoàn tất")
    btn_hoantat.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    logger.info(msg="Review order")
    btn_Tienhanhthanhtoan = set_up_page.get_by_role("button", name="Tiến hành thanh toán")
    btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Chọn thanh toán thẻ nội địa
    logger.info(msg="Review payment")
    payment_thenoidia = set_up_page.get_by_title("Thẻ Nội Địa")
    payment_thenoidia.click()
    # Click Xác nhận
    btn_xacnhan = set_up_page.get_by_role("button", name="Thanh toán")
    btn_xacnhan.click()

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

    btn_Thanhtoan = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div > app-vietcombank > form.ng-touched.ng-dirty.ng-invalid > div.nd-bank-card > div.action > button")
    btn_Thanhtoan.click()

    input_otp = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.nd-form-input > div > input")
    input_otp.fill("123456")

    btn_ThanhtoanOTP = set_up_page.locator(
        "#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.action > div > button")
    btn_ThanhtoanOTP.click()

    logger.info(msg="Payment success")
    result_payment = set_up_page.wait_for_selector("//div[@class='text-nds-para-small font-semibold sm:text-nds-desktop-h6']")
    expect_result: str = 'Thanh toán thành công'
    assert expect_result in result_payment.text_content()
