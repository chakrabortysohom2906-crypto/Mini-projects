#Simple Calculator

first_number = int(input("enter your first number:"))
second_number = int(input("enter your second number:"))
operator = input("enter the oparetor:")

if operator == '+':
    print("answer:",first_number + second_number)
elif operator == '-':
    print("answer:",first_number-second_number)
elif operator == '*':
    print("answer:",first_number*second_number)
elif operator == '/':
    if second_number != 0:
        print("result:",first_number/second_number)
        print("remainder:",first_number%second_number)
    else:
        print("the second number is 0.(something not divisible by 0).")
   
else:
    print("enter a valid operator.")
