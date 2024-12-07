from tkinter import *
from tkinter import ttk
from DB import Connection
from tkinter import messagebox
from AdminDashboard import AdminDashboard

class AssignDriver(AdminDashboard):
    def __init__(self, root):
        self.root = root
        self.driver_id = None

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

        # Driver selection for assigning
        self.driver_label = Label(self.root, text="Select Driver:")
        self.driver_label.place(x=50, y=300)
        
        self.driver_combo = ttk.Combobox(self.root, width=25)
        self.driver_combo.place(x=150, y=300)
        
        self.assign_button = Button(self.root, text="Assign Driver", command=self.assign_driver)
        self.assign_button.place(x=50, y=340)

        back = Button(self.root, text="Back", command=self.back)
        back.place(x=100, y=340)

        self.fetch_bookings()  # Load bookings into the table
        self.fetch_drivers()   # Load drivers into the combo box

    def back(self):
        self.clearWindow()
        from AdminDashboard import AdminDashboard
        AdminDashboard(self.root)

    def fetch_bookings(self):
        try:
            db = Connection()
            connection = db.connection()
            cursor = connection.cursor()

            # Query to fetch booking details
            query = "SELECT bid, fromlocation, tolocation, dateofbooking, booktime, status FROM bookings WHERE status='Pending'"
            cursor.execute(query)
            rows = cursor.fetchall()

            # Clear existing data in the treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insert fetched rows into the treeview
            for row in rows:
                self.tree.insert("", END, values=row)

            cursor.close()
            connection.close()

        except Exception as e:
            print("Error fetching bookings:", e)

    def fetch_drivers(self):
       
        try:
            db = Connection()
            connection = db.connection()
            cursor = connection.cursor()

            # Query to fetch driver names and IDs
            query = "SELECT id, name FROM driver where status='Free'"
            cursor.execute(query)
            drivers = cursor.fetchall()

            driver_names = [driver[1] for driver in drivers]
            self.driver_combo['values'] = driver_names

            cursor.close()
            connection.close()

        except Exception as e:
            print("Error fetching drivers:", e)

    def assign_driver(self):
 
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a booking to assign.")
            return

        booking_id = self.tree.item(selected_item[0], "values")[0]
        selected_driver_name = self.driver_combo.get()

        if not selected_driver_name:
            messagebox.showwarning("Selection Error", "Please select a driver.")
            return

        try:
            db = Connection()
            connection = db.connection()
            cursor = connection.cursor()

            # Get the driver ID based on the selected driver name
            query = "SELECT id FROM driver WHERE name = %s"
            cursor.execute(query, (selected_driver_name,))
            driver_data = cursor.fetchone()
            if driver_data:
                self.driver_id = driver_data[0]
            
            # Update the booking with the selected driver
            update_query = "UPDATE bookings SET did = %s, status = 'Assigned' WHERE bid = %s"
            cursor.execute(update_query, (self.driver_id, booking_id))

            update_query = "UPDATE driver SET status='Busy' WHERE id = %s"
            cursor.execute(update_query, (self.driver_id))
            
            connection.commit()
            cursor.close()

            # Update the Treeview to reflect the change
            self.fetch_bookings()

            messagebox.showinfo("Success", f"Driver {selected_driver_name} assigned to booking ID {booking_id}.")
            self.clearWindow()
            AdminDashboard(self.root)


        except Exception as e:
            print("Error assigning driver:", e)

