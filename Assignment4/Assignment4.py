num = input("Enter a positive number: ")
primediv = ["2", "3", "5", "7"]
while True:
    if num.isdigit() :
        if int(num) > 1 and int(num)%int(num) == 0 and int(num)%2 != 0 and int(num)%3 != 0 and int(num)%5 != 0 and int(num)%7 != 0:
            print(f"{num} is a prime number")
            break
        elif num in primediv:
            print(f"{num} is a prime number")
            break
        else:
            print(f"{num} is not a prime number")
            break
    else:
        print("Please enter a valid number! ")
        num = input("Enter a positive number: ")