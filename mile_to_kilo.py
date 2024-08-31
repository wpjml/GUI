import tkinter

def maile_to_kilo():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=str(km))


window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

miles_input = tkinter.Entry(width=7)
miles_input.grid(row=1, column=2)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=1, column=3)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=2, column=1)

kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(row=2, column=2)

kilometer_label = tkinter.Label(text="Km")
kilometer_label.grid(row=2,column=3)

calculate_button = tkinter.Button(text="Calculate", command=maile_to_kilo)
calculate_button.grid(row=3, column=2)

window.mainloop()
