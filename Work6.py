num = float(input("Enter a number: "))

if abs(num)>=10 and abs(num)<=99:
    print("It is a two-digit number.")
elif abs(num)>=100 and abs(num)<=999:
    print("It is a three-digit number.")
elif abs(num)>=100 and abs(num)<=9999:
    print("It is a four-digit number.")
else:
    print("the number u have entered isnt 2, 3 or 4 digit")
