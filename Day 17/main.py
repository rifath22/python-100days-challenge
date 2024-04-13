from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from open_trivia_data import ot_question_data
question_bank       = []
ot_question_bank    = []

for q in question_data:
    question_text   = q['text']
    question_answer = q['answer']
    new_question    = Question(question_text, question_answer)     
    question_bank.append(new_question)

# for question in ot_question_data:
#     question_text   = question['question']
#     question_answer = question['correct_answer']
#     new_question    = Question(question_text, question_answer)     
#     ot_question_bank.append(new_question)
# print(question_bank)
# quiz = QuizBrain(question_bank)
# while quiz.still_has_questions():
#     quiz.next_question()

ot_quiz = QuizBrain(question_bank)
while ot_quiz.still_has_questions():
    ot_quiz.next_question()

print("Thanks for completing the quiz")
# print(f"You final score is {quiz.score}/{quiz.question_number}.")
print(f"You final score is {ot_quiz.score}/{ot_quiz.question_number}.")

