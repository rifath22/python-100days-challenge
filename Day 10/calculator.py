def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

num1 = int(input("What's the first number: "))
num2 = int(input("What's the second number: "))

for key in operations:
  print(key)

operation_input = input("Please pick one of the above operation: ")

output = operations[operation_input](num1, num2)
print(output)