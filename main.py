import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
my_label["text"] = "New Text"


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = tkinter.Button(text="click me", command=button_clicked)
button.grid(row=2, column=2)

input = tkinter.Entry(width=10)
input.grid(row=3, column=4)

new_button = tkinter.Button()
new_button.grid(row=0, column=3)


window.mainloop()
