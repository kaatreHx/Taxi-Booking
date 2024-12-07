from tkinter import *

class AdminDashboard:
    def __init__(self, root):
        self.root = root

        title = Label(self.root, text="Welcome to Admin Dashboard", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Buttons for Dashboard Features
        regDriver_btn = Button(self.root, text="Register Driver", width=20, command=self.reqDriver)
        regDriver_btn.pack(pady=10)

        assignDriver_btn = Button(self.root, text="Assign Driver", width=20, command=self.assignDriver)
        assignDriver_btn.pack(pady=10)

        history_btn = Button(self.root, text="History", width=20, command=self.view_history)
        history_btn.pack(pady=10)

        logout_btn = Button(self.root, text="Logout", width=20, command=self.logout)
        logout_btn.pack(pady=20)

    # Placeholder method for Edit Profile
    def reqDriver(self):
        self.clearWindow()
        from RegDriver import Register
        Register(self.root)

    # Placeholder method for Book Taxi
    def assignDriver(self):
        self.clearWindow()
        from AssignDriver import AssignDriver
        AssignDriver(self.root)

    # Placeholder method for History
    def view_history(self):
        self.clearWindow()
        from AdminHistory import History
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