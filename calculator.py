#***Python Calculator***
#Defining numbers as n1,n2


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2
#required operation
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
#main function
def calculator():

 

  number1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    number2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(number1, number2)
    print(f"{number1} {operation_symbol} {number2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type any alphabet to stop calculation: ") == 'y':
      number1 = answer
    
    elif input("Do you want to continue calculation if yes type n or if no type any alphabet : ") == 'n':
      should_continue = False
      pass
      calculator()
    else:
      break


calculator()


