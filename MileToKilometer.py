from tkinter import *


window = Tk()
window.title("Mile to Kilometer ")
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)




def convert_to_kilometer():
    miles = float(input_entry.get())
    km = miles * 1.609
    km_label.config(text=f"{km}")

equal_label = Label(text="is equal to ", font=("New Time Roman", 15, "bold"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

input_entry = Entry(width=14)
input_entry.grid(column=1, row=0)

output_label = Label()
output_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", font=("New Time Roman", 15, "bold"), command=convert_to_kilometer)
calculate_button.grid(column=1, row=2)

mile_label = Label(text="Miles", font=("New Time Roman", 15, "bold"))
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=("New Time Roman", 15, "bold"))
km_label.grid(column=2, row=1)



window.mainloop()