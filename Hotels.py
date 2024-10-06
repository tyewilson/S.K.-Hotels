import tkinter as tk
from tkinter import *
import bcrypt
import time
import csv

# DO NOT move OR delete this class!!!!
class Navigating(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)  # This line of code is extremely important.
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Welcome, Location, Login, peopleamount, finalbill, staff, Register, Welcome1):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Welcome)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Main Class
class Welcome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Welcome to The S.K. Hotels App!", font=("Comic Sans", 20)).place(x=20, y=10)

        Booking = tk.Button(self, text="Book a Room", command=lambda: controller.show_frame(Location), height=2, width=10, fg="black")
        Booking.place(x=20, y=50)

        usrlogin = tk.Button(self, text="Login/signup", command=lambda: controller.show_frame(Login), height=1, width=10, fg="black")
        usrlogin.place(x=1835, y=5)

# Second Class
class Location(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Which location would you like to stay at?", font=("Comic Sans", 20)).pack(padx=10, pady=5)

# Third Class
class roomtype(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

# Fourth Class
class peopleamount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

# Fifth Class
class Welcome1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

# Sixth Class
class finalbill(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

# Seventh Class
class staff(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Title
        St = tk.Label(self, text="Welcome to The S.K. Hotels App!", font=("Comic Sans", 20))
        St.place(x=950, y=10)

# Eighth Class
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Title
        Li = tk.Label(self, text="Register", font=("Comic Sans", 20))
        Li.place(x=950, y=10)

        # Button to take user back to login screen
        login = tk.Button(self, text="Login", command=lambda: controller.show_frame(Login), height=1, width=10, fg="black")
        login.place(x=1835, y=5)

        # Username entry box
        self.Username = tk.Entry(self, font=("Comic Sans", 20), width=40)
        self.Username.place(x=170, y=100)

        # Displays "Username:" next to entry box
        UsrTxt = tk.Label(self, text="Username:", font=("Comic Sans", 20))
        UsrTxt.place(x=10, y=100)

        # Password entry box
        self.PlainPwd = tk.Entry(self, font=("Comic Sans", 20), width=40, show="*")  # Mask the password input
        self.PlainPwd.place(x=170, y=150)

        # Displays "Password:" next to password box
        PwdTxt = tk.Label(self, text="Password:", font=("Comic Sans", 20))
        PwdTxt.place(x=10, y=150)

        # Register Button
        RegBtn = tk.Button(self, text="Register", command=self.save_user_data, height=2, width=10)
        RegBtn.place(x=170, y=200)

    # Save user data (Registration)
    def save_user_data(self):
        username = self.Username.get()
        PlainPwd = self.PlainPwd.get()

        if not username or not PlainPwd:
            print("Username or password cannot be empty.")
            return

        # Hash the password
        HashPwd = bcrypt.hashpw(PlainPwd.encode('utf-8'), bcrypt.gensalt())

        try:
            # Open the file and append user data
            with open("Data.txt", "a") as file:
                file.write(f'{username}:{HashPwd.decode("utf-8")}\n')
            usrreg=tk.Label(self,text="User registered successfully!")
            usrreg.place(x=500,y=200)
        except Exception as e:
            print(f"Error writing to file: {e}")



#Ninth Class
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Title
        Li = tk.Label(self, text="Login", font=("Comic Sans", 20))
        Li.place(x=950, y=10)

        # Register Button (go to Register)
        Reg = tk.Button(self, text="Register", command=lambda: controller.show_frame(Register), height=1, width=10, fg="black")
        Reg.place(x=1835, y=5)

        # Username entry box
        self.Usr = tk.Entry(self, text="", font=("Comic Sans", 20), width=40)
        self.Usr.place(x=170, y=100)

        # Displays "Username:" next to entry box
        UsrTxt = tk.Label(self, text="Username:", font=("Comic Sans", 20))
        UsrTxt.place(x=10, y=100)

        # Password entry box
        self.PlainPwd = tk.Entry(self, text="", font=("Comic Sans", 20), width=40, show="*")
        self.PlainPwd.place(x=170, y=150)

        # Displays "Password:" next to password box
        PwdTxt = tk.Label(self, text="Password:", font=("Comic Sans", 20))
        PwdTxt.place(x=10, y=150)

        # Login button
        LoginBtn = tk.Button(self, text="Login", command=lambda: self.check_password(controller), height=2, width=10)
        LoginBtn.place(x=170, y=200)

        # Label to display messages
        self.message_label = tk.Label(self, text="", font=("Comic Sans", 20))
        self.message_label.place(x=10, y=270)
    # Check password function 
    def check_password(self, controller):

        # Gets the input from the user
        entered_username = self.Usr.get()
        PlainPwd = self.PlainPwd.get()

        # Opens user data text file
        try:
            with open("Data.txt", "r") as file:
                users = file.readlines()
        except FileNotFoundError:
            self.message_label.config(text="User data file not found.")
            return

        # Checks for Username
        for user in users:
            username, HashPwd = user.strip().split(":")
            # If username matches it hashes the inputted password and checks if it matches the password in the file
            if username == entered_username:
                if bcrypt.checkpw(PlainPwd.encode('utf-8'), HashPwd.encode('utf-8')):
                    # Prints message password accepted
                    self.message_label.config(text="Password accepted")

                    # Redirects to the welcome screen 
                    self.after(100, lambda: controller.show_frame(Welcome1))
                    return
                else:
                    # Error message
                    self.message_label.config(text="Password/Username does not match")
                    return
        # Error message if username not in file
        self.message_label.config(text="Username not found.")

        # Staff data verification
        try:
            with open("StaffData.txt", "r") as file:
                Roles = file.readlines()
        except FileNotFoundError:
            self.message_label.config(text="Role data file not found.")
            return

        # Checks if user is staff
        for role in Roles:

            # Looks for staff username and password 
            staff_username, staff_password = role.strip().split(":")

            #Checks if username matches username inputted
            if entered_username == staff_username:

                # Hashes inputted password and checks if it matches with the password in the staff data file
                if bcrypt.checkpw(PlainPwd.encode('utf-8'), staff_password.encode('utf-8')):

                    # Successful login message
                    self.message_label.config(text="Staff login successful")

                    # Redirect to the staff page
                    self.after(100, lambda: controller.show_frame(staff))  
                   

# DO NOT CHANGE OR REMOVE!!!!!!!!
root = Navigating()
root.geometry("1920x1080") 
root.mainloop()  