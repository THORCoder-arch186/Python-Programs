correct_password = "python123"

for attempt in range(3):
    password = input("Enter password: ").strip()
    if password == correct_password:
        print("Access Granted, Enjoy!")
        break
    else:
        print("Wrong Password, try again! ")
else:
    print("Too many attempts. Access Denied")