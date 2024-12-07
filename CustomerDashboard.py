from tkinter import *

class CustomerDashboard:
    def __init__(self, root):
        self.root = root

        title = Label(self.root, text="Welcome to Customer Dashboard", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Buttons for Dashboard Features
        profile_btn = Button(self.root, text="Edit Profile", width=20, command=self.edit_profile)
        profile_btn.pack(pady=10)

        book_taxi_btn = Button(self.root, text="Book Taxi", width=20, command=self.book_taxi)
        book_taxi_btn.pack(pady=10)

        history_btn = Button(self.root, text="View History", width=20, command=self.view_history)
        history_btn.pack(pady=10)

        logout_btn = Button(self.root, text="Logout", width=20, command=self.logout)
        logout_btn.pack(pady=20)

    # Placeholder method for Edit Profile
    def edit_profile(self):
        self.clearWindow()
        from ProfileEdit import Edit
        Edit(self.root)

    # Placeholder method for Book Taxi
    def book_taxi(self):
        self.clearWindow()
        from RequestTaxi import RequestTaxi
        RequestTaxi(self.root)

    # Placeholder method for History
    def view_history(self):
        self.clearWindow()
        from ViewHistory import History
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