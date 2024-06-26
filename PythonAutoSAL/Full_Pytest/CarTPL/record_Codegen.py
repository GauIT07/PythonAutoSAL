import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dev.saladin.vn/")
    page.get_by_title("Bảo hiểm ô tô").click()
    page.get_by_role("button", name="Mua ngay").click()
    page.locator("section").filter(has_text=re.compile(r"^Năm sản xuất$")).locator("label").nth(1).click()
    page.get_by_role("option", name="2022").click()
    page.locator("section").filter(has_text=re.compile(r"^Mục đích sử dụng$")).get_by_placeholder("Chọn").click()
    page.get_by_role("option", name="Chở người").click()
    page.locator("section").filter(has_text=re.compile(r"^Loại vận chuyển đặc biệt$")).locator("label").nth(1).click()
    page.get_by_role("option", name="Không").click()
    page.get_by_label("chỗ").click()
    page.get_by_label("chỗ").fill("5")
    page.get_by_role("button", name="Tiếp tục").click()
    page.get_by_text("₫").nth(2).click(button="right")
    page.get_by_text("₫").nth(2).click()
    expect(page.locator("form")).to_contain_text("480.700 ₫")
    page.get_by_role("button", name="").click()
    page.get_by_label("chỗ").click()
    page.get_by_label("chỗ").fill("16")
    page.get_by_role("button", name="Tiếp tục").click()
    page.get_by_text("₫").nth(2).click(button="right")
    expect(page.locator("form")).to_contain_text("1.397.000 ₫")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
