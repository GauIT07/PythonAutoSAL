from playwright.sync_api import Page, sync_playwright, Locator
import pytest
import logging

logger = logging.getLogger('___Test___')
logger.setLevel(logging.INFO)

@pytest.fixture(scope="function", autouse=True)
def set_up_page(page: Page):
    logger.info(msg="Open dev.saladin.vn")
    page.goto("https://dev.saladin.vn")
    # return page
    yield page

    logger.info(msg="Close Browser")
    page.close()

#@pytest.fixture(scope="function", autouse=True)
#def payment_provider(set_up_page: Page):

def test_CarCom_VNI(set_up_page: Page):
    product_detail = "Bảo hiểm vật chất ô tô"
    insurer_detail = "Bảo Hiểm Hàng Không"

    # Homepage Saladin
    logger.info(msg="Choose product cats")
    product_cat = set_up_page.get_by_title(product_detail)
    product_cat.click()

    # Landing page Bảo hiểm ô tô
    logger.info(msg="open landing page")
    flow_mua = set_up_page.get_by_text("Mua online")
    flow_mua.click()

    # Page chọn bảo hiểm
    logger.info(msg="Input car information")
    icon_meow1 = set_up_page.get_by_role("button", name="Meow meow")
    icon_meow1.click()
    # Click btn Tiếp tục
    btn_Tieptuc = set_up_page.get_by_text("Tiếp tục")
    btn_Tieptuc.click()

    # Page Thời hạn bảo hiểm
    # Chọn nhà cung cấp
    logger.info(msg="Choose insurer package")

    btn_muangay = set_up_page.get_by_role("button", name="Mua ngay")
    btn_muangay.nth[0].click()
    # Click btn Điền thông tin
    btn_Dienthongtin = set_up_page.get_by_text("Điền thông tin")
    btn_Dienthongtin.click()

    # Page Điền thông tin
    # Click icon meo meo
    logger.info(msg="Input detail car information")
    icon_meow2 = set_up_page.get_by_role("button", name="Meow meow")
    icon_meow2.click()
    # Click btn Hoàn tất
    btn_Hoantat = set_up_page.get_by_text("Hoàn tất")
    btn_Hoantat.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    logger.info(msg="review order")
    btn_Tienhanhthanhtoan = set_up_page.get_by_role("button", name="Tiến hành thanh toán")
    btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Chọn thanh toán thẻ nội địa
    logger.info(msg="review payment")
    payment_thenoidia = set_up_page.get_by_title("Thẻ Nội Địa")
    payment_thenoidia.click()
    # Click Xác nhận
    btn_Xacnhan = set_up_page.get_by_role("button", name="Xác nhận")
    btn_Xacnhan.click()

    # Page Onepay Thẻ nội địa
    # Chọn ABBANK
    logger.info(msg="Payment provider")
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

