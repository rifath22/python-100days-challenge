from tkinter import *
from turtle import bgcolor
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")

# print(word_dict)
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas.itemconfig(lang_name_text, text="French", fill="black")
    canvas.itemconfig(random_lang_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(lang_name_text, text="English", fill="white")
    canvas.itemconfig(random_lang_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)

def known_card():
    global current_card
    word_dict.remove(current_card)
    out_file = pd.DataFrame(word_dict)
    out_file.to_csv("./data/words_to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
lang_name_text = canvas.create_text(400, 150, text="", fill="black", font=('Arial', 40, "italic"))
random_lang_word = canvas.create_text(400, 263, text="", fill="black", font=('Arial', 40, "bold"))
canvas.grid(row=0, column=0,columnspan=2)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0,command=known_card)
right_button.grid(row=1, column=1)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0,command=next_card)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()