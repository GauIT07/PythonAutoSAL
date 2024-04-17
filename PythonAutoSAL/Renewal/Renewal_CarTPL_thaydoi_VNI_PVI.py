import asyncio

from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright, __next=None):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()

    renewal_urlCarTPL = "https://dev.saladin.vn/renewal/zns?policy_id=P4559194770&env=staging"
    insurer_detail = "PVI"
    sokhung = "SOKHUNG"
    bienso = "14N11234"

    # Renewal Car TPL
    # [to: 84347771791] ["CHU NGỌC THÁI", "P7592385410", "10-05-2024 23:59:00", "CHU NGỌC THÁI",
    # "P7592385410", "Ô tô", "530,700đ", "Liên hệ ngay Saladin để được gia hạn và đảm bảo quyền lợi",
    # "renewal/zns?policy_id=P7592385410&env=staging"]
    await page.goto(renewal_urlCarTPL)

    # click xem chi tiết
    icon_edit = page.locator("#__next > main > div > section > div > div > div.relative.pb-nds-xl.xl\:rounded-b-nds-lg.xl\:bg-nds-t-bg-alternative.xl\:shadow-nds-md > section > div > div:nth-child(2)")
    await icon_edit.highlight()
    await icon_edit.click()
    # click thay đổi
    text_Thaydoi = page.get_by_text("Thay đổi")
    await text_Thaydoi.highlight()
    await text_Thaydoi.click()

    # Page Chọn bảo hiểm
    # Chọn Nhà cung cấp
    insurer = page.get_by_text(insurer_detail)
    await insurer.highlight()
    await insurer.check()
    # Enable toggle
    toggle_TNNNTX = page.locator("#__next > main > div > div.pb-\[130px\].xl\:flex.xl\:space-x-\[34px\] > section > div:nth-child(2) > form > div.mb-\[24px\].space-y-\[8px\].bg-white.py-\[0px\].sm\:space-y-0 > section:nth-child(3) > div:nth-child(3) > div > div:nth-child(2) > label > div.rv-input-radio-text-unchecked-icon.hover\:opacity-90 > svg > rect:nth-child(3)")
    await toggle_TNNNTX.highlight()
    await toggle_TNNNTX.click()
    # Click btn Điền thông tin
    btn_Dienthongtin = page.get_by_role("button", name="Điền thông tin")
    await btn_Dienthongtin.highlight()
    await btn_Dienthongtin.click()


    # Page Điền thông tin
    # Bổ sung biển số
    textbox_bienso = page.locator("//*[@id='plate_number']")
    await textbox_bienso.highlight()
    await textbox_bienso.clear()
    await textbox_bienso.fill(bienso)
    # Bổ sung số khung
    textbox_sokhung = page.locator("//*[@id='chassis']")
    await textbox_sokhung.highlight()
    await textbox_sokhung.fill(sokhung)
    # Click Hoàn tất
    btn_Hoantat = page.get_by_role("button",name="Hoàn tất")
    await btn_Hoantat.highlight()
    await btn_Hoantat.click()

    # Page Đơn hàng
    # click btn Tiến hành thanh toán
    btn_Tienhanhthanhtoan = page.get_by_role("button", name="Tiến hành thanh toán")
    await btn_Tienhanhthanhtoan.highlight()
    await btn_Tienhanhthanhtoan.click()

    # Page thông tin thanh toán
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

    btn_Thanhtoan = page.locator("#domescard-radio > div > domescard-main > div > div > div > app-vietcombank > form.ng-touched.ng-dirty.ng-invalid > div.nd-bank-card > div.action > button")
    await btn_Thanhtoan.highlight()
    await btn_Thanhtoan.click()

    input_otp = page.locator("#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.nd-form-input > div > input")
    await input_otp.highlight()
    await input_otp.fill("123456")

    btn_ThanhtoanOTP = page.locator("#domescard-radio > div > domescard-main > div > div > div > app-otp-auth > form > div.nd-bank-card > div.action > div > button")
    await btn_ThanhtoanOTP.highlight()
    await btn_ThanhtoanOTP.click()

    await browser.close()

#__next > main > div > section > div > div > div.xl\:hidden > div > div > div:nth-child(1) > button > div > div
async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())