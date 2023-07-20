import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    timeLabel.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work = WORK_MIN * 60
    s_brk = SHORT_BREAK_MIN * 60
    l_brk = LONG_BREAK_MIN * 60
    reps += 1
    print(reps)
    if reps % 8 == 0:
        timeLabel.config(text="Break", fg=RED)
        count_down(l_brk)
    elif reps % 2 == 0:
        timeLabel.config(text="Break", fg=PINK)
        count_down(s_brk)
    else:
        timeLabel.config(text="Work", fg=GREEN)
        count_down(work)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(cnt):
    c_min = math.floor(cnt / 60)
    if c_min < 10:
        c_min = f"0{c_min}"
    c_sec = cnt % 60
    if c_sec < 10:
        c_sec = f"0{c_sec}"

    canvas.itemconfig(timer_txt, text=f"{c_min}:{c_sec}")
    if cnt > 0:
        global timer
        timer = window.after(1000, count_down, cnt - 1)
    else:
        if reps % 2 != 0:
            tick.config(text="✔" * int((reps - 1) / 2 + 1))
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timeLabel = Label(text="TIMER", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
timeLabel.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 9), command=start_timer)
start_button.grid(row=2, column=0)
stop_button = Button(text="Reset", font=(FONT_NAME, 9), command= reset_timer)
stop_button.grid(row=2, column=2)

tick = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
tick.grid(row=3, column=1)
window.mainloop()
