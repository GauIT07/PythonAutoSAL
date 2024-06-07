from playwright.sync_api import Page, sync_playwright, Locator, expect
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

# Insurer PVI KKD CN
def test_CarTPL_KKD_CN_K_promo(set_up_page: Page, ):
    product_detail = "Bảo hiểm ô tô"
    insurer_detail = "PVI"
    kdvt_value = "Không"
    numberseat = "4"
    namSanXuat = "2023"
    mucDichSuDung = "Chở người"
    loaiVanChuyenDacBiet = "Không"
    expected_result :str = "480.700"

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
    field_KDVT = f"//div[@class='font-medium text-inherit' and contains(text(),'{kdvt_value}')]"
    selectbox_KDVT = set_up_page.locator(field_KDVT)
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
    textbox_loaiVanChuyenDacBiet_value = set_up_page.wait_for_selector(xpath_loaiVanChuyenDacBiet)
    textbox_loaiVanChuyenDacBiet_value.click()
    # Nhap so cho ngoi
    textbox_amountseat = set_up_page.locator("//input[@id=':rh:']")
    textbox_amountseat.clear()
    textbox_amountseat.fill(numberseat)
    # Click btn Tiếp tục
    btn_Tieptuc = set_up_page.get_by_text("Tiếp tục")
    btn_Tieptuc.click()

    # Page Thời hạn bảo hiểm

    #price_TNDS = set_up_page.locator("//div[@class='text-nds-para-medium font-semibold' and contains(text(), '₫')]")
    price_TNDS = set_up_page.locator("//*[@id='__next']/main/div/div/form/section/div[2]/div[1]/aside/div[2]/div[2]")
    actual_result_value = price_TNDS.text_content()
    actual_result = f"{actual_result_value}"
    assert expected_result in actual_result
