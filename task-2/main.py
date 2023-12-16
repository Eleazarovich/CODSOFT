import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
# root.geometry("300x350")

screen = tk.Entry(font=("Arial", 16), width=22, border=10)

# buttons to visualize 0 to 9

zero = tk.Button(root, text="0", height=2, width=3)
one = tk.Button(root, text="1", height=2, width=3)
two = tk.Button(root, text="2", height=2, width=3)
three = tk.Button(root, text="3",height=2, width=3)
four = tk.Button(root, text="4", height=2, width=3)
five = tk.Button(root, text="5", height=2, width=3)
six = tk.Button(root, text="6", height=2, width=3)
seven = tk.Button(root, text="7", height=2, width=3)
eight = tk.Button(root, text="8", height=2, width=3)
nine = tk.Button(root, text="9", height=2, width=3)

# buttons to visualize arithmetic operations

addition = tk.Button(root, text="+", fg="white", bg="black", height=2, width=3)
subtraction = tk.Button(root, text="-", fg="white", bg="black", height=2, width=3)
multiplication = tk.Button(root, text="X", fg="white", bg="black", height=2, width=3)
division = tk.Button(root, text="/", fg="white", bg="black", height=2, width=3)

# button to visualize equal sign

equal = tk.Button(root, text="=", fg="white", bg="black", height=2, width=3)

# button to visualize clear sign

clear = tk.Button(root, text="C", fg="white", bg="red", height=2, width=3)

# visualize buttons on the GUI
# first row
screen.grid(row=0, columnspan=4, padx=10, pady=10)

# second row
seven.grid(row=1, column=0, padx=5, pady=7)
eight.grid(row=1, column=1, padx=5)
nine.grid(row=1, column=2, padx=5)
addition.grid(row=1, column=3, padx=5)

# third row
four.grid(row=2, column=0, padx=5, pady=7)
five.grid(row=2, column=1, padx=5)
six.grid(row=2, column=2, padx=5)
subtraction.grid(row=2, column=3, padx=5)

# fourth row
one.grid(row=3, column=0, padx=5, pady=7)
two.grid(row=3, column=1, padx=5)
three.grid(row=3, column=2, padx=5)
multiplication.grid(row=3, column=3, padx=5)

# firth row
clear.grid(row=4, column=0, padx=5, pady=7)
zero.grid(row=4, column=1, padx=5)
equal.grid(row=4, column=2, padx=5)
division.grid(row=4, column=3, padx=5)










root.mainloop()