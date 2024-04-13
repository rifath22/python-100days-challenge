import pandas as pd
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
data = pd.read_csv('./nato_phonetic_alphabet.csv')
# print(data)
dict_phonetic = {row.letter:row.code for (index, row) in data.iterrows()}
# for (index, row) in data.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(f"letter: {row.letter} and code: {row.code}")
# print(dict_phonetic)

user_input = str(input("Please enter a word: ")).upper()
# for letter in user_input:
#     print(f"letter: {letter} and its code is {dict_phonetic[letter]}")
output_list = [dict_phonetic[letter] for letter in user_input]
print(output_list)