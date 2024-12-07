from tkinter import *
from tkinter import ttk
from DB import Connection
from DriverDashboard import DriverDashboard
import Global

class History(DriverDashboard):
    def __init__(self, root):
        self.root = root

        self.tree = ttk.Treeview(self.root, columns=("bid", "from", "to", "requestDate", "requestTime", "status"), show="headings")
        self.tree.heading("bid", text="Booking ID")
        self.tree.heading("from", text="From")
        self.tree.heading("to", text="To")
        self.tree.heading("requestDate", text="Request Date")
        self.tree.heading("requestTime", text="Request Time")
        self.tree.heading("status", text="Status")

        self.tree.column("bid", width=80, anchor=CENTER)
        self.tree.column("from", width=120, anchor=CENTER)
        self.tree.column("to", width=120, anchor=CENTER)
        self.tree.column("requestDate", width=100, anchor=CENTER)
        self.tree.column("requestTime", width=100, anchor=CENTER)
        self.tree.column("status", width=100, anchor=CENTER)

        self.tree.pack(fill=BOTH, expand=1)

        back = Button(self.root, text="Back", command=self.back)
        back.pack(pady=10)

        # Load data into the table
        self.fetch_data()

    def fetch_data(self):
        try:
            # Connect to the database
            db = Connection()
            connection = db.connection()
            cursor = connection.cursor()

            # Query to fetch booking history
            query = f"SELECT bid, fromlocation, tolocation, dateofbooking, booktime, status FROM bookings where did={Global.id} and status='Complete'"
            cursor.execute(query)
            rows = cursor.fetchall()

            # Clear existing data in the table
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insert fetched rows into the Treeview
            for row in rows:
                self.tree.insert("", END, values=row)

            cursor.close()
            connection.close()

        except Exception as e:
            print("Error fetching data:", e)

    def back(self):
        self.clearWindow()
        DriverDashboard(self.root)