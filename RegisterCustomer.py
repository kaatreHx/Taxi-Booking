from tkinter import *
from tkinter import messagebox
from DB import Connection
from LoginPage import LoginPage

class Register(LoginPage):
    def __init__(self, root):
        self.root = root

        name = Label(self.root, text="Name:")
        name.place(x=50, y=20)
        self.name_entry = Entry(self.root, width=25)
        self.name_entry.place(x=150, y=20)

        email = Label(self.root, text="Email:")
        email.place(x=50, y=60)
        self.email_entry = Entry(self.root, width=25)
        self.email_entry.place(x=150, y=60)

        contact = Label(self.root, text="Contact:")
        contact.place(x=50, y=100)
        self.contact_entry = Entry(self.root, width=25)
        self.contact_entry.place(x=150, y=100)

        address = Label(self.root, text="Address:")
        address.place(x=50, y=140)
        self.address_entry = Entry(self.root, width=25)
        self.address_entry.place(x=150, y=140)

        username = Label(self.root, text="Username:")
        username.place(x=50, y=180)
        self.username_entry = Entry(self.root, width=25)
        self.username_entry.place(x=150, y=180)

        password = Label(self.root, text="Password:")
        password.place(x=50, y=220)
        self.password_entry = Entry(self.root, width=25, show="*")
        self.password_entry.place(x=150, y=220)

        register = Button(self.root, text="Register", command=self.register)
        register.place(x=50, y=260)
    
    def register(self):
        try:
            db = Connection()
            connection = db.connection()
            cursor = connection.cursor()
            query = """
                    INSERT INTO customer (name, email, contact, address, username, password)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
            values = (self.name_entry.get(), self.email_entry.get(), self.contact_entry.get(), self.address_entry.get(), self.username_entry.get(), self.password_entry.get())
            cursor.execute(query, values)
            self.clearWindow()
            messagebox.showinfo("Registration","Registration Success")
            from LoginPage import LoginPage
            LoginPage(self.root)
            connection.commit()
            cursor.close()
        
        except Exception as e:
            print("Error:",e)


        
        
        
        
        
        
        