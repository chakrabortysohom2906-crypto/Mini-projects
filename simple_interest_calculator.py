principle = int(input("enter your principle amount:"))
interest_rate = float(input("enter the interest rate:"))
time = int(input("enter the time in years only:"))

simple_interest = (principle*interest_rate*time)/100
total_amount = (principle + simple_interest)

print("this is the interest you got:",simple_interest)
print("this is the total amount you got:",total_amount)
print()