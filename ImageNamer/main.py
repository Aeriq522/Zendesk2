import os
from tkinter import Tk, Label, Button, Entry, filedialog
from PIL import Image, ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD
from pathlib import Path

# Define the folder path containing your images
folder_path = "C:/Users/eriks/OneDrive"


# # Specify the input and output directories
input_directory = folder_path
output_directory = folder_path

# User Select the folder
# # Specify the input and output directories
input_directory = folder_path
output_directory = folder_path

# User Select the folder
def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    update_image_files()
    show_next_image()
    
    # Specify the input and output directories
    input_directory = folder_path
    output_directory = folder_path

    
    # Update the window title with the folder name
    folder_name = os.path.basename(folder_path)
    root.title(f"Currently Viewing --- {folder_name}")
    
    # # Specify the input and output directories based on the selected folder
    # input_directory = folder_path
    # output_directory = os.path.join(folder_path, "Processed")  # Add "Processed" subfolder
    
    # # Call the function to resize and process images
    # resize_and_process_images(input_directory, output_directory)


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
        a

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
                   
       
# Resize all images in the folder
def resize_and_process_images():
    global folder_path
    global current_image
    
    if 0 <= current_image < len(image_files):
        # Get the currently displayed image's file name
        current_image_file = image_files[current_image]
        
        # Check if the file is an image (you can add more image extensions if needed)
        if current_image_file.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
            # Specify the input and output directories based on the selected folder
            input_directory = folder_path
            output_directory = os.path.join(folder_path, "Processed")  # Add "Processed" subfolder
            
            # Create the output directory if it doesn't exist
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            # Open the image using Pillow
            with Image.open(os.path.join(input_directory, current_image_file)) as img:
                # Calculate the new width and height (60% of the original size)
                width, height = img.size
                new_width = int(width * 0.6)
                new_height = int(height * 0.6)

                # Resize the image to the new dimensions using BILINEAR filter
                resized_img = img.resize((new_width, new_height), Image.BILINEAR)

                # Save the resized image to the output directory
                output_path = os.path.join(output_directory, current_image_file)
                resized_img.save(output_path)
                print(f"Resized {current_image_file} to {new_width}x{new_height} and saved to {output_path}")

    print("All images resized.")  
            


    
# Label and Entry for user input (new name)
new_name_label = Label(root, text="Enter a new name:")
new_name_label.grid(row=4, column=12, columnspan=4, pady=5)
new_name_entry = Entry(root)
new_name_entry.grid(row=5, column=12, columnspan=4, pady=2)

# Button to select the folder containing images
select_folder_button = Button(root, text="Select Folder", padx=20, pady=10, command=select_folder)
select_folder_button.grid(row=7, column=12, columnspan=4, pady=10)

# # Button to rename to FACP
resize_button = Button(root, text="Resize 60%", padx=20, pady=10, command=resize_and_process_images)
resize_button.grid(row=0, column=12, columnspan=4, pady=10, padx=10)



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



