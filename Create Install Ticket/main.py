import csv
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright, expect
from colorama import init, Style

# Initialize colorama to work on Windows as well
init()


# Load environment variables from .env file
load_dotenv()

# Access the secrets using os.getenv()
USERNAME_FOR_ZENDESK = os.getenv("USERNAME_FOR_ZENDESK")
PASSWORD_FOR_ZENDESK = os.getenv("PASSWORD_FOR_ZENDESK")


# Get the current date and time
current_date_time = datetime.now()

# Get today's date as a string in the format "MM/DD/YYYY"
current_date_string = current_date_time.strftime("%m/%d/%Y")

# Example: "MM/DD/YYYY"


def add_two_days(date_string):
    current_date = datetime.strptime(date_string, "%m/%d/%Y")
    followup_date = current_date + timedelta(days=2)
    followup_date_string = followup_date.strftime("%m/%d/%Y")
    return followup_date_string


# Get the follow-up date (2 days from today) as a string
followup_date_string = add_two_days(current_date_string)

# print("Today's Date: ", current_date_string)
# print("Follow-up Date: ", followup_date_string)


def run(playwright: Playwright) -> None:

    with open('Create Site Survey/tickets.csv', 'r') as csvfile:
       # try:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
           # Headers from the csv file
            Ticket_Name = row[0]
            Status = row[1]
            Install_Location = row[2]
            Carrier = row[3]
            Download = row[4]
            Upload = row[5]
            Latency = row[6]
            Jitter = row[7]
            ATA_Type = row[26]
            Equipment_1 = row[8]
            Number_1 = row[9]
            Equipment_2 = row[10]
            Number_2 = row[11]
            Equipment_3 = row[12]
            Number_3 = row[13]
            Equipment_4 = row[14]
            Number_4 = row[15]
            Equipment_5 = row[16]
            Number_5 = row[17]
            Equipment_6 = row[18]
            Number_6 = row[19]
            Equipment_7 = row[20]
            Number_7 = row[21]
            Equipment_8 = row[22]
            Number_8 = row[23]
            Notes = row[24]
            Total_DiDs_Installed = row[25]
            In_Production = row[26]


       # Open the browser
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(
                "https://machnetworks.zendesk.com/agent/filters/360205088072")
            page.goto("https://machnetworks.zendesk.com/access/unauthenticated?return_to=https%3A%2F%2Fmachnetworks.zendesk.com%2Fagent%2Ffilters%2F360205088072")
            page.goto("https://machnetworks.zendesk.com/auth/v2/login/signin?return_to=https%3A%2F%2Fmachnetworks.zendesk.com%2Fagent%2Ffilters%2F360205088072&theme=hc&locale=1&brand_id=360005574752&auth_origin=360005574752%2Cfalse%2Ctrue&role=agent")
            page.get_by_label("Email").click()
            page.get_by_label("Email").fill("esanchez@machnetworks.com")
            page.get_by_label("Password").click()
            page.get_by_label("Password").fill("Esm522@@Zendesk")
            page.get_by_role("button", name="Sign in").click()

       # Adding a new ticket
            page.locator(
                "[data-test-id=\"header-toolbar-add-menu-button\"]").hover()
            page.locator(
                "[data-test-id=\"header-toolbar-add-menu-new-ticket\"]").click()

       # Create a new ticket from template
            page.locator("[data-test-id=\"omni-header-subject\"]").click()
            page.locator(
                "[data-test-id=\"omni-header-subject\"]").fill(Ticket_Name)
            page.locator(
                "[data-test-id=\"ticket-footer-macro-menu-autocomplete-input\"]").get_by_text("Apply macro").click()
            page.locator("#downshift-3-item-3").click()
            page.locator(
                "[data-test-id=\"omnicomposer-rich-text-ckeditor\"]").click()
            page.get_by_text("Install Ticket 4 Port:").click()

       # Fill the form
            page.get_by_text("{Status}").fill(f"Installation: {Style.BRIGHT}{Status}{Style.RESET_ALL}")
            page.get_by_text("{Carrier}").fill(f"Carrier: {Carrier} | Download: {Download} Mbps | Upload: {Upload} Mbps |\n Latency: {Latency} ms | Jitter: {Jitter} ms |")
            page.get_by_text("{Install_Location}").fill(f"Installation Location: {Install_Location}")
            page.get_by_text("{ATA_Type}").fill(f"{ATA_Type} 4 Port ATA.")
            page.get_by_text("{Equipment_1}").fill(f"{Equipment_1}:")
            page.get_by_text("{Number_1}").fill(f"     - Line 1: {Number_1}")
            page.get_by_text("{Equipment_2}").fill(f"{Equipment_2}:")
            page.get_by_text("{Number_2}").fill(f"     - Line 2: {Number_2}")
            page.get_by_text("{Equipment_3}").fill(f"{Equipment_3}:")
            page.get_by_text("{Number_3}").fill(f"     - Line 3: {Number_3}")
            page.get_by_text("{Equipment_4}").fill(f"{Equipment_4}:")
            page.get_by_text("{Number_4}").fill(f"     - Line 4: {Number_4}")
            page.get_by_text("{Total_DiDs_Installed}}").fill(f"{Total_DiDs_Installed} DiDs Installed.")
            page.get_by_text("{Notes}}").fill(f"{Notes}")
            
        # Assign production status based on In_Production
            if In_Production == "True":
                page.get_by_text("{In_Production}}").fill(f"This site is in production.")
            else:
                page.get_by_text("{In_Production}}").fill(f"This site is not in production.")

    # Filling out the ticket forms
       # Submit ticket requester, assignee, and submit ticket
            page.get_by_placeholder("search name or contact info").fill("er")
            page.locator(
                "[data-test-id=\"ticket-system-field-requester-menu\"]").get_by_text("ik Sanchez").click()
            page.locator(
                "[data-test-id=\"assignee-field-take-it-button\"]").click()
            
        # Get the date to follow up on
            page.get_by_placeholder("e.g. October 1, 2008").click()
            page.get_by_placeholder("e.g. October 1, 2008").fill(
                followup_date_string)

        # Ticket Type
            page.locator(
                "[data-test-id=\"ticket-form-field-dropdown-button\"] svg").click()
            page.get_by_role("option", name="Field Install").click()
            page.locator(
                "[data-test-id=\"ticket-form-field-dropdown-field-8323312621837\"] svg").click()

        # Ticket Resolution
            page.locator(
                "[data-test-id=\"ticket-fields-multiline-field\"]").click()
            page.locator("[data-test-id=\"ticket-fields-multiline-field\"]").fill(
                "Installation completed. Please see the attached for the installation results.")






#############################################################################                 Need to check how to conditionally add a new ticket to the ticket system depending on if the lenth of Total_DiDs_Installed is greater than 4, so i can have a 4 and 8 port ticket









            page.locator(
                "[data-test-id=\"ticket-composer-toolbar-link-button\"]").click()
            page.locator(
                "[data-test-id=\"link-modal-link-input\"]").fill(Fieldnation_Workorder_Link)
            page.locator("[data-test-id=\"link-modal-text-input\"]").click()
            page.locator(
                "[data-test-id=\"link-modal-text-input\"]").fill("\n Field Nation Work Order")
            page.locator("[data-test-id=\"link-modal-add-button\"]").click()

        # Submit Ticket
            page.locator(
                "[data-test-id=\"submit_button-menu-button\"]").hover()
            page.locator(
                "[data-test-id=\"submit_button-menu-button\"]").click()
            page.get_by_text("Submit as Pending").click()

        # # Return to the views page
            # page.locator("[data-test-id=\"views_icon\"]").click()


       # Close the browser
            context.close()
            browser.close()


with sync_playwright() as playwright:
    run(playwright)
