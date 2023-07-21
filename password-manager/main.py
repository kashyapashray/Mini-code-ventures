from tkinter import *
FONT = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password-Man")
window.config(padx=50, pady=50)
canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website/URL", font=FONT)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/username", font=FONT)
email_label.grid(row=2, column=0)
pass_label = Label(text="Password", font=FONT)
pass_label.grid(row=3, column=0)

url_space = Entry(width=35)
url_space.grid(row=1, column=1, columnspan=2)
email_space = Entry(width=35)
email_space.grid(row=2, column=1, columnspan=2)
pass_space = Entry(width=21)
pass_space.grid(row=3, column=1, columnspan=1)
generate_butt = Button(text="Generate Pass")
generate_butt.grid(row=3, column=2, columnspan=1)
add_butt = Button(text="ADD", width=36)
add_butt.grid(row=4, column=1, columnspan=2)
window.mainloop()
