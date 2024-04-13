import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =  1 #25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    heading_label.config(text="Timer",bg=YELLOW, fg=GREEN)
    tick_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count = LONG_BREAK_MIN * 60
        heading_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN * 60
        heading_label.config(text="Break", fg=PINK)
    else:
        count = WORK_MIN * 60
        heading_label.config(text="Work", fg=GREEN)
    count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    formatted_time = f"{count_min}:{count_sec}"

    canvas.itemconfig(timer_text, text=formatted_time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        tick_count = math.floor(reps / 2)
        tick_out = ""
        # tick_list = ["✓", "✓✓", "✓✓✓", "✓✓✓✓"]
        for _ in range(tick_count):
            tick_out += "✓"

        tick_label.config(text=tick_out, fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='./tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)


#Buttons
def action():
    print("Do something")
start_button = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2,column=0)

reset_button = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2,column=2)

#Labels
heading_label = tkinter.Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
heading_label.grid(row=0,column=1)

tick_label = tkinter.Label()
tick_label.grid(row=3,column=1)

window.mainloop()