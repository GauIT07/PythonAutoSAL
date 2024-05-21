import asyncio
import random

from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    # where we define all actions we control and action on browser
    browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
    page = await browser.new_page()


    await page.goto("https://dev.saladin.vn")

    product_detail = "Sức khỏe & Ung thư"
    insurer_detail = "PVI"
    numberseat = "10"
    text_owner = "Đặt đơn T"
    coupon_detail_name = "CarTPL10K"

    # Homepage Saladin
    product_cat = page.get_by_title(product_detail)
    await product_cat.highlight()
    await product_cat.click()

    # Landing page Bảo hiểm ô tô
    flow_mua = page.get_by_text("Mua ngay")
    await flow_mua.highlight()
    await flow_mua.click()

    # Page chọn bảo hiểm
    # Chọn giới tính
    gioitinh = page.get_by_text("Nam")
    await gioitinh.highlight()
    await gioitinh.click()
    # Chọn đối tượng bảo hiểm
    doituong_baohiem = page.get_by_text("Bản thân")
    await doituong_baohiem.highlight()
    await doituong_baohiem.click()
        # Click btn Tiếp tục
    btn_Tieptuc = page.get_by_text("Tiếp tục")
    await btn_Tieptuc.highlight()
    await btn_Tieptuc.click()

    # Page Tuổi của người được bảo hiểm
    # Nhập tuổi
    textbox_ngaysinh = page.locator("#self > div > div")
    await textbox_ngaysinh.highlight()
    await textbox_ngaysinh.focus()
    input_ngaysinh = page.locator("//*[@id='self']/div/div/div[1]/input")
    await input_ngaysinh.fill("01/01/2000")
    # Click btn Xem gói bảo hiểm
    btn_Xemgoibaohiem = page.locator("//div[@class='flex-1' and contains(text(), 'Xem gói bảo hiểm')]")
    await btn_Xemgoibaohiem.highlight()
    await btn_Xemgoibaohiem.click()

    # Page Gói bảo hiểm
    goibaohiem = page.locator("//*[@id='__next']/main/div/div/div/div[3]/div[1]/div[3]/div[2]/div[2]/button[2]/div/div")
    await goibaohiem.highlight()
    await goibaohiem.click()

    # Page Người mua bảo hiểm
    textbox_hoten = page.locator("//input[@name='name']")
    await textbox_hoten.highlight()
    await textbox_hoten.fill(text_owner)

    textbox_idnumber = page.locator("//input[@name='identity_no']")
    await textbox_idnumber.highlight()
    await textbox_idnumber.fill("111222333")

    textbox_email = page.locator("//input[@name='email']")
    await textbox_email.highlight()
    await textbox_email.fill("nhantest1@yopmail.com")

    textbox_phonenumber = page.locator("//input[@name='phone_no']")
    await textbox_phonenumber.highlight()
    await textbox_phonenumber.fill("0908111222")

    textbox_address = page.locator("//input[@name='address']")
    await textbox_address.highlight()
    await textbox_address.fill("111 LCT Q3")

    combobox_tinhthanh = page.locator("//*[@id='__next']/main/div/div/div/form/div/div[1]/div[1]/div[3]/div[4]/label/label")
    await combobox_tinhthanh.highlight()
    await combobox_tinhthanh.click()
    value_tinhthanh = page.get_by_role("option", name="Hậu Giang")
    await value_tinhthanh.click()

    combobox_quanhuyen = page.locator("//*[@id='__next']/main/div/div/div/form/div/div[1]/div[1]/div[3]/div[5]/label/label")
    await combobox_quanhuyen.click()
    value_quanhuyen = page.get_by_role("option", name="Long Mỹ")
    await value_quanhuyen.click()

    btn_Hoantat = page.get_by_role("button", name="Tiếp tục")
    # await btn_Hoantat.highlight()
    await btn_Hoantat.click()

    # Page Người được bảo hiểm
    option_Khong = page.locator("//div[@class='flex-1' and contains(text(),'Không')]")
    await option_Khong.highlight()
    await option_Khong.click()

    btn_Hoantat = page.get_by_role("button", name="Tiếp tục")
    await btn_Hoantat.highlight()
    await btn_Hoantat.click()

    btn_Xacnhan = page.locator("//div[@class='flex-1' and contains(text(),'Xác nhận')]")
    await btn_Xacnhan.highlight()
    await btn_Xacnhan.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    btn_Tienhanhthanhtoan = page.get_by_role("button", name="Tiến hành thanh toán")
    await btn_Tienhanhthanhtoan.highlight()
    await btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Add coupon code
    coupon = page.locator("//*[@class='ml-[8px] text-nds-para-medium text-nds-t-text-placeholder']")
    await coupon.highlight()
    await coupon.click()
    xpath = f"//div[@class='pr-[8px] text-body-medium font-semibold' and contains(text(),'{coupon_detail_name}')]"
    coupon_detail = page.locator(xpath)
    await coupon_detail.highlight()
    await coupon_detail.click()
    btn_Sudung = page.get_by_role("button", name="Sử dụng")
    await btn_Sudung.highlight()
    await btn_Sudung.click()

    # Chọn thanh toán thẻ nội địa
    payment_thenoidia = page.locator("//*[@title='Thẻ Nội Địa']")
    await payment_thenoidia.highlight()
    await payment_thenoidia.click()
    # Click Xác nhận
    btn_Thanhtoan = page.get_by_role("button", name="Thanh toán")
    await btn_Thanhtoan.highlight()
    await btn_Thanhtoan.click()

    popup_error_coupon = page.locator("//*[@class='sc-3101c9f6-0 fkOicM']")
    if popup_error_coupon.is_visible():
        btn_errorTieptuc = page.locator("//*[@class='sc-4d7de6dd-0 fVNRie']")
        btn_errorTieptuc.click()


    # Page Onepay Thẻ nội địa
    # Chọn ABBANK
    bank_ABBANK = page.locator("#domescard-radio > div > domescard-main > div > div > div.bank-list > div > div:nth-child(17) > a > div > img")
    await bank_ABBANK.highlight()
    await bank_ABBANK.click()
    # Nhập thông tin thẻ
    card_number = page.locator("#card_number")
    await card_number.highlight()
    await card_number.fill("9704250000000001")
    issue_date = page.locator("#exp_date")
    await issue_date.highlight()
    await issue_date.fill("0113")
    card_name = page.locator("#card_name")
    await card_name.highlight()
    await card_name.fill("NGUYEN VAN A")

    btn_Thanhtoan = page.locator(
        "#domescard-radio > div > domescard-main > div > div > div > app-vietcombank > form.ng-touched.ng-dirty.ng-invalid > div.nd-bank-card > div.action > button")
    await btn_Thanhtoan.highlight()
    await btn_Thanhtoan.click()

    input_otp = page.locator("#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.nd-form-input > div > input")
    await input_otp.highlight()
    await input_otp.fill("123456")

    btn_ThanhtoanOTP = page.locator("#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.action > div > button")
    await btn_ThanhtoanOTP.highlight()
    await btn_ThanhtoanOTP.click()

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
