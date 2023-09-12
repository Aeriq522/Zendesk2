import os
from tkinter import Tk, Label, Button, Entry
from PIL import Image, ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD
from pathlib import Path

# Define the folder path containing your images
folder_path = "C:/Users/eriks/OneDrive/Pictures/Screenshots"

# Get a list of image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".png", ".gif"))]

# Create a tkinter window
root = TkinterDnD.Tk()
root.title("Image Viewer")

# Create a label to display the images
image_label = Label(root)
image_label.pack()

# Function to display the next image
def show_next_image():
    global current_image
    # Function to display the next image or a dropped image
def show_next_image():
    global current_image
    if len(dropped_files) > 0:
        # Display the next dropped image
        if 0 <= current_image < len(dropped_files) - 1:
            current_image += 1
        else:
            current_image = 0
        img = Image.open(dropped_files[current_image])
        img = img.resize((500, 500))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
    elif current_image < len(image_files):
        # Display the next image from the folder
        img = Image.open(os.path.join(folder_path, image_files[current_image]))
        img = img.resize((500, 500))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
        current_image += 1

# Function to display the previous image or a dropped image
def show_previous_image():
    global current_image
    if len(dropped_files) > 0:
        # Display the previous dropped image
        if 0 < current_image < len(dropped_files):
            current_image -= 1
        else:
            current_image = len(dropped_files) - 1
        img = Image.open(dropped_files[current_image])
        img = img.resize((500, 500))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
    elif current_image < len(image_files):
        # Display the previous image from the folder
        current_image -= 1
        if current_image < 0:
            current_image = len(image_files) - 1
        img = Image.open(os.path.join(folder_path, image_files[current_image]))
        img = img.resize((500, 500))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
# Initialize current image index
current_image = 0

# Function to rename the dropped image
def rename_image():
    # Get the user input for the new name
    new_name = new_name_entry.get()

    # print(new_name)
    # print(dropped_files)
    
    # Process each dropped file
    for file_path in dropped_files:
        # Check if the file is an image (you can add more image extensions if needed)
        if file_path.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
            # Rename the image
            file_name = os.path.basename(file_path)
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = new_name + file_extension
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

            # Rename the file using os.rename
            os.rename(file_path, new_file_path)
            print(new_file_path)
            
        # Update the text field with the new file path
        new_name_entry.delete(0, 'end')

    
    # Update the list of image files
    global image_files
    image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png", ".gif"))]

# Label and Entry for user input (new name)
new_name_label = Label(root, text="Enter a new name:")
new_name_label.pack()
new_name_entry = Entry(root)
new_name_entry.pack()


# Button to initiate the renaming process
rename_button = Button(root, text="Rename Images", command=rename_image)
rename_button.pack()

# List to store dropped file paths
dropped_files = []


# Function to handle file drops
def drop(event):
    # print(event.data)
    file_path = event.data
    
    # Remove curly braces from the file path string
    file_path = file_path.strip('{}')
    # Change Name of the file to whatever name user entered
    dropped_files.append(file_path)
    global image_files
    image_files = file_path
        


# Button to show the next image
next_button = Button(root, text="Next Image", padx=20, pady=10, command=show_next_image)
next_button.pack()
previous_button = Button(root, text="Previous Image", padx=20, pady=10, command=show_previous_image)
previous_button.pack()

# Start by displaying the first image
show_next_image()

# Bind the drop function to the window
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# Start the tkinter main loop
root.mainloop()
