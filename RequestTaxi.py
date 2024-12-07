from tkinter import *
from DB import Connection
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox
import Global
from CustomerDashboard import CustomerDashboard

class RequestTaxi(CustomerDashboard):
    def __init__(self, root):
        self.root =root

        fromLoc = Label(self.root, text="From:")
        fromLoc.place(x=50, y=20)
        self.from_entry = Entry(self.root, width=25)
        self.from_entry.place(x=150, y=20)

        toLoc = Label(self.root, text="To:")
        toLoc.place(x=50, y=60)
        self.to_entry = Entry(self.root, width=25)
        self.to_entry.place(x=150, y=60)

        date = Label(self.root, text="Date:")
        date.place(x=50, y=100)
        self.date_entry = DateEntry(self.root, width=22, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
        self.date_entry.place(x=150, y=100)

        time = Label(self.root, text="Time:")
        time.place(x=50, y=140)
        self.time_entry = Entry(self.root, width=25)
        self.time_entry.place(x=150, y=140)

        # Submit Button
        submit_btn = Button(self.root, text="Request Taxi", command=self.request_taxi)
        submit_btn.place(x=150, y=180)

    def request_taxi(self):
        from_location = self.from_entry.get()
        to_location = self.to_entry.get()
        request_date = self.date_entry.get()
        request_time = self.time_entry.get()
        current_date_str = datetime.now().strftime("%Y-%m-%d")

        if request_date < current_date_str:
            messagebox.showwarning("Date Error","Invalid Date Choice!")
            return
        
        try:
            db = Connection()
            connection = db.connection()
            cursor = connection.cursor()
            query = """
                    INSERT INTO bookings (fromlocation, tolocation, dateofbooking, booktime, currentdate, cid, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
            values = (from_location, to_location, request_date, request_time, current_date_str, Global.id, "Pending")
            cursor.execute(query, values)
            self.clearWindow()
            messagebox.showinfo("Book","Book Sent!")
            CustomerDashboard(self.root)
            connection.commit()
            cursor.close()
        
        except Exception as e:
            print("Error:",e)