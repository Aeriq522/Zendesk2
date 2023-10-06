import tkinter as tk
import imageviewer  # Import the imageviewer module
import new_window



def APP_Gui():

    # Function to switch to the image renamer screen
    def show_image_renamer():
        main_menu.grid_forget()  # Hide the main menu frame
        image_namer.grid(row=0, column=0, sticky="nsew")  # Show the image renamer frame
        
        # Call the function or code from the imageviewer module
        imageviewer.run_imageviewer()  # Replace this with the actual function or code you want to run


    # Function to go back to the main menu
    def show_main_menu():
        image_namer.grid_forget()  # Hide the image renamer frame
        main_menu.grid(row=0, column=0, sticky="nsew")  # Show the main menu frame

    # Function to go back to the main menu
    def show_main_menueeeexxxxxxxxssssssaaaaaammmmppppllllllleeeee():
        main_menu.grid_forget()  # Hide the main menu frame
        image_namer.grid(row=0, column=0, sticky="nsew")  # Show the image renamer frame
        
        # Call the function or code from the imageviewer module
        new_window.run_new_window()  # Replace this with the actual function or code you want to run

    root = tk.Tk()
    root.title("Work Application 2.1")

    # Create a frame for the main menu
    main_menu = tk.Frame(root)
    main_menu.grid(row=0, column=0, sticky="nsew")

    # Create a "Image Renamer" button to go to the image renamer screen
    next_button = tk.Button(main_menu, text="Image Renamer", command=show_image_renamer)
    next_button.grid(row=0, column=0, padx=20, pady=10)

    # Create a "Image Renamer" button to go to the image renamer screen
    next_button = tk.Button(main_menu, text="Image Renamer", command=show_main_menueeeexxxxxxxxssssssaaaaaammmmppppllllllleeeee)
    next_button.grid(row=0, column=1, padx=20, pady=10)

    # Create a frame for the image renamer screen
    image_namer = tk.Frame(root)

    # Create a "Back" button on the image renamer screen to go back to the main menu
    back_button = tk.Button(image_namer, text="Back to Main Menu", command=show_main_menu)
    back_button.grid(row=0, column=0, padx=20, pady=10)

    # Create unique widgets for the image renamer screen
    image_label = tk.Label(image_namer, text="Enter Image Name:")
    image_label.grid(row=1, column=0, padx=20, pady=10)
    image_entry = tk.Entry(image_namer)
    image_entry.grid(row=1, column=1, padx=20, pady=10)

    rename_button = tk.Button(image_namer, text="Rename Image")
    rename_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

    # Create unique widgets for the main menu
    width_label = tk.Label(main_menu, text="Width:")
    width_label.grid(row=1, column=0, padx=20, pady=10)
    width_entry = tk.Entry(main_menu)
    width_entry.grid(row=1, column=1, padx=20, pady=10)

    height_label = tk.Label(main_menu, text="Height:")
    height_label.grid(row=2, column=0, padx=20, pady=10)
    height_entry = tk.Entry(main_menu)
    height_entry.grid(row=2, column=1, padx=20, pady=10)

    # Initially, display the main menu
    show_main_menu()

    # Configure column and row weights for resizing
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.mainloop()
    
APP_Gui()
