# Write a program to accept a 4 digit number and
# b. Display place value of each decimal digit

number= int(input("Enter a 4 digit number: "))
num=number

a=num%10
num=int(num/10)

b=num%10
num=int(num/10)

c=num%10
num=int(num/10)

d=num%10
num=int(num/10)
    
print(f"{number} = {d*1000} + {c*100} + {b*10} + {a}")