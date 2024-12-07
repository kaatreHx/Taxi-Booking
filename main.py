import tkinter as tk

class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x800")
        self.root.title("Assignment Taxi")
        self.login()
    
    def login(self):
        from LoginPage import LoginPage
        LoginPage(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    Main(root)
    root.mainloop()