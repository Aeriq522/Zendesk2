import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


def CRUD():
    # Connection Later
    def connection():
        conn = pymysql.connect(
            host=
        )
    
    
    
    # MAIN GUI
    root = Tk()
    root.title("Student Registration System")
    root.geometry("1080x720")
    my_tree = ttk.Treeview(root)
    
    # Functions later
    
    
    
    # GUI
    label=Label(root, text="Student Registration System (CRUD MATRIX)", font=("Arial Bold",30))
    label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)
    
    # Labels GUI
    studidLabel = Label(root, text="Student ID", font=("Arial", 15))
    fnameLabel = Label(root, text="First Name", font=("Arial", 15))
    lnameLabel = Label(root, text="Last Name", font=("Arial", 15))
    addressLabel = Label(root, text="Address", font=("Arial", 15))
    phoneLabel = Label(root, text="Phone", font=("Arial", 15))
    
    studidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
    fnameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
    lnameLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
    addressLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
    phoneLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)
    
    # Text Variable Later
    studIDEntry = Entry(root, width=55, bd=5, font=("Arial",15))
    fname = Entry(root, width=55, bd=5, font=("Arial",15))
    lname = Entry(root, width=55, bd=5, font=("Arial",15))
    addressEntry = Entry(root, width=55, bd=5, font=("Arial",15))
    phoneEntry = Entry(root, width=55, bd=5, font=("Arial",15))
    
    
    studIDEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
    fname.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
    lname.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
    addressEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
    phoneEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)
    
    
    addBtn = Button(root, text="Add", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg='#84F894')
    updateBtn = Button(root, text="Update", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg='#84E8F8')
    deleteBtn = Button(root, text="Delete", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg='#FF9999')
    searchBtn = Button(root, text="Search", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg='#F4FE82')
    resetBtn = Button(root, text="Reset", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg='#F398FF')
    selectBtn = Button(root, text="Select", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg='#EEEEEE')
    
    addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
    updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
    deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
    searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
    resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
    selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)
    
    
    style=ttk.Style()
    style.configure("TreeView.Heading", font=('Arial',15))
    my_tree['columns'] = ("Stud ID", "FirstName", "LastName", "Address", "Phone")
    
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Stud ID", anchor=W, width=170)
    my_tree.column("FirstName", anchor=W, width=150)
    my_tree.column("LastName", anchor=W, width=150)
    my_tree.column("Address", anchor=W, width=160)
    my_tree.column("Phone", anchor=W, width=150)
    
    my_tree.heading("Stud ID", text="Student ID", anchor=W)
    my_tree.heading("FirstName", text="FirstName", anchor=W)
    my_tree.heading("LastName", text="LastName", anchor=W)
    my_tree.heading("Address", text="Address", anchor=W)
    my_tree.heading("Phone", text="Phone", anchor=W)
    
    my_tree.column
    
    
    
    
    
    
  
    

    
    root.mainloop()




CRUD()