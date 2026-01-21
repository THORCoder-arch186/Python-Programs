num = int(input("Enter any number to find multiples of five from 1 to the number: "))
for i in range(1, num+1):
    if i % 5 == 0: 
        print(i)
