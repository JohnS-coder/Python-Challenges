while True:
    year = int(input("Enter the year('0' to quit): "))
    if year == 0 :
        break
    elif year%4 == 0 and year%100 != 0 :
        print(f"{year} --> is a leap year! ")
    elif year%400 == 0:
        print(f"{year} --> is a leap year! ")
    else:
        print(f"{year} --> is not a leap year!")