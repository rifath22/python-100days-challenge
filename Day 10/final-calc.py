from art import logo

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
print(logo)
num1 = int(input("What's the first number: "))
should_continue = True
while should_continue:
  for key in operations:
    print(key)
    
  operation_input = input("Please pick one of the above operation: ")
  num2 = int(input("What's the second number: "))
  
  output = operations[operation_input](num1, num2)  #multiply(3, 2) = 6
  print(f"The value of {num1} {operation_input} {num2} is {output}")

  next_input = str(input("Do you want to continue: ")).lower()
  if next_input == "no":
    should_continue = False
  else:
    num1 = output