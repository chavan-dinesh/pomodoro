from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 6
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0 and reps < 8:
        timer_label.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
        count_down(work_sec)
    elif reps == 8:
        timer_label.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 30))
        count_down(long_break_sec)
    elif reps % 2 == 0 and reps < 7:
        timer_label.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 30))
        count_down(short_break_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
    mark = ""
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
        mark += "✔"
    check_marks.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro - Built by Reyaansh!")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=320, height=324, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(160, 150, image=tomato_image)
timer_text = canvas.create_text(170, 170, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)



timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()