
while True:
    def print_factors(x):
        print("The factors of", x,"are:")
        for i in range(1, x+1):
            if x % i == 0:
                print(i)

    num = int(input("What number factors u want?! :"))
    print_factors(num)

    cont = str(input("Wanna continue?")).strip().lower()
    if cont != "yes":
        break