print("program to fnd greatest number of five")

while True:
    def find_big(a, b, c, d, e):
        big = a
        if b > big:
            big = b
        elif c > big:
            big = c
        elif d > big:
            big = d
        elif e > big:
            big = e

        return big
    
    a = int(input("Enter your 1st number to be compared to find their greatest:"))
    b = int(input("Enter your 2nd number to be compared to find their greatest:"))
    c = int(input("Enter your 3rd number to be compared to find their greatest:"))
    d = int(input("Enter your 4th number to be compared to find their greatest:"))
    e = int(input("Enter your 5th number to be compared to find their greatest:"))
    print("The series of numbers entered is:", a, b, c, d, e)

    large = find_big(a, b, c, d, e)
    print("The largest from the series of number is", large)

    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Bye")
        break