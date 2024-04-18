# Write a program to accept a 4 digit number and
# c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 output should be

number= int(input("Enter a 4 digit number: "))
num=number
rem=0
rev=0

while num>0:
    rem=num%10
    rev=rev*10+rem
    num=int(num/10)
    
print(f"{rev}")

