print("Welcome to the Python CLI Calculator tool...")

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
arith_type = int(input("1 to Add,\n2 to Subtract, \n3 to multiply, \n4 to Divide, \n5 to find remainder \n Enter an operation type: "))

def add():
  print(first_num, "added to", second_num, "is", first_num + second_num )

def subtract():
  print(first_num, "subtracts", second_num, "to give", first_num - second_num)

def divide():
  print(first_num, "divided by", second_num, "gives", first_num / second_num)

def multiply():
  print(first_num, "multiplied by", second_num, "gives",first_num * second_num)

def modulo():
   print(first_num, "divided by", second_num, "gives a remainder of",first_num % second_num)

if arith_type == 1:
  add()
elif arith_type == 2:
  subtract()
elif arith_type == 3:
   multiply()
elif arith_type == 4:
   divide()
elif arith_type == 5:
  modulo()   
else:
  print("Invalid Arithmetic type")   

  