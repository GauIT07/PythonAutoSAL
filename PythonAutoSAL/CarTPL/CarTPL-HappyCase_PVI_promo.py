import asyncio
import random

from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    # where we define all actions we control and action on browser
    browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
    page = await browser.new_page()


    await page.goto("https://dev.saladin.vn")

    product_detail = "Bảo hiểm ô tô"
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
    # Nhập số chỗ ngồi
    textbox_amountseat = page.locator("//*[@id='amount_seat']")
    await textbox_amountseat.highlight()
    await textbox_amountseat.clear()
    await textbox_amountseat.fill(numberseat)
    # Click btn Tiếp tục
    btn_Tieptuc = page.get_by_text("Tiếp tục")
    await btn_Tieptuc.highlight()
    await btn_Tieptuc.click()

    # Page Thời hạn bảo hiểm
    # Chọn nhà cung cấp
    insurer = page.get_by_text(insurer_detail)
    await insurer.highlight()
    await insurer.click()
    # Click btn Điền thông tin
    btn_Dienthongtin = page.get_by_text("Điền thông tin")
    await btn_Dienthongtin.highlight()
    await btn_Dienthongtin.click()

    # Page Điền thông tin
    # Click icon meo meo
    textbox_owner = page.locator("#buyer_name")
    await textbox_owner.highlight()
    await textbox_owner.fill(text_owner)

    textbox_address = page.locator("#buyer_address")
    await textbox_address.highlight()
    await textbox_address.fill("111 LCT Q3")

    textbox_idnumber = page.locator("#buyer_identity")
    await textbox_idnumber.highlight()
    await textbox_idnumber.fill("111222333")

    textbox_platenumber = page.locator("#plate_number")
    await textbox_platenumber.highlight()
    await textbox_platenumber.fill("51L12222")

    textbox_chassis = page.locator("#chassis")
    await textbox_chassis.highlight()
    await textbox_chassis.fill("SOKHUNG")

    # icon_meow = page.get_by_title("Meow meow")
    # await icon_meow.highlight()
    # await icon_meow.click()
    # Click btn Hoàn tất
    textbox_email = page.locator("#buyer_email")
    await textbox_email.highlight()
    await textbox_email.fill("nhantest1@yopmail.com")

    textbox_phonenumber = page.locator("#buyer_phone")
    await textbox_phonenumber.highlight()
    await textbox_phonenumber.fill("0908111222")

    btn_Hoantat = page.get_by_text("Hoàn tất")
    await btn_Hoantat.highlight()
    await btn_Hoantat.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    btn_Tienhanhthanhtoan = page.get_by_role("button", name="Tiến hành thanh toán")
    await btn_Tienhanhthanhtoan.highlight()
    await btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
    # Add coupon code
    coupon = page.locator("//div[@class='ml-[8px] text-on-surface-dark-high-emphasis sm:text-body-large' and contains(text(),'Chọn hoặc nhập mã ưu đãi')]")
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
    payment_thenoidia = page.get_by_title("Thẻ Nội Địa")
    await payment_thenoidia.highlight()
    await payment_thenoidia.click()
    # Click Xác nhận
    btn_Xacnhan = page.get_by_role("button", name="Xác nhận")
    await btn_Xacnhan.highlight()
    await btn_Xacnhan.click()

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