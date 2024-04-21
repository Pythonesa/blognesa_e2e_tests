import re
from playwright.sync_api import Page, expect

def test_menu_home(page: Page):
    page.goto("https://blognesa.netlify.app/blog")
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    page.get_by_role("link", name="Home").click()
    expect(page).to_have_url(re.compile("https://blognesa.netlify.app/"))

def test_menu_blog(page: Page):
    page.goto("https://blognesa.netlify.app")
    expect(page.get_by_role("link", name="Blog", exact=True)).to_be_visible()
    page.get_by_role("link", name="Blog", exact=True).click()
    expect(page).to_have_url(re.compile("https://blognesa.netlify.app/blog"))

def test_menu_series(page: Page):
    page.goto("https://blognesa.netlify.app")
    expect(page.get_by_role("link", name="Series")).to_be_visible()
    page.get_by_role("link", name="Series").click()
    expect(page).to_have_url(re.compile("https://blognesa.netlify.app/series"))