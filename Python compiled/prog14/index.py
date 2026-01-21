numbers = [2,13,8,96,57,12,77,39,67,66,32]
even_numbers = []
count_even = 0

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        count_even += 1

print("Even numbers:", ", ".join(map(str, even_numbers)))
print("Number of even values =", count_even)
