import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

basic_arithmetic_sign = None

screen = tk.Entry(font=("Arial", 16), width=22, border=10, justify="right")

def show_number_on_screen(number):
    # if screen.get():
    #     screen.delete(0, tk.END)

    current_number = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, str(current_number) + str(number))
    return current_number, number


def clear_screen():
    # clear.bind("<Enter>", clear.config(bg="red"))
    global basic_arithmetic_sign
    basic_arithmetic_sign = None
    screen.delete(0, tk.END)

def add():
    global basic_arithmetic_sign
    basic_arithmetic_sign = "+"
    first_number = int(screen.get())
    screen.delete(0, tk.END)
    return first_number

def sub():
    global basic_arithmetic_sign
    basic_arithmetic_sign = "-"
    first_number = int(screen.get())
    screen.delete(0, tk.END)
    return first_number

def mul():
    global basic_arithmetic_sign
    basic_arithmetic_sign = "x"
    first_number = int(screen.get())
    screen.delete(0, tk.END)
    return first_number

def div():
    global basic_arithmetic_sign
    basic_arithmetic_sign = "/"
    first_number = int(screen.get())
    screen.delete(0, tk.END)
    return first_number

def show_answer():
    global basic_arithmetic_sign
    # if basic_arithmetic_sign == None:
    #     pass

    second_number = screen.get()

    if basic_arithmetic_sign == "+":
        screen.insert(0, add() + int(second_number))
        # basic_arithmetic_sign = None
    elif basic_arithmetic_sign == "-":
        screen.insert(0, sub() - int(second_number))
        # basic_arithmetic_sign = None
    elif basic_arithmetic_sign == "x":
        screen.insert(0, mul() * int(second_number))
        # basic_arithmetic_sign = None
    elif basic_arithmetic_sign == "/":
        screen.insert(0, div() / int(second_number))
        # basic_arithmetic_sign = None



# buttons to visualize 0 to 9

zero = tk.Button(root, text="0", height=2, width=3, command=lambda: show_number_on_screen(0))
one = tk.Button(root, text="1", height=2, width=3, command=lambda: show_number_on_screen(1))
two = tk.Button(root, text="2", height=2, width=3, command=lambda: show_number_on_screen(2))
three = tk.Button(root, text="3",height=2, width=3, command=lambda: show_number_on_screen(3))
four = tk.Button(root, text="4", height=2, width=3, command=lambda: show_number_on_screen(4))
five = tk.Button(root, text="5", height=2, width=3, command=lambda: show_number_on_screen(5))
six = tk.Button(root, text="6", height=2, width=3, command=lambda: show_number_on_screen(6))
seven = tk.Button(root, text="7", height=2, width=3, command=lambda: show_number_on_screen(7))
eight = tk.Button(root, text="8", height=2, width=3, command=lambda: show_number_on_screen(8))
nine = tk.Button(root, text="9", height=2, width=3, command=lambda: show_number_on_screen(9))

# buttons to visualize arithmetic operations

addition = tk.Button(root, text="+", fg="white", bg="black", height=2, width=3, command=add)
subtraction = tk.Button(root, text="-", fg="white", bg="black", height=2, width=3, command=sub)
multiplication = tk.Button(root, text="X", fg="white", bg="black", height=2, width=3, command=mul)
division = tk.Button(root, text="/", fg="white", bg="black", height=2, width=3, command=div)

# button to visualize equal sign

equal = tk.Button(root, text="=", fg="white", bg="black", height=2, width=3, command=show_answer)

# button to visualize clear sign

clear = tk.Button(root, text="C", fg="white", bg="red", height=2, width=3, command=clear_screen)

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