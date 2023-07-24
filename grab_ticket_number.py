import csv
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright, expect


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

    with open('tickets.csv', 'r') as csvfile:
       # try:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
           # Headers from the csv file
            Ticket_title = row[0]
            Location = row[1]
            Carrier = row[2]
            Download = row[3]
            Upload = row[4]
            Mount = row[5]
            Facp = row[6]
            Primary = row[7]
            Secondary = row[8]
            Burglar = row[9]
            Intercomm = row[10]
            number_of_elevators = row[11]
            Elevator = row[12]
            Elevator_notes = row[13]
            Fax = row[14]
            Total_dids = row[15]
            Notes = row[16]
            Fieldnation_Workorder_Link = row[17]

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
            
        # Open Ticket To Search
            page.get_by_role("cell", name="Shipped Devices and Accessories 7/14/23").locator("div").nth(1).click()
            page.locator("[data-test-id=\"header-tab\"]").click()
            
        # Get the ticket number
            ticket_number = ""

            # Find the element with the class "header-tab-subtitle" and get its first occurrence
            ticket_locator = page.locator("[data-test-id=\"header-tab-subtitle\"]")
            ticket_element = ticket_locator.nth(0)
            
            # Check if the element exists before getting the text
            if ticket_element:
                ticket_number = ticket_element.inner_text()

            # Now you can use the stored ticket_number variable later in the code
            # For example:
            print("Ticket number:", ticket_number)
                        
         
            
            















            print("Script Completed")

# Close the browser
            context.close()
            browser.close()


with sync_playwright() as playwright:
    run(playwright)
