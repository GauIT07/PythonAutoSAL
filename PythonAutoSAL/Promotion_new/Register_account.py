import asyncio
import os

from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    user_dir = 'tmp/playwright'
    user_dir = os.path.join(os.getcwd(), user_dir)
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch_persistent_context(user_dir, headless=False, slow_mo=1000,
                                                       args=['--start-maximized'], no_viewport=True)

    page = await browser.new_page()

    url_claim = ("https://boithuong-staging.saladin.vn/claim-create/travel/info-policy?policy_number=BVT.SLD.24.00000523&policy_id=colgo6d9vcg9furslplgZP&product_code=DOM_TRAVEL_E_BV_1")
    phone_embedded = 0901001013

    await page.goto(url_claim)

    # Đăng nhập và liên kết HĐ
    btn_Signin = page.get_by_text("Đăng nhập & Liên kết HĐ")
    await btn_Signin.highlight()
    await btn_Signin.click()

    textbox_phonenumber = page.locator("//input[@id='phone']")
    await textbox_phonenumber.highlight()
    await textbox_phonenumber.fill(phone_embedded)

    btn_Tieptuc = page.locator("//button[@type='submit']")
    await btn_Tieptuc.highlight()
    await btn_Tieptuc.click()
    


    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())