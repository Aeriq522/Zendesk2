import csv
import os
from datetime import datetime, timedelta
import time
# from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright, expect


# # Load environment variables from .env file
# load_dotenv()

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
            
            # Define a function to process a single row from the CSV file
            def process_row(row):
                Ticket_title = row[1]
                Location = row[2]
                Carrier = row[3]
                Download = row[4]
                Upload = row[5]
                Mount = row[6]
                Facp = row[7]
                Primary = row[8]
                Secondary = row[9]
                Burglar = row[10]
                Intercomm = row[11]
                number_of_elevators = row[12]
                Elevator = row[13]
                Elevator_notes = row[14]
                Fax = row[15]
                Total_dids = row[16]
                Notes = row[17]
                # Extract other data from the row as needed

       # Processed data
            # number of elevators is a string, this converts it to an integer
            number_of_elevators = int(number_of_elevators)

       # Open the browser
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            
            try:
                page.goto(
                "https://machnetworks.zendesk.com/agent/filters/360205088072")
                page.goto("https://machnetworks.zendesk.com/access/unauthenticated?return_to=https%3A%2F%2Fmachnetworks.zendesk.com%2Fagent%2Ffilters%2F360205088072")
                page.goto("https://machnetworks.zendesk.com/auth/v2/login/signin?return_to=https%3A%2F%2Fmachnetworks.zendesk.com%2Fagent%2Ffilters%2F360205088072&theme=hc&locale=1&brand_id=360005574752&auth_origin=360005574752%2Cfalse%2Ctrue&role=agent")
                page.get_by_label("Email").click()
                page.get_by_label("Email").fill("esanchez@machnetworks.com")
                page.get_by_label("Password").click()
                page.get_by_label("Password").fill("Esm522@@Zendesk")
                page.get_by_role("button", name="Sign in").click()
                
                # Open the CSV file for reading
                with open('Create Site Survey/tickets.csv', newline='') as csvfile:
                    csvreader = csv.reader(csvfile)
                    next(csvreader)  # Skip the header row if it exists

                    # Iterate over each row in the CSV file
                    for row in csvreader:
                        process_row(row)  # Process the current row
                        print('Hello from csv reader')
                        # Adding a new ticket
                        page.locator(
                            "[data-test-id=\"header-toolbar-add-menu-button\"]").hover()
                        page.locator(
                            "[data-test-id=\"header-toolbar-add-menu-new-ticket\"]").click()

                        # Create a new ticket from template
                        page.locator("[data-test-id=\"omni-header-subject\"]").click()
                        page.locator(
                            "[data-test-id=\"omni-header-subject\"]").fill(Ticket_title)
                        page.locator(
                            "[data-test-id=\"ticket-footer-macro-menu-autocomplete-input\"]").get_by_text("Apply macro").click()

                        
                        
                        if row[0].startswith('Site Survey'):
                            page.locator("[data-test-id=\"ticket-footer-macro-menu-autocomplete-input\"]").get_by_label("Apply macro autocomplete menu").click()
                            page.locator("[data-test-id=\"ticket-footer-macro-menu-autocomplete-input\"]").get_by_label("Apply macro autocomplete menu").fill("Site")
                            page.locator("[data-test-id=\"ticket-footer-macro-menu-autocomplete-input\"]").get_by_label("Apply macro autocomplete menu").fill("Site Survey")
                            
                            time.sleep(1)  # Add a 5-second delay
                            page.locator("[data-test-id=\"ticket-footer-macro-menu-autocomplete-input\"]").get_by_label("Apply macro autocomplete menu").press("Enter")


                # Fill the form
                        page.get_by_text("{Location}").fill(f"Location: {Location}")
                        page.get_by_text("{Carrier}").fill(
                            f"Carrier: {Carrier} | Download: {Download} Mbps | Upload: {Upload} Mbps |")
                        page.get_by_text("{Mount}").fill(f"- {Mount}")
                        page.get_by_text("{FACP}").fill(
                            f"FACP: {Facp} | Primary Number: {Primary} | Secondary Number: {Secondary} |")
                        page.get_by_text("{Burglar}").fill(f"Burglar Panel: {Burglar}")
                        page.get_by_text("{Intercomm}").fill(f"Intercom: {Intercomm}")

                    # Check for number of elevators
                        # And then adjust the Reports Number of Elevators
                        page.get_by_text("{Elevator}").fill(
                            f"{number_of_elevators} Elevator : {Elevator}")
                        page.get_by_text("{Elevator Notes}").fill(
                            f"Elevator Notes: {Elevator_notes}")

                        # Continue filling the form
                        page.get_by_text("{Fax}").fill(f"Fax: {Fax}")
                        page.get_by_text("{Total DiDs}").fill(
                            f"Total Number of DiDs: {Total_dids}")
                        page.get_by_text("{Notes}").fill(f"Notes: {Notes}")

                # Submit ticket requester, assignee, and submit ticket
                        page.get_by_placeholder("search name or contact info").fill("er")
                        page.locator(
                            "[data-test-id=\"ticket-system-field-requester-menu\"]").get_by_text("ik Sanchez").click()
                        page.locator(
                            "[data-test-id=\"assignee-field-take-it-button\"]").click()

                    # # Add followers
                        page.get_by_role("combobox", name="Followers").click()
                        page.get_by_placeholder("search agents").click()
                        page.get_by_placeholder("search agents").fill("ht")
                        page.locator("[data-test-id=\"ticket-fields-collaborators-contact-card\"]").click()
                        page.get_by_role("combobox", name="Followers").fill("chris")
                        page.locator("[data-test-id=\"ticket-fields-collaborators-contact-card\"]").click()

                    # Get the date to follow up on
                        # page.get_by_placeholder("e.g. October 1, 2008").click()
                        # page.get_by_placeholder("e.g. October 1, 2008").fill(
                        #     followup_date_string)

                    # Ticket Priority
                        page.locator(
                            "[data-test-id=\"ticket-fields-priority-select\"]").click()
                        page.get_by_role("option", name="Normal").click()

                    # Ticket Type
                        page.locator(
                            "[data-test-id=\"ticket-form-field-dropdown-button\"] svg").click()
                        page.get_by_role("option", name="Field Install").click()
                        page.locator(
                            "[data-test-id=\"ticket-form-field-dropdown-field-8323312621837\"] svg").click()
                        page.get_by_text("Site Survey WO").click()

                    # Ticket Resolution
                        page.locator(
                            "[data-test-id=\"ticket-fields-multiline-field\"]").click()
                        page.locator("[data-test-id=\"ticket-fields-multiline-field\"]").fill(
                            "Site survey completed. Please see the attached for the site survey results.")

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
                        time.sleep(5)  # Add a 5-second delay
                        page.get_by_text("Submit as Pending").click()

                    # # # Return to the views page
                    #     page.locator("[data-test-id=\"views_icon\"]").click()
                    #     time.sleep(3)  # Add a 5-second delay


            finally:
        # Close the browser
                context.close()
                browser.close()


with sync_playwright() as playwright:
    run(playwright)
