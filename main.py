from tkinter import *
def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    my_label_3.config(text = f"{km}" )

window =Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady= 20)

# Label
my_label_1 = Label(text="Miles")
my_label_1.grid(column = 2, row = 0)


my_label_2 = Label(text="Km")
my_label_2.grid(column = 2, row = 1)

my_label_3 = Label(text="0")
my_label_3.grid(column = 1, row = 1)


my_label_4 = Label(text="is equal to")
my_label_4.grid(column = 0, row = 1)


# Button
button = Button(text= "Calculate", command = miles_to_km)
button.grid(column= 1, row = 2)


# Entry
input = Entry(width = 7)
input.grid(column =1, row =0 )

window.mainloop()