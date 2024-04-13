with open('file1.txt') as f1:
  file1_contents = f1.readlines()

with open('file2.txt') as f2:
  file2_contents = f2.readlines()
# Write your code above 👆

result = [int(value) for value in file1_contents if value in file2_contents]
print(result)


