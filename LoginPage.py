from tkinter import *
from tkinter import messagebox
from DB import Connection
import Global

class LoginPage:
    def __init__(self, root):
        self.root = root

        username = Label(self.root, text="Username:")
        username.place(x=50, y=20)
        self.username_entry = Entry(self.root, width=25)
        self.username_entry.place(x=120, y=20)

        pwd = Label(self.root, text="Password:")
        pwd.place(x=50, y=50)
        self.pwd_entry = Entry(self.root, width=25, show="*")
        self.pwd_entry.place(x=120, y=50)


        login = Button(self.root, text="Login", command=self.login, width=10)
        login.place(x=80, y=100)

        register = Button(self.root, text="Register", command=self.register, width=10)
        register.place(x=160, y=100)
    
    def login(self):
        username = self.username_entry.get()
        password = self.pwd_entry.get()
        try:
            db = Connection()
            self.connection = db.connection()
            cursor = self.connection.cursor()

            # Check for customer login
            query = "SELECT * FROM customer WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            data = cursor.fetchone()  # Use fetchone for efficiency
            if data:
                Global.id = data[0]
                self.clearWindow()
                messagebox.showinfo("Login", "Login Success")
                from CustomerDashboard import CustomerDashboard
                CustomerDashboard(self.root)
                return  # Exit after successful login

            # Check for driver login
            query = "SELECT * FROM driver WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            data = cursor.fetchone()  # Use fetchone for efficiency
            if data:
                Global.id = data[0]
                self.clearWindow()
                messagebox.showinfo("Login", "Login Success")
                from DriverDashboard import DriverDashboard
                DriverDashboard(self.root)
                return  # Exit after successful login

            if username == "admin" and password == "admin":
                self.clearWindow()
                messagebox.showinfo("Login", "Login Success")
                from AdminDashboard import AdminDashboard
                AdminDashboard(self.root)
                return

            # If no match found in either table
            messagebox.showerror("Login Failed", "Invalid username or password")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def register(self):
        self.clearWindow()
        from RegisterCustomer import Register
        Register(self.root)

    def clearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()