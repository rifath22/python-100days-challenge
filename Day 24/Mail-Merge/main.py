# Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



def update(names):
    with open('c:/Users/azabdul2001/Desktop/PythonChallenge/Version 2/Day 24/Mail-Merge/Input/Letters/starting_letter.txt') as f:
        letter_contents = f.read()
        letter_contents = letter_contents.replace("[name]", names)
        
    filename = f"letter_for_{names}.txt"
    
    with open(f"c:/Users/azabdul2001/Desktop/PythonChallenge/Version 2/Day 24/Mail-Merge/Output/ReadyTosend/{filename}", mode='w') as out_file:
        out_file.write(letter_contents)


with open('c:/Users/azabdul2001/Desktop/PythonChallenge/Version 2/Day 24/Mail-Merge/Input/Names/invited_names.txt') as f:
    names = f.readlines()
name_list = []

for i in range(0,len(names)):
    name_list.append(names[i].strip())
# print(name_list)

for names in name_list:
    update(names)