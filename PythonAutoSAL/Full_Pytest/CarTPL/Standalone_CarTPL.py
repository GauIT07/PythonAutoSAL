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

    page.goto("https://dev-admin.saladin.vn/login")
    page.locator("//input[@name='email']").fill("saladin_writer@tenxtenx.com")
    page.locator("//input[@name='password']").fill("123456")
    page.locator("//button[@type='submit']").click()

    yield page

    logger.info(msg="Close Browser")
    page.close()

def test_CarTPL_PVI_promo(set_up_page: Page):
    product_detail = "Bảo hiểm ô tô"
    insurer_detail = "PVI"
    numberseat = "5"
    fullname = "Dat don CarTPL"
    coupon_detail_name = "Nghia Campaign Car"
    namSanXuat = "2023"
    mucDichSuDung = "Chở người"
    loaiVanChuyenDacBiet = "Không"

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
    # Chon KDVT
    selectbox_KDVT = set_up_page.locator("//div[@class='font-medium text-inherit' and contains(text(),'Có')]")
    selectbox_KDVT.check()
    # Chon Nam san xuat
    textbox_namSanXuat = set_up_page.locator("//input[@id=':r5:']")
    textbox_namSanXuat.click()
    xpath_namSanXuat = f"//div[@class='text-nds-para-medium' and contains(text(),'{namSanXuat}')]"
    textbox_namSanXuat_value = set_up_page.locator(xpath_namSanXuat)
    textbox_namSanXuat_value.click()
    # Chon Muc dich su dung
    textbox_mucDichSuDung = set_up_page.locator("//input[@id=':ra:']")
    textbox_mucDichSuDung.click()
    xpath_mucDichSuDung = f"//div[@class='text-nds-para-medium' and contains(text(), '{mucDichSuDung}')]"
    textbox_mucDichSuDung_value = set_up_page.locator(xpath_mucDichSuDung)
    textbox_mucDichSuDung_value.click()
    # Chon Loai van chuyen dac biet
    textbox_loaiVanChuyenDacBiet = set_up_page.locator("//input[@id=':rf:']")
    textbox_loaiVanChuyenDacBiet.click()
    xpath_loaiVanChuyenDacBiet = f"//div[@class='text-nds-para-medium' and contains(text(), '{loaiVanChuyenDacBiet}')]"
    textbox_loaiVanChuyenDacBiet_value = set_up_page.locator(xpath_loaiVanChuyenDacBiet)
    textbox_loaiVanChuyenDacBiet_value.click()
    # Nhap so cho ngoi
    textbox_amountseat = set_up_page.locator("//input[@id=':rh:']")
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
    btn_Tieptuc2 = set_up_page.get_by_text("Tiếp tục")
    btn_Tieptuc2.click()

    # Page Điền thông tin
    # Click icon meo meo
    logger.info(msg="input car and buyer information")
    textbox_owner = set_up_page.locator("//input[@name='buyer_name']")
    textbox_owner.fill("Don CarTPL")

    textbox_address = set_up_page.locator("//input[@name='buyer_address']")
    textbox_address.fill("111 LCT Q3")

    textbox_idnumber = set_up_page.locator("//input[@name='buyer_nid']")
    textbox_idnumber.fill("111222333")

    textbox_platenumber = set_up_page.locator("//input[@name='plate']")
    textbox_platenumber.fill("51L12222")

    textbox_chassis = set_up_page.locator("//input[@name='chassis']")
    textbox_chassis.fill("SOKHUNG")

    # icon_meow = page.get_by_title("Meow meow")
    # await icon_meow.highlight()
    # await icon_meow.click()
    # Click btn Hoàn tất
    textbox_email = set_up_page.locator("//input[@name='cert_email']")
    textbox_email.fill("saltest@yopmail.com")

    textbox_phonenumber = set_up_page.locator("//input[@name='cert_phone']")
    textbox_phonenumber.fill("0901123123")

    btn_Tieptuc3 = set_up_page.get_by_text("Tiếp tục")
    btn_Tieptuc3.first.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    logger.info(msg="review order")
    btn_Tienhanhthanhtoan = set_up_page.get_by_role("button", name="Tiến hành thanh toán")
    btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Add coupon code
    logger.info(msg="review payment and apply promotion")
    # Ma don hang
    order_id_value = set_up_page.locator("//div[@class='text-right text-nds-para-small sm:text-nds-para-medium ']")
    order_id = order_id_value.first.text_content()
    # Nhap ma uu dai
    coupon_code = set_up_page.locator("//div[@class='ml-[8px] text-nds-para-medium text-nds-t-text-placeholder']")
    coupon_code.click()
    xpath = f"//div[@class='pr-[8px] text-body-medium font-semibold' and contains(text(),'{coupon_detail_name}')]"
    coupon_detail = set_up_page.locator(xpath)
    coupon_detail.click()
    btn_Sudung = set_up_page.get_by_role("button", name="Sử dụng")
    btn_Sudung.click()

    # Chọn thanh toán thẻ nội địa
    payment_thenoidia = set_up_page.get_by_title("Thẻ Nội Địa")
    payment_thenoidia.click()
    # Click Xác nhận
    btn_Xacnhan = set_up_page.get_by_role("button", name="Thanh toán")
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

    logger.info(msg="Order id: " + order_id)

    return order_id

