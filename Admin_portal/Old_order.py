
from playwright.async_api import async_playwright, Playwright
import pytest
import logging

@pytest.fixture
def test_Admin_portal(page: Page):


async def run(playwright: Playwright, __next=None):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()


async def main():
    async with async_playwright() as playwright:
    await run(playwright)

asyncio.run(main())