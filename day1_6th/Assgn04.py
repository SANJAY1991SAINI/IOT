def maximum()
    n1= int(input("Enter n1: "))
    n2= int(input("Enter n2: "))
    n3= int(input("Enter n3: "))

    if (n1>n2) & (n1>n3):
        print("n1 is greater")

    elif (n2>n1) & (n2>n3):
        print("n2 is greater")

    elif (n3>n1) & (n3>n2):
        print("n3 is greater")

    else:
        print("Invalid Input")

maximum()