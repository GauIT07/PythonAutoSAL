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

def test_CarCom_CarTPL_BaoViet(set_up_page: Page):
    product_detail = "Bảo hiểm vật chất ô tô"
    insurer_detail = "Bảo Hiểm Hàng Không"
    phone_number = "0901123079"
    user_password = "112233"

    # Sign in
    btn_signin = set_up_page.get_by_role("button", name="Đăng nhập")
    btn_signin.click()
    textbox_phone = set_up_page.locator("//input[@id='phone']")
    textbox_phone.fill(phone_number)
    btn_Tieptuc = set_up_page.get_by_role("button", name="Tiếp tục")
    btn_Tieptuc.click()
    textbox_password = set_up_page.locator("//input[@id='password']")
    textbox_password.fill(user_password)
    btn_dangnhap = set_up_page.get_by_role("button", name="Đăng nhập")
    btn_dangnhap.click()

    # Homepage Saladin
    logger.info(msg="Choose product cats")
    product_cat = set_up_page.get_by_title(product_detail)
    product_cat.click()

    # Landing page Bảo hiểm ô tô
    logger.info(msg="open landing page")
    flow_mua = set_up_page.get_by_text("Mua online")
    flow_mua.click()

    order_draft = set_up_page.get_by_role("button", name="Không, tạo đơn mới")
    order_draft.click()


     # Click btn Tiếp tục
    logger.info(msg="Input detail car information")
    icon_meow = set_up_page.get_by_role("button", name="Meow meow")
    icon_meow.click()
    btn_Tieptuc1 = set_up_page.get_by_role("button", name="Tiếp tục")
    btn_Tieptuc1.click()

    # Page Thời hạn bảo hiểm
    # Chọn nhà cung cấp
    logger.info(msg="Choose insurer package")
    btn_muangay = set_up_page.get_by_role("button", name="Mua ngay")
    btn_muangay.nth(4).click()

    # Page thông tin bảo hiểm
    logger.info(msg="input buyer information")
    textbox_idnumber = set_up_page.locator("//*[@name='buyer_identity']")
    textbox_idnumber.fill("111222333")

    textbox_address = set_up_page.locator("//*[@name='buyer_address']")
    textbox_address.fill("111 LCT Q3")

    field_tinhthanh = set_up_page.locator("//div[@class='h-[18px] fill-nds-t-icon text-nds-t-icon']")
    field_tinhthanh.nth(0).click()
    combobox_tinhthanh = set_up_page.locator("//div[@class='text-nds-para-medium' and contains(text(), 'Thành phố Hồ Chí Minh')]")
    combobox_tinhthanh.click()

    field_quanhuyen = field_tinhthanh.nth(1)
    field_quanhuyen.click()
    combobox_quanhuyen = set_up_page.locator("//div[@class='text-nds-para-medium' and contains(text(), 'Quận 3')]")
    combobox_quanhuyen.click()

    btn_Tieptuc2 = set_up_page.get_by_text("Tiếp tục")
    btn_Tieptuc2.click()

    # Page Điền thông tin
    # Click icon meo meo
    logger.info(msg="Input detail car information")
    select_option = set_up_page.locator("//*[@class='font-medium text-inherit' and contains(text(), 'Bảo hiểm cũ còn hiệu lực')]")
    select_option.check()

    bh_VNI = set_up_page.locator("//div[@title='Bảo Hiểm Hàng Không']")
    bh_VNI.click()

    textbox_plate = set_up_page.locator("//input[@name='plate']")
    textbox_plate.fill("51A12345")
    texbox_chassis = set_up_page.locator("//input[@name='chassis']")
    texbox_chassis.fill("SOKHUNG")
    # checkbox TNDS
    checkbox_CarTPL = set_up_page.locator("//input[@id='cs_tnds']")
    checkbox_CarTPL.check()
    # Click btn Hoàn tất
    btn_Tieptuc3 = set_up_page.locator("//button[@type='submit']")
    btn_Tieptuc3.nth(0).click()

    # Page upload ảnh
    icon_meow3 = set_up_page.locator("//button[@title='Meow meow']")
    icon_meow3.click()

    btn_Tieptuc4 = set_up_page.locator("//button[@type='submit']")
    btn_Tieptuc4.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    logger.info(msg="review order")
    btn_Tienhanhthanhtoan = set_up_page.get_by_role("button", name="Tiến hành thanh toán")
    btn_Tienhanhthanhtoan.click()


