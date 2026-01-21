def check(num):  
    eoro = "Even" if num%2==0 else "Odd"
    return eoro

number = int(input("Enter any number: "))
print(f"The number inputted by the user is {check(number)}")