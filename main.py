import tkinter as tk

print("hello")
x = 0;
def increment_x():
    global x
    x += 1
    c
    value_label.config(text=f"Value of x: {x}")
root = tk.Tk()
root.title("Cookie Clicker")
root.geometry("400x300")
tk.Label(root, text="Nothing will work unless you do.").pack()

value_label = tk.Label(root, text=f"Value of x: {x}")
value_label.pack()

turn_on = tk.Button(root, text="ON", command=increment_x)
turn_on.pack()

root.mainloop()
