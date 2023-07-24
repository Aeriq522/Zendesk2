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

       # Processed data
            # number of elevators is a string, this converts it to an integer
            number_of_elevators = int(number_of_elevators)

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
                "[data-test-id=\"omni-header-subject\"]").fill(Ticket_title)
            page.locator(
                "[data-test-id=\"ticket-footer-macro-menu-autocomplete-input\"]").get_by_text("Apply macro").click()
            page.locator("#downshift-4-item-4").click()
            page.locator(
                "[data-test-id=\"omnicomposer-rich-text-ckeditor\"]").click()
            page.get_by_text("Site Survey:").click()

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
        #     page.get_by_role("combobox", name="Followers").click()
        #     page.get_by_placeholder("search agents").click()
        #     page.get_by_placeholder("search agents").fill("ht")
        #     page.locator("[data-test-id=\"ticket-fields-collaborators-contact-card\"]").click()
        #     page.get_by_role("combobox", name="Followers").fill("chris")
        #     page.locator("[data-test-id=\"ticket-fields-collaborators-contact-card\"]").click()

        # Get the date to follow up on
            page.get_by_placeholder("e.g. October 1, 2008").click()
            page.get_by_placeholder("e.g. October 1, 2008").fill(
                followup_date_string)

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
            page.get_by_text("Submit as Pending").click()

        # # Return to the views page
        #     page.locator("[data-test-id=\"views_icon\"]").click()


            Ticket_Number_Value = "header-tab-subtitle"
        # Assuming page.locator("[data-test-id=\"header-tab-subtitle\"]") returns a list of elements
            elements = page.get_by_test_id(Ticket_Number_Value)

            # Create a list to store the Ticket_Numbers
            Ticket_Numbers = []

            # Extract the text from each element and add it to the Ticket_Numbers list
            for element in elements:
                Ticket_Numbers.append(element.text)

            # Now Ticket_Numbers contains all values in elements with data-test-id="header-tab-subtitle"
            print(Ticket_Numbers)

            # Load the original CSV data into csv_data
            csv_file_path = "C:/Users/eriks/OneDrive/Desktop/Coding/Python Scripts/Zendesk/tickets.csv"

            with open(csv_file_path, "r") as csvfile:
                csv_reader = csv.reader(csvfile)
                csv_data = list(csv_reader)

            # element = page.get_by_role("cell", name=Ticket_title)
            # if element:
            #     Ticket_Number = element.get_attribute("name")

        # Update the value in the corresponding row (assuming row 18 here)
            row_index_to_update = 18  # Since list index is 0-based, row 18 is at index 17

            if 0 <= row_index_to_update < len(csv_data):
                csv_data[row_index_to_update] = Ticket_Numbers
            else:
                print("Invalid row index.")

            # Write the updated csv_data back to the CSV file
            csv_file_path = "C:/Users/eriks/OneDrive/Desktop/Coding/Python Scripts/Zendesk/tickets.csv"

            with open(csv_file_path, "w", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(csv_data)

       # Close the browser
            context.close()
            browser.close()


with sync_playwright() as playwright:
    run(playwright)
