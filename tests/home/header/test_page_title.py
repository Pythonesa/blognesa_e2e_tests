import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://blognesa.netlify.app/")
    expect(page).to_have_title(re.compile("Pythonesa's Blog"))
