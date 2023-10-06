from PIL import Image
import os

# Specify the input and output directories
input_directory = "C:/Users/eriks/Downloads/ImageResize"
output_directory = "C:/Users/eriks/Downloads/ImageResize/Processed"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    
    
# Iterate through the files in the input directory
for filename in os.listdir(input_directory):
    # Check if the file is an image (you can add more image formats as needed)
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        # Open the image using Pillow
        with Image.open(os.path.join(input_directory, filename)) as img:
            # Calculate the new width and height (60% of the original size)
            width, height = img.size
            new_width = int(width * 0.6)
            new_height = int(height * 0.6)
            
            # Resize the image to the new dimensions using BILINEAR filter
            resized_img = img.resize((new_width, new_height), Image.BILINEAR)
            
            # Save the resized image to the output directory
            output_path = os.path.join(output_directory, filename)
            resized_img.save(output_path)
            print(f"Resized {filename} to {new_width}x{new_height} and saved to {output_path}")

print("All images resized.")
