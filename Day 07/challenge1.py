#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_input = str(input("Please choose a letter")).lower()
# print(user_input)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
split_chosen_word = list(chosen_word)
print(split_chosen_word)

if user_input in split_chosen_word:
  print("chosen letter is present in the word")
else:
  print("letter is not in the word")