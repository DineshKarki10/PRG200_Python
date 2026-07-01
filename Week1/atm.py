
for i in range(3):
    username = input("Enter yourn  Name: ")
    password = int(input("Enter your password: "))
    if(username == "neymar" and password==12345):
        print(f"Welcome {username}")
        break
    else:
        print("Invalid Entry")

    print("You are blocked")
