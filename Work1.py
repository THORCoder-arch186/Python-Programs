num_T = 0
sum_T = 0

while True:
    num_T = int(input("Pls enter a pos num, or neg num to stop"))
    if num_T < 0:
        break
    sum_T += num_T

print("The sum of the numbers entered by the user is:", sum_T)