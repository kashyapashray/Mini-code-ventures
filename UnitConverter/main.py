from tkinter import *

window = Tk()
window.title("KM to Miles Converter")
window.minsize(width=400, height=150)
window.config(padx=100, pady=20)

# label

kmLabel = Label(text="km", font=("Arial",12))
kmLabel.grid(row=0, column=2, padx=10,pady=10)

milesLabel = Label(text="miles", font=("Arial",12))
milesLabel.grid(row=1, column=2, padx=10,pady=10)

equLabel = Label(text="is equal to", font=("Arial",12))
equLabel.grid(row=1, column=0, padx=10,pady=10)


def butt_clicked():
    km = inpKm.get()
    miles = round(int(km) * .62, 2)
    inpM.config(text=miles)


# button

button = Button(text="CONVERT", command=butt_clicked)
button.grid(row=2, column=1)

# entry

inpKm = Entry(width=10)
inpKm.grid(row=0, column=1)

inpM = Label(text="0")
inpM.grid(row=1, column=1)

window.mainloop()
