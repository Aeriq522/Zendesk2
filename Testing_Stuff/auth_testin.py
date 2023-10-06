from playwright.sync_api import Playwright, sync_playwright, expect, BrowserContext
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="google.json")
    page = context.new_page()
    page.goto("https://www.netflix.com/")
    # page.get_by_label("Email or phone number").click()
    # page.get_by_label("Email or phone number").fill("eriksanchez6@gmail.com")
    # page.get_by_label("Email or phone number").press("Tab")
    # page.get_by_label("Password").fill("Esm522@@Netflix")
    # page.get_by_label("Password").press("Enter")
    # page.get_by_role("link", name="Erik").click()
    
    
  
    time.sleep(3)  # Add a 5-second delay

    # ---------------------
    context.storage_state(path="google.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
