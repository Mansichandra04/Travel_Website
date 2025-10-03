import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")
label = tk.Label(root, font=("Arial", 40), bg="black", fg="cyan")
label.pack()

def update():
    label.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, update)

update()
root.mainloop()
