import tkinter as tk

print("App started!")

x = 0;

def increment_x():
    global x
    x += 1
    value_label.config(text=f"Cookies: {x}")
root = tk.Tk()
root.title("Cookie Clicker")
root.geometry("400x300")
tk.Label(root, text="Lets farm cookies!").pack()

value_label = tk.Label(root, text=f"Cookies: {x}")
value_label.pack()

turn_on = tk.Button(root, text="+1", command=increment_x, bg="blue", width=10, height=2)
turn_on.pack()

root.mainloop()