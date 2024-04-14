import asyncio

from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    # where we define all actions we control and action on browser
    browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
    page = await browser.new_page()


    await page.goto("https://dev.saladin.vn")

    title1 = page.get_by_title("Bảo hiểm ô tô")
    await title1.highlight()
    await title1.click()
    flow_mua = page.get_by_text("Mua ngay")
    await flow_mua.highlight()
    await flow_mua.click()
    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())