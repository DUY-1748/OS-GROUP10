import tkinter as tk
from GUI import VMEApp # Class giao diện từ file gui.py

if __name__ == "__main__":
    root = tk.Tk()
    app = VMEApp(root)
    root.mainloop()