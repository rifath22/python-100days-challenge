from tkinter import *

from matplotlib.pyplot import text
from quiz_brain import QuizBrain
from pyparsing import col
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, width=280, font=('Arial', 20, "italic"))
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0,column=1)

        right_button_img = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_button_img, highlightthickness=0, command=self.green_button_press)
        self.right_button.grid(row=2, column=0)

        wrong_button_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=self.red_button_press)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
        # self.green_button_press()
        # self.red_button_press()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def green_button_press(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def red_button_press(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)