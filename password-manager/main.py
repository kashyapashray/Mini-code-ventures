from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password-Man")
window.config(padx=20, pady=20)
canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website_label = Label()

window.mainloop()