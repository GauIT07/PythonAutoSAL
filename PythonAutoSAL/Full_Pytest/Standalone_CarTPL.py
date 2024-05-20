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


def test_CarTPL_PVI_promo(set_up_page: Page):
    product_detail = "Bảo hiểm ô tô"
    insurer_detail = "PVI"
    numberseat = "10"
    text_owner = "Đặt đơn T"
    coupon_detail_name = "CarTPL10K"

    # Homepage Saladin
    logger.info(msg="Choose product cats")
    product_cat = set_up_page.get_by_title(product_detail)
    product_cat.click()

    # Landing page Bảo hiểm ô tô
    logger.info(msg="open landing page")
    flow_mua = set_up_page.get_by_text("Mua ngay")
    flow_mua.click()

    # Page chọn bảo hiểm
    # Nhập số chỗ ngồi
    logger.info(msg="Input infomation")
    textbox_amountseat = set_up_page.locator("//*[@id='amount_seat']")
    textbox_amountseat.clear()
    textbox_amountseat.fill(numberseat)
    # Click btn Tiếp tục
    btn_Tieptuc = set_up_page.get_by_text("Tiếp tục")
    btn_Tieptuc.click()

    # Page Thời hạn bảo hiểm
    # Chọn nhà cung cấp
    logger.info(msg="chosse insurer PVI")
    insurer = set_up_page.get_by_text(insurer_detail)
    insurer.click()
    # Click btn Điền thông tin
    btn_Dienthongtin = set_up_page.get_by_text("Điền thông tin")
    btn_Dienthongtin.click()

    # Page Điền thông tin
    # Click icon meo meo
    logger.info(msg="input car and buyer information")
    textbox_owner = set_up_page.locator("#buyer_name")
    textbox_owner.fill(text_owner)

    textbox_address = set_up_page.locator("#buyer_address")
    textbox_address.fill("111 LCT Q3")

    textbox_idnumber = set_up_page.locator("#buyer_identity")
    textbox_idnumber.fill("111222333")

    textbox_platenumber = set_up_page.locator("#plate_number")
    textbox_platenumber.fill("51L12222")

    textbox_chassis = set_up_page.locator("#chassis")
    textbox_chassis.fill("SOKHUNG")

    # icon_meow = page.get_by_title("Meow meow")
    # await icon_meow.highlight()
    # await icon_meow.click()
    # Click btn Hoàn tất
    textbox_email = set_up_page.locator("#buyer_email")
    textbox_email.fill("nhantest1@yopmail.com")

    textbox_phonenumber = set_up_page.locator("#buyer_phone")
    textbox_phonenumber.fill("0908111222")

    btn_Hoantat = set_up_page.get_by_text("Hoàn tất")
    btn_Hoantat.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    logger.info(msg="review order")
    btn_Tienhanhthanhtoan = set_up_page.get_by_role("button", name="Tiến hành thanh toán")
    btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Add coupon code
    logger.info(msg="review payment and apply promotion")
    coupon = set_up_page.locator(
        "//div[@class='ml-[8px] text-on-surface-dark-high-emphasis sm:text-body-large' and contains(text(),'Chọn hoặc nhập mã ưu đãi')]")
    coupon.click()
    xpath = f"//div[@class='pr-[8px] text-body-medium font-semibold' and contains(text(),'{coupon_detail_name}')]"
    coupon_detail = set_up_page.locator(xpath)
    coupon_detail.click()
    btn_Sudung = set_up_page.get_by_role("button", name="Sử dụng")
    btn_Sudung.click()

    # Chọn thanh toán thẻ nội địa
    payment_thenoidia = set_up_page.get_by_title("Thẻ Nội Địa")
    payment_thenoidia.click()
    # Click Xác nhận
    btn_Xacnhan = set_up_page.get_by_role("button", name="Xác nhận")
    btn_Xacnhan.click()

    # Page Onepay Thẻ nội địa
    # Chọn ABBANK
    logger.info(msg="Payment Provider")
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