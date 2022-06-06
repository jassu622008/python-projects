def add(n1, n2):
  res = int(n1 + n2)
  print(res)
  
def subtract(n1, n2):
  res = int(n1 - n2)
  print(res)

def multiply(n1, n2):
  res = int(n1 * n2)
  print(res)
  
def divide(n1, n2):
  res = int(n1 / n2)
  print(res)
  
def modules(n1, n2):
  res = int(n1 % n2)
  print(res)
  
  print("""
    1. add
    2. subtract
    3. multiply
    4. divide
    5. modules
  """)
  
  command = int(input("Enter Your Command: "))
  
  if command == 1:
    n1 = int(input("Enter First Number: "))
    n2 = int(input("Enter Second Number: "))
    add(n1, n2)
  if command == 2:
    n1 = int(input("Enter First Number: "))
    n2 = int(input("Enter Second Number: "))
    subtract(n1, n2)
    
  if command == 3:
    n1 = int(input("Enter First Number: "))
    n2 = int(input("Enter Second Number: "))
    multiply(n1, n2)
    
  if command == 4:
    n1 = int(input("Enter First Number: "))
    n2 = int(input("Enter Second Number: "))
    divide(n1, n2)
    
  if command == 5:
    n1 = int(input("Enter First Number: "))
    n2 = int(input("Enter Second Number: "))
    modules(n1, n2)
