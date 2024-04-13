from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")

EASY = 10
HARD = 5

computer_list = list(range(1,101))
computer_choice = random.choice(computer_list)
# print(computer_choice)
difficulty_level = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
if difficulty_level == "easy":
    attempts = EASY
else:
    attempts = HARD

print(f"You have {attempts} attempts to guess the number")

while attempts > 0:
    user_guess = int(input("Make a guess: "))
    if user_guess == computer_choice:
        print(f"You got it! The answer was {user_guess}")
        break
    elif user_guess > computer_choice:
        print(f"Too high")
        print(f"Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")
    elif user_guess < computer_choice:
        print(f"Too Low")
        print(f"Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")
    else:
        print("You lose")

print(f"The computer answer is {computer_choice}")