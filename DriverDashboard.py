from tkinter import *

class DriverDashboard:
    def __init__(self, root):
        self.root = root

        title = Label(self.root, text="Welcome to Customer Dashboard", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Buttons for Dashboard Features
        assign_btn = Button(self.root, text="AssignTrip", width=20, command=self.assignTrip)
        assign_btn.pack(pady=10)

        history_btn = Button(self.root, text="History", width=20, command=self.history)
        history_btn.pack(pady=10)

        logout_btn = Button(self.root, text="Logout", width=20, command=self.logout)
        logout_btn.pack(pady=20)

    # Placeholder method for Edit Profile
    def assignTrip(self):
        self.clearWindow()
        from AssignTrip import AssignTrip
        AssignTrip(self.root)

    # Placeholder method for Book Taxi
    def history(self):
        self.clearWindow()
        from DriverHistory import History
        History(self.root)

    # Placeholder method for Logout
    def logout(self):
        self.clearWindow()
        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        from LoginPage import LoginPage
        LoginPage(self.root)
    
    def clearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()