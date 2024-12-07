from tkinter import *
from DB import Connection
from tkinter import messagebox
from CustomerDashboard import CustomerDashboard
import Global

class Edit(CustomerDashboard):
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

        update = Button(self.root, text="Keep Changes", command=self.update)
        update.place(x=50, y=260)

        self.fetchData()
    
    def update(self):
        try:
            # Retrieve data from entry fields
            name = self.name_entry.get()
            email = self.email_entry.get()
            contact = self.contact_entry.get()
            address = self.address_entry.get()
            username = self.username_entry.get()
            password = self.password_entry.get()

            # Database connection
            db = Connection()
            self.connection = db.connection()
            cursor = self.connection.cursor()

            # Update query
            query = """
                UPDATE customer 
                SET name=%s, email=%s, contact=%s, address=%s, username=%s, password=%s 
                WHERE id=%s
            """
            cursor.execute(query, (name, email, contact, address, username, password, Global.id))
            self.connection.commit()

            # Success message
            messagebox.showinfo("Success", "Profile updated successfully!")
            self.clearWindow()
            CustomerDashboard(self.root)


        except Exception as e:
            messagebox.showerror("Error", f"Error updating data: {e}")

    def fetchData(self):
        try:
            db = Connection()
            self.connection = db.connection()
            cursor = self.connection.cursor()

            # Check for customer login
            query = f"SELECT * FROM customer WHERE id={Global.id}"
            cursor.execute(query)
            data = cursor.fetchone()
            if data:
                self.name_entry.insert(0, data[1])  
                self.email_entry.insert(0, data[2])
                self.contact_entry.insert(0, data[3])
                self.address_entry.insert(0, data[4])
                self.username_entry.insert(0, data[5]) 
                self.password_entry.insert(0, data[6])
        
        except Exception as e:
            print("Error:", e)