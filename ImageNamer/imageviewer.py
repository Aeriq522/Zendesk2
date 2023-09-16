import os
from tkinter import Tk, Label, Button, Entry, filedialog
from PIL import Image, ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD
from pathlib import Path

# Define the folder path containing your images
folder_path = "C:/Users/eriks/OneDrive"

# User Select the folder
def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    update_image_files()
    show_next_image()
    
    # Update the window title with the folder name
    folder_name = os.path.basename(folder_path)
    root.title(f"Currently Viewing --- {folder_name}")

# Initialize a global list to store image files
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".png", ".gif", ".jpeg"))]

# Get a list of image files in the folder
def update_image_files():
    global image_files
    image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".png", ".gif", ".jpeg"))]

# Initialize current image index
current_image = 0

# Create a tkinter window
root = TkinterDnD.Tk()
root.title("Image Viewer")

# Create a label to display the images
image_label = Label(root)
image_label.grid(row=2, column=12, columnspan=4, pady=10, padx=10)  # Adjust row, column, and other options as needed

# Change the image
def show_next_image():
    global current_image
    if len(image_files) > 0:
        # Increase the current image index
        current_image = (current_image + 1) % len(image_files)
        img = Image.open(os.path.join(folder_path, image_files[current_image]))
        img = img.resize((500, 500))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo

        # Set the new image file name in the new_name_entry
        current_image_file = image_files[current_image]
        new_name_entry.delete(0, 'end')
        new_name_entry.insert(0, os.path.splitext(current_image_file)[0])
        
          # Update the window title
        root.title(f"Image Viewer {current_image_file}")
        
def show_previous_image():
    global current_image
    if len(image_files) > 0:
        # Decrease the current image index
        current_image = (current_image - 1) % len(image_files)
        img = Image.open(os.path.join(folder_path, image_files[current_image]))
        img = img.resize((500, 500))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo

        # Set the new image file name in the new_name_entry
        current_image_file = image_files[current_image]
        new_name_entry.delete(0, 'end')
        new_name_entry.insert(0, os.path.splitext(current_image_file)[0])
        
          # Update the window title
        root.title(f"Image Viewer {current_image_file}")
        

# Function to rename the image based off the user input
def rename_image():
    global current_image
    
    if 0 <= current_image < len(image_files):
        # Get the user input for the new name
        new_name = new_name_entry.get()
        
        # If new_name is empty, set it to a default value
        if not new_name:
            new_name = "test"
        
        # Get the currently displayed image's file name
        current_image_file = image_files[current_image]
        
        # Check if the file is an image (you can add more image extensions if needed)
        if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()
             
# Rename all images to user input
def rename_all_images(): 
    global image_files
    # Get the user input for the new name
    new_name = new_name_entry.get()
    
    # If new_name is empty, set it to a default value
    if not new_name:
        new_name = "test"
    
    # Process each dropped file
    for file_name in image_files:
        # Check if the file is an image (you can add more image extensions if needed)
        if file_name.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            file_path = os.path.join(folder_path, file_name)

            # Rename the image
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(file_path, new_file_path)
            print(f"Renamed {file_name} to {new_file_name}")
            
    # Update the text field with the new file path
    new_name_entry.delete(0, 'end')

    # Update the list of image files
    update_image_files()
    
    # Change to the next image file
    show_next_image()
                   
# Function to rename the FACP image
def rename_image_FACP():
    global current_image
    new_name = "Fire Access Control Panel"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()

# Function to rename the FACP image
def rename_image_FACP_connections():
    global current_image
    new_name = "FACP Connections"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()

# Function to rename the Burglar Alarm image
def rename_image_burglar_alarm():
    global current_image
    new_name = "Burglar Alarm Panel"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()

# Function to rename the Burglar Alarm image
def rename_image_burglar_alarm_connections():
    global current_image
    new_name = "Burglar Alarm Connections"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()

# Function to rename the Elevator image
def rename_image_elevator():
    global current_image
    new_name = "Elevator"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image() 

# Function to rename the Elevator image
def rename_image_elevator_connections():
    global current_image
    new_name = "Elevator Connections"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image() 

# Function to rename the Intercom image
def rename_image_intercom():
    global current_image
    new_name = "Intercom"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()
            
# Function to rename the Intercom image
def rename_image_intercom_connections():
    global current_image
    new_name = "Intercom Connections"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()
              
# Function to rename the Phone image
def rename_image_landline_phone():
    global current_image
    new_name = "Phone"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()
      
# Function to rename the Phone image
def rename_image_landline_phone_connections():
    global current_image
    new_name = "Phone Connections"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()
                   
# Function to rename the 66-Block image
def rename_image_sixtysixblock():
    global current_image
    new_name = "66 Block"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()

# Function to rename the Path of Communication image
def rename_image_path():
    global current_image
    new_name = "Path of Communication"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()
            
# Function to rename the Path of Communication image
def rename_image_mounting_location():
    global current_image
    new_name = "Equipment Mounting Location"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()
            
