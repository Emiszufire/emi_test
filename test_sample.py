from playwright.sync_api import expect


def test_page_has_title(page):
    page.goto("https://demoqa.com/elements")
    expect(page).to_have_title("DEMOQA")