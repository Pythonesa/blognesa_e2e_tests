import re
from playwright.sync_api import Page, expect

def test_has_logo(page: Page):
    page.goto("https://blognesa.netlify.app/blog")
    expect(page.get_by_role("link", name="Icono que muestra un diálogo")).to_be_visible()
    page.get_by_role("link", name="Icono que muestra un diálogo").click()
    expect(page).to_have_url(re.compile("https://blognesa.netlify.app/"))
