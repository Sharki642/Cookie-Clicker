import tkinter as tk

print("App started!")

x = 0;
factor = 1;

def increment_x():
    global x
    x += 1*factor
    value_label.config(text=f"Cookies: {x}, Factor: {factor}")

def multiplyer():
    global factor
    factor += 1

  
root = tk.Tk()
root.title("Cookie Clicker")
root.geometry("400x300")
tk.Label(root, text="Lets farm cookies!").pack()

value_label = tk.Label(root, text=f"Cookies: {x}")
value_label.pack()

turn_on = tk.Button(root, text="+1", command=increment_x, bg="blue", width=10, height=2)
turn_on.pack()

multiply_button = tk.Button(root, text="Multiplyer", command=multiplyer, bg="green", width=10, height=2)
multiply_button.pack()

root.mainloop()