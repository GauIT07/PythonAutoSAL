import asyncio

from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright, __next=None):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()

    renewal_urlCarTPL = "https://saladin.vn/renewal/zns?policy_id=P1117031362&env=staging"
    # sokhung = "SOKHUNG"
    # bienso = "14N11234"

    # Renewal Car TPL
    # [to: 84901112233] ["Test BIKE Test StandaloneNăm 718142","P1117031362","12-04-2025 23:59:00",
    # "Test BIKE Test StandaloneNăm 718142","P1117031362","Xe máy","66,000đ","Liên hệ ngay Saladin để được gia hạn và đảm bảo quyền lợi",
    # "renewal/zns?policy_id=P1117031362&env=staging"]
    await page.goto(renewal_urlCarTPL)

    # Click Thanh toán ngay
    btn_Thanhtoanngay = page.locator("#__next > main > div > section > div > div > div.mt-nds-lg.hidden.xl\:block > div > div:nth-child(2) > button > div > div")
    await btn_Thanhtoanngay.highlight()
    await btn_Thanhtoanngay.click()

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