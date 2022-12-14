from tkinter import Tk, Label, Button, Canvas, PhotoImage
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 25
# Uncomment the next line while testing with
# the test version of start_timer so you don't have to wait 25 seconds
# WORK_MIN = 7
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECKMARK = "✓"

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global CHECKMARK, REPS
    CHECKMARK = "✓"
    checkmark_label.config(text=CHECKMARK)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0

# --------------------------- TIMER MECHANISM ------------------------------ #

def countdown(count):
    if REPS != 0:
        count_min = floor(count / 60)
        count_sec = count % 60
        timer_label_func(REPS)
        if count_sec >= 10:
            count_sec_final = count_sec
        elif count_sec < 10:
            count_sec_final = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec_final}")
        if count > 0:
            window.after(1000, countdown, count - 1)
        elif count == 0:
            start_timer()

# def start_timer():
#     # Test version that counts in seconds instead of minutes.
#     global REPS
#     REPS += 1
#     if REPS % 8 == 0:
#         countdown(LONG_BREAK_MIN)
#     elif REPS % 2 == 0:
#         countdown(SHORT_BREAK_MIN)
#     elif REPS % 2 != 0:
#         countdown(WORK_MIN)
#         if REPS != 1:
#             add_checkmark()

def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        countdown(60 * LONG_BREAK_MIN)
    elif REPS % 2 == 0:
        countdown(60 * SHORT_BREAK_MIN)
    elif REPS % 2 != 0:
        countdown(60 * WORK_MIN)
        if REPS != 1:
            add_checkmark()

def timer_label_func(reps_count):
    if reps_count % 8 == 0:
        timer_label.config(text="Long break. Have some fun!", fg=RED)
    elif reps_count % 2 == 0:
        timer_label.config(text="Short break.", fg=PINK)
    elif reps_count % 2 != 0:
        timer_label.config(text="Work.", fg=GREEN)

def add_checkmark():
    global CHECKMARK
    CHECKMARK += "✓"
    checkmark_label.config(text=CHECKMARK)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=("Arial", 35), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

checkmark_label = Label(text=CHECKMARK, font=("Arial", 15, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

image = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

window.mainloop()
