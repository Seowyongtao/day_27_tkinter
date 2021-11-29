from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)


def button_clicked():
    user_input = my_entry.get()
    my_label.config(text=user_input)


# label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

# entry

my_entry = Entry(width=10)
my_entry.grid(row=2, column=4)

# button

my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(row=1, column=1)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(row=0, column=2)


window.mainloop()
