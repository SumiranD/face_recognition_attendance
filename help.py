from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1370x768+0+0")
        self.root.title("Help Desk")

        # Title label
        title_lbl = Label(self.root, text="Help Desk", font=("Arial", 30, "bold"), bg="silver", fg="black")
        title_lbl.place(x=0, y=0, width=1370, height=75)

        # Frame for form content
        form_frame = Frame(self.root, bg="white")
        form_frame.place(x=50, y=100, width=1270, height=600)

        # Name label and entry
        name_lbl = Label(form_frame, text="Name", font=("Arial", 16), bg="white", fg="black")
        name_lbl.place(x=50, y=50)
        self.name_entry = Entry(form_frame, font=("Arial", 16), bd=2, relief=SOLID)
        self.name_entry.place(x=200, y=50, width=400)

        # Email label and entry
        email_lbl = Label(form_frame, text="Email", font=("Arial", 16), bg="white", fg="black")
        email_lbl.place(x=50, y=100)
        self.email_entry = Entry(form_frame, font=("Arial", 16), bd=2, relief=SOLID)
        self.email_entry.place(x=200, y=100, width=400)

        # Issue description label and text box
        issue_lbl = Label(form_frame, text="Issue", font=("Arial", 16), bg="white", fg="black")
        issue_lbl.place(x=50, y=150)
        self.issue_text = Text(form_frame, font=("Arial", 16), bd=2, relief=SOLID, height=6, width=40)
        self.issue_text.place(x=200, y=150)

        # Submit button
        submit_btn = Button(form_frame, text="Submit", font=("Arial", 16, "bold"), bg="green", fg="white", command=self.submit_ticket)
        submit_btn.place(x=200, y=450)

    def submit_ticket(self):
        # Get user input
        name = self.name_entry.get()
        email = self.email_entry.get()
        issue = self.issue_text.get("1.0", END).strip()

        # If all fields are filled
        if name and email and issue:
            # Show a success message (you could also send this data to a database here)
            messagebox.showinfo("Success", "Your help request has been submitted successfully!")
        else:
            # Show an error message if some fields are missing
            messagebox.showerror("Error", "Please fill all the fields.")

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
