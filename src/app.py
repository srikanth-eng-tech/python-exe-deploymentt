import tkinter as tk
from tkinter import messagebox

def on_click():
    messagebox.showinfo("Message", "Hello! This GUI EXE was built automatically.")

root = tk.Tk()
root.title("My GUI App")
root.geometry("400x200")

label = tk.Label(root, text="Welcome to My GUI App", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

root.mainloop()

