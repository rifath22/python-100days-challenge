rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_input == 0:
  print("User chooses:")
  print(rock)
elif user_input == 1:
  print("User chooses:")
  print(paper)
elif user_input == 2:
  print("User chooses:")
  print(scissors)
else:
  print("Please choose the correct input")

inputs = [0, 1, 2]
computer_input = random.choice(inputs)
if computer_input == 0:
  print("computer chooses:")
  print(rock)
elif computer_input == 1:
  print("computer chooses:")
  print(paper)
else:
  print("computer chooses:")
  print(scissors)
print(f"user_input: {user_input}")
print(f"computer_input: {computer_input}")

if user_input == 0 and computer_input == 2:
  print("User Won")
elif user_input == 0 and computer_input == 1:
    print("computer Won")
elif user_input == 1 and computer_input == 0:
  print("User Won")
elif user_input == 1 and computer_input == 2:
    print("computer Won")
if user_input == 2 and computer_input == 1:
  print("User Won")
elif user_input == 2 and computer_input == 0:
    print("computer Won")
elif user_input == computer_input:
  print("Match Draw")