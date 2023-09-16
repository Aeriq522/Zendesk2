import os
from tkinter import Tk, Label, Button, Entry, filedialog
from PIL import Image, ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD
from pathlib import Path

# Define the folder path containing your images
folder_path = "C:/Users/Erik Sanchez/Downloads/DelRay"

def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    update_image_files()
    show_next_image()
    
    # Update the window title with the folder name
    folder_name = os.path.basename(folder_path)
    root.title(f"Image Viewer - {folder_name}")

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
image_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)  # Adjust row, column, and other options as needed


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
        
        
# Initialize current image index
current_image = 0

# Function to rename the dropped image
def rename_image():
    global current_image
    
    if 0 <= current_image < len(image_files):
        # Get the user input for the new name
        new_name = new_name_entry.get()
        
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
            
# Function to rename the dropped image
def rename_all_images(): 
    global image_files
    # Get the user input for the new name
    new_name = new_name_entry.get()
    
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
    
# Label and Entry for user input (new name)
new_name_label = Label(root, text="Enter a new name:")
new_name_label.grid(row=1, column=0, columnspan=3, pady=5)
new_name_entry = Entry(root)
new_name_entry.grid(row=2, column=0, columnspan=3, pady=2)

# Button to select the folder containing images
select_folder_button = Button(root, text="Select Folder", padx=20, pady=10, command=select_folder)
select_folder_button.grid(row=3, column=0, columnspan=3, pady=10)

# Button to rename to FACP the image
facp_button = Button(root, text="FACP", padx=20, pady=10, command=rename_image)
facp_button.grid(row=4, column=0, padx=10, pady=10)

# Button to rename the image
rename_button = Button(root, text="Rename Image", padx=20, pady=10, command=rename_image)
rename_button.grid(row=4, column=1, padx=10, pady=10)

# Button to rename all images
rename_all_button = Button(root, text="Rename All Images", padx=20, pady=10, command=rename_all_images)
rename_all_button.grid(row=4, column=2, padx=10, pady=10)

# Button to show the previous image
previous_button = Button(root, text="Previous Image", padx=20, pady=10, command=show_previous_image)
previous_button.grid(row=5, column=0, padx=10, pady=10)

# Button to show the next image
next_button = Button(root, text="Next Image", padx=20, pady=10, command=show_next_image)
next_button.grid(row=5, column=2, padx=10, pady=10)


# Start the tkinter main loop
root.mainloop()

