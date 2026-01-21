basket = []

while True:
    item = input("Enter fruit (type stop to finish): ").lower()
    if item == "stop":
        break
    basket.append(item)

print("Your basket contains:")
for fruit in basket:
    print(fruit)
