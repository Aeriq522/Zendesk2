import os
from tkinter import Tk, Label, Entry, Button
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
from pathlib import Path

# Create a tkinter window with drag-and-drop support
root = TkinterDnD.Tk()
root.title("Image Renamer")

# Set the window's size (width x height)
root.geometry("600x400")  # Change these dimensions as needed

# Function to rename the dropped image
def rename_image():
    # Get the user input for the new name
    new_name = new_name_entry.get()
    new_name = new_name_entry_2.get()
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
            
            #    # Update the text field with the new file path
            # new_name_entry.delete(0, 'end')
            # new_name_entry.insert(0, new_file_path)

    # Reset the input field
    new_name_entry.delete(0, 'end')
    new_name_entry.insert(0, new_file_path)

# Label and Entry for user input (new name)
new_name_label = Label(root, text="Enter a new name:")
new_name_label.pack()
new_name_entry = Entry(root)
new_name_entry.pack()
new_name_entry_2 = Entry(root)
new_name_entry_2.pack()

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
        
# Bind the drop function to the window
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# Start the tkinter main loop
root.mainloop()


#  folder_name = input("Enter folder name: ")
#  screenshot_path = os.path.join(folder_name, "GoogleViewScreenshot.png")