# Function to rename the Path of Communication image
def rename_image_equipment():
    global current_image
    new_name = "Equipment"
        
    # Get the currently displayed image's file name
    current_image_file = image_files[current_image]
        
    # Check if the file is an image (you can add more image extensions if needed)
    if current_image_file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
            # Get the full path to the file
            current_image_path = os.path.join(folder_path, current_image_file)
            
            # Rename the image
            file_extension = os.path.splitext(current_image_file)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Check if the new file name already exists
            counter = 1
            while os.path.exists(new_file_path):
                # If the file already exists, add a suffix to make it unique
                new_file_name = f"{new_name} {counter}{file_extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                counter += 1

            # Rename the file using os.rename
            os.rename(current_image_path, new_file_path)
            print(f"Renamed {current_image_file} to {new_file_name}")
            
            # Update the text field with the new file path
            new_name_entry.delete(0, 'end')
            
            # Update the list of image files
            update_image_files()
                
            # Change to the next image file
            show_next_image()
            

    
# Label and Entry for user input (new name)
new_name_label = Label(root, text="Enter a new name:")
new_name_label.grid(row=4, column=12, columnspan=4, pady=5)
new_name_entry = Entry(root)
new_name_entry.grid(row=5, column=12, columnspan=4, pady=2)

# Button to select the folder containing images
select_folder_button = Button(root, text="Select Folder", padx=20, pady=10, command=select_folder)
select_folder_button.grid(row=7, column=12, columnspan=4, pady=10)



# Button to rename to FACP
facp_button = Button(root, text="Fire Alarm Panel", padx=20, pady=10, command=rename_image_FACP)
facp_button.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to FACP
facp_biscuit_jacks_button = Button(root, text="FACP Biscuit Jacks", padx=20, pady=10, command=rename_image_FACP_connections)
facp_biscuit_jacks_button.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Burglar Alarm
burglar_alarm_button = Button(root, text="Burglar Alarm", padx=20, pady=10, command=rename_image_burglar_alarm)
burglar_alarm_button.grid(row=0, column=4, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Burglar Alarm
burglar_alarm_connections_button = Button(root, text="Burglar Alarm Connections", padx=20, pady=10, command=rename_image_burglar_alarm_connections)
burglar_alarm_connections_button.grid(row=1, column=4, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Elevator
elevator_button = Button(root, text="Elevator", padx=20, pady=10, command=rename_image_elevator)
elevator_button.grid(row=0, column=16, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Elevator
elevator_connections_button = Button(root, text="Elevator Connections", padx=20, pady=10, command=rename_image_elevator_connections)
elevator_connections_button.grid(row=1, column=16, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Intercom Phone
intercom_button = Button(root, text="Intercom Phone", padx=20, pady=10, command=rename_image_intercom)
intercom_button.grid(row=0, column=20, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Intercom Phone
intercom_connections_button = Button(root, text="Intercom Connections", padx=20, pady=10, command=rename_image_intercom_connections)
intercom_connections_button.grid(row=1, column=20, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Landline Phone
landline_phone_button = Button(root, text="Landline Phone", padx=20, pady=10, command=rename_image_landline_phone)
landline_phone_button.grid(row=0, column=24, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Landline Phone
landline_phone_connections_button = Button(root, text="Phone Connections", padx=20, pady=10, command=rename_image_landline_phone_connections)
landline_phone_connections_button.grid(row=1, column=24, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Landline Phone
sixtysixblock_button = Button(root, text="66 Block", padx=20, pady=10, command=rename_image_sixtysixblock)
sixtysixblock_button.grid(row=0, column=8, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Landline Phone
path_button = Button(root, text="Path", padx=20, pady=10, command=rename_image_path)
path_button.grid(row=1, column=8, columnspan=4, padx=10, pady=10, sticky="ew")

# Button to rename to Landline Phone
mounting_location_button = Button(root, text="Mounting Location", padx=20, pady=10, command=rename_image_mounting_location)
mounting_location_button.grid(row=1, column=12, columnspan=4, pady=10, padx=10)

# Button to rename to Landline Phone
equipment_button = Button(root, text="Equipment", padx=20, pady=10, command=rename_image_equipment)
equipment_button.grid(row=0, column=12, columnspan=4, pady=10, padx=10)



# Button to rename the image
rename_button = Button(root, text="Rename Image", padx=20, pady=10, command=rename_image)
rename_button.grid(row=8, column=8,columnspan=4, padx=10, pady=10)

# Button to rename all images
rename_all_button = Button(root, text="Rename All Images", padx=20, pady=10, command=rename_all_images)
rename_all_button.grid(row=8, column=16,columnspan=4, padx=10, pady=10)

# Button to show the previous image
previous_button = Button(root, text="Previous Image", padx=20, pady=10, command=show_previous_image)
previous_button.grid(row=9, column=10, columnspan=4, padx=10, pady=10)

# Button to show the next image
next_button = Button(root, text="Next Image", padx=20, pady=10, command=show_next_image)
next_button.grid(row=9, column=14,columnspan=4,  padx=10, pady=10)


# Start the tkinter main loop
root.mainloop()

