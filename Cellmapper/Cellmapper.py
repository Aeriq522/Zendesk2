from playwright.sync_api import Playwright, sync_playwright, expect
import time
import re
import os

street_address_1 = "21010 39th Way S"
zip_code = "98198"







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
    
    
    # After navigating to the page and interacting with other elements
    # Define a regular expression pattern for the IDs
    id_pattern = r'#([a-f0-9]{41})'
    
    # Get the HTML content of the page
    html_content = page.content()

    # Find all IDs matching the pattern - Hide Ad Popu
    ids = re.findall(id_pattern, html_content)
    
    
    # Set the Ad ID that will be hidden
    ad_id = f"#{ids[0]}"
    # print(ad_id)

    # Add CSS to hide the ad div
    css_to_hide_ad = f"{ad_id} {{ display: none !important; }}"
    page.add_style_tag(content=css_to_hide_ad)
    
    # Define the CSS selector for the <nav> element - Hide Navbar in Screenshot
    css_selector = ".navbar"

    # Generate CSS to hide the element
    css_to_hide_element = f"{css_selector} {{ display: none !important; }}"

    # Inject the CSS using Playwright's page.add_style_tag() method
    page.add_style_tag(content=css_to_hide_element)
    
    #   # Define the CSS selector for the <button> element - Hide Menu Bar in Screenshot
    # css_selector = ".btn.btn-primary.button-nav#button-menu-button"

    # # Generate CSS to hide the element
    # css_to_hide_element = f"{css_selector} {{ display: none !important; }}"

    # # Inject the CSS using Playwright's page.add_style_tag() method
    # page.add_style_tag(content=css_to_hide_element)

  
    
    page.get_by_role("button", name=" Search").click()
    page.get_by_placeholder("Enter street or city name").click()
    page.get_by_placeholder("Enter street or city name").fill(f"{street_address_1}, {zip_code}")
    page.get_by_placeholder("Enter street or city name").press("Enter")
    page.locator("#modal_searchtools_details").get_by_role("button", name="").click()
    page.get_by_role("button", name=" Hide Menu").click()
   
    
    
    time.sleep(5)  # Add a 5-second delay
    page.wait_for_selector('button[class="ol-zoom-out"]')
    # # Click the button
    page.click('button[class="ol-zoom-out"]')
    # page.get_by_role("button", name=" Hide Menu").click()
  
  
    time.sleep(5)  # Add a 5-second delay
    
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    screenshot_path = os.path.join(folder_name, "ATTCellMapper.png")
    page.screenshot(path=screenshot_path, full_page=True) # Screenshot the page
    
    
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
    screenshot_path = os.path.join(folder_name, "VerizonCellMapper.png")
    page.screenshot(path=screenshot_path, full_page=True) # Screenshot the page
   
    
    
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
    screenshot_path = os.path.join(folder_name, "TMobileCellMapper.png")
    page.screenshot(path=screenshot_path, full_page=True) # Screenshot the page

    
    
    # Grab Google Maps Screenshot for Location
    page2 = context.new_page()
    page2.goto("https://www.google.com/maps")
    page2.get_by_role("textbox", name="Search Google Maps").click()
    page2.get_by_role("textbox", name="Search Google Maps").fill(f"{street_address_1}, {zip_code}")
    page2.get_by_label("Search", exact=True).click()
    page2.get_by_label("Layers").click()
    page2.get_by_role("button", name="Collapse side panel").click()
    page2.get_by_role("button", name="Zoom out").click()
    page2.get_by_role("button", name="Zoom out").click()
   
    
    
    time.sleep(3)  # Add a 5-second delay
    screenshot_path = os.path.join(folder_name, "GoogleViewScreenshot.png")
    page2.screenshot(path=screenshot_path, full_page=True) # Screenshot the page
    
    
    
    print("Done")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    # Get user input for the folder name
    folder_name = input("Enter folder name: ")
    street_address_1 = input("Enter street address: ")
    zip_code = input("Enter zip code: ")
    # run(street_address_1, zip_code)
    run(playwright)
