from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cellmapper.net/map?MCC=310&MNC=410&type=LTE&latitude=0&longitude=0&zoom=11&showTowers=true&showIcons=true&showTowerLabels=true&clusterEnabled=true&tilesEnabled=true&showOrphans=false&showNoFrequencyOnly=false&showFrequencyOnly=false&showBandwidthOnly=false&DateFilterType=Last&showHex=false&showVerifiedOnly=false&showUnverifiedOnly=false&showLTECAOnly=false&showENDCOnly=false&showBand=0&showSectorColours=true&mapType=roadmap&darkMode=false&imperialUnits=false")
    page.get_by_role("button", name="I Agree").click()
    page.get_by_label("dismiss cookie message").click()
    page.get_by_role("button", name=" Menu").click()
    page.get_by_role("button", name=" Provider").click()
    page.locator("#modal_select_provider").get_by_role("button", name="").click()
    
    page.get_by_role("button", name=" Settings").click()
    page.locator("#doTrails").uncheck()
    page.locator("#modal_mapsettings_details").get_by_role("button", name="").click()
    
    
    page.get_by_role("button", name=" Search").click()
    page.get_by_placeholder("Enter street or city name").click()
    page.get_by_placeholder("Enter street or city name").fill("1620 S Ocean Blvd, 33062")
    page.get_by_placeholder("Enter street or city name").press("Enter")
    page.locator("#modal_searchtools_details").get_by_role("button", name="").click()
    page.get_by_role("button", name=" Hide Menu").click()
   
    
    
    time.sleep(1.5)  # Add a 5-second delay
    page.wait_for_selector('button[class="ol-zoom-out"]')
    # # Click the button
    page.click('button[class="ol-zoom-out"]')
    # page.get_by_role("button", name=" Hide Menu").click()
  
  
    time.sleep(3)  # Add a 5-second delay
    
    page.screenshot(path="./ATTCellMapper.png", full_page=True) # Screenshot the page
    
    
    page.get_by_role("button", name=" Menu").click()
    page.get_by_role("button", name=" Provider").click()
    page.get_by_text("AT&T Mobility - United States of America - 310410").nth(1).click()
    page.get_by_role("combobox", name="Select a Provider").fill("verizon")
    page.get_by_role("option", name="Verizon - United States of America - 311480").click()
    page.locator("#modal_select_provider").get_by_role("button", name="").click()
    
    page.get_by_role("button", name=" Settings").click()
    page.locator("#doTrails").check()
    page.locator("#doTrails").uncheck()
    page.locator("#modal_mapsettings_details").get_by_role("button", name="").click()
    page.get_by_role("button", name=" Hide Menu").click()
   
    
    time.sleep(3)  # Add a 5-second delay
    page.screenshot(path="./VerizonCellMapper.png", full_page=True) # Screenshot2 the page
    
    
    page.get_by_role("button", name=" Menu").click()
    page.get_by_role("button", name=" Provider").click()
    page.get_by_text("Verizon - United States of America - 311480").nth(1).click()
    page.get_by_role("combobox", name="Select a Provider").fill("mobile")
    page.get_by_role("option", name="T-Mobile USA - United States of America - 310260").click()
    page.locator("#modal_select_provider").get_by_role("button", name="").click()
    
    page.get_by_role("button", name=" Settings").click()
    page.locator("#doTrails").check()
    page.locator("#doTrails").uncheck()
    page.locator("#modal_mapsettings_details").get_by_role("button", name="").click()
    page.get_by_role("button", name=" Hide Menu").click()
   
    
    time.sleep(3)  # Add a 5-second delay
    page.screenshot(path="./TMobileCellMapper.png", full_page=True) # Screenshot2 the page
    
    print("Done")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
