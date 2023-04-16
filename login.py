import tkinter as tk
import json
from homepage import HomePageUI
from color_palette import *
class Login:
    def __init__(self, root, role_with_id=None, username=None):
        self.role_with_id = role_with_id
        self.username = username
        self.window = root
        self.window.title("Student System Management")
        self.window.geometry("800x500+0+0")
        self.window.config(padx=20, pady=20, bg=ALMOND_FROST)

        self.login_frame = tk.Frame(
            self.window,  
            bg=ALMOND_FROST, 
            relief=tk.GROOVE
        )        
        self.login_frame.place(x=0, width=1540, height=700)

        self.login_text = tk.Label(
            self.login_frame, 
            text="Login", 
            font=FONT_TEXT, 
            background=ALMOND_FROST, 
            foreground="#fff")
        self.login_text.place(x=120, y=100)

        self.login_username_lab = tk.Label(
            self.login_frame, 
            text="Username: ",
            font=FONT_TEXT, 
            background=ALMOND_FROST, 
            foreground="#fff")
        self.login_username_lab.place(x=120, y=135)

        self.login_username_entry = tk.Entry(
            self.login_frame, 
            font=("Times New Roman", 13),
            )
        self.login_username_entry.place(x=300, y=135, width=250, height=30)

        self.login_password_lab = tk.Label(
            self.login_frame,
            text="Password: ",
            font=FONT_TEXT, 
            background=ALMOND_FROST, 
            foreground="#fff")
        self.login_password_lab.place(x=120, y=170)

        self.login_password_entry = tk.Entry(
            self.login_frame,
            font=("Times New Roman", 13),
            show="*", 
            )
        self.login_password_entry.place(x=300, y=170, width=250, height=30)
        
        self.submit_button = tk.Button(
            self.login_frame,
            text="Submit",
            font=FONT_TEXT, 
            background=ALMOND_FROST, 
            foreground="#fff",
            width=20,
            relief=tk.FLAT,
            command=self.login_submit
        )
        self.submit_button.place(x=300, y=300)

    def login_submit(self):
        # read the username and password data from user_data.txt
        with open("user_data.txt", "r") as f:
            user_data = f.read().splitlines()
        # chữ r trước string bởi vì \ thuộc Escape Sequence trong string
        # vì vậy có thể dùng \\ hoặc r tượng trưng cho raw

        # loop through each line in the file and check if login credentials are valid
        valid_credentials = False
        for line in user_data:
            username, password, role_with_id = line.strip().split(":")
            role_parts = role_with_id.split("-")
            role = role_parts[0]
            if len(role_parts) > 1:
        # If there is an ID, extract it
                role_id = role_parts[1]
            """else:
        # If there is no ID, set it to None
                role_id = None"""
            if self.login_username_entry.get() == username and self.login_password_entry.get() == password:
                valid_credentials = True
                self.role = role
                self.role_id = role_id  # set role_id to None if it doesn't exist
                self.username = username
                break


    # show error message if login credentials are invalid
        if not valid_credentials:
            error_label = tk.Label(self.login_frame, text="Invalid username or password", font=("Times New Roman", 13), fg="red")
            error_label.place(x=350, y=240)
        else:
            # create and show the appropriate window based on the user's role
            if self.role == "t":
                self.show_window()
                """elif self.role == "BI":
                self.show_student_window()"""
            else:
                error_role_label = tk.Label(self.login_frame, text="Invalid user role", font=("Times New Roman", 13), fg="red")
                error_role_label.place(x=350, y=240)   
            
    def show_window(self):
        self.window.destroy()  # destroy the login window
        obj = HomePageUI()  # create a new instance of Teacher class to show the teacher window
        
