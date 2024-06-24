from playwright.sync_api import Page, sync_playwright, Locator
import pytest
import logging
from PythonAutoSAL.CarCom.Standalone_CarCom import test_CarCom_VNI

logger = logging.getLogger('___Test___')
logger.setLevel(logging.INFO)

@pytest.fixture(scope="function", autouse=True)
def set_up_page(page: Page):
    logger.info(msg="Open dev-admin.saladin.vn")
    page.goto("https://dev-admin.saladin.vn/login")
    email_textbox = page.locator("//input[@name='email']")
    email_textbox.fill("saladin_writer@tenxtenx.com")
    password_textbox = page.locator("//input[@name='password']")
    password_textbox.fill("123456")
    btn_Dangnhap = page.get_by_role("button", name="Đăng nhập")
    btn_Dangnhap.click()
    # return page
    yield page

    logger.info(msg="Close Browser")
    page.close()


def test_Old_order(set_up_page: Page):
    menu_BHthongthuong = set_up_page.get_by_text("BH thông thường")
    menu_BHthongthuong.click()
    menu_OldOder = set_up_page.get_by_text("Đơn hàng")
    menu_OldOder.click()

    filter_list = set_up_page.locator("//div[@aria-controls='mantine-va7rr9lqm']")
    filter_list.click()
    filter_MaDonHang = set_up_page.locator("//div[@id='mantine-va7rr9lqm-2']")
    filter_MaDonHang.click()

    searchbox_value = set_up_page.locator(    )
    searchbox_value.fill(order_id)