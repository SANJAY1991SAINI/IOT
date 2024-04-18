#Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit

num= int(input("Enter a 4 digit number: "))
while num>0:
    a=num%10
    num=int(num/10)

    b=num%10
    num=int(num/10)

    c=num%10
    num=int(num/10)

    d=num%10
    num=int(num/10)
    
print(f"{d} {c} {b} {a}")
