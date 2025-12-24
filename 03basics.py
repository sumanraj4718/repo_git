# Ques1.Checking positive or negative number.
# a=int(input("Enter a number:"))
# if a>0:
#     print("positive number.")
# elif a<0:
#     print("Negative number")
# else:
#     print("Zero")

#ques2.Check Leap year or not.
# year=int(input("Enter year: "))
# if (year%400==0) or(year%4==0 and year%100!=0):
#     print("This is a leap year.")

# else:
#     print("This isn't a leap year.")

#ques3.Multiplication Table.
# a=int(input("Enter a natural number:"))
# for i in range(1,11):
#     table=a*i
#     print(a,"X",i,"=",table)

#ques4.Count number of digits using while loop.
# num = int(input("Enter a number: "))
# count = 0

# while num > 0:
#     count += 1
#     num //= 10

# print("Number of digits:", count)

#ques5.Reversing a number.
# num = int(input("Enter a number: "))
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10

# print("Reversed number:", rev)

#ques6.Factorial of a number.
# a=int(input("Enter the number:"))
# fact=1
# i=1
# while i<=a:
#     fact=fact*i
#     i+=1
# print("Factorial:",fact)


#ques7. Armstrong number.
# num = int(input("Enter a number: "))
# temp = num
# n = len(str(num))
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** n
#     temp //= 10

# if sum == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



#Q.8

#Skips multiple of 5
a=1

while a<21:
    if a%5!=0:
        print(a,sep=" ",end=" ")
        a+=1
    elif a%5==0:
        a+=1

#Stops when number reaches 16

a=1
print()
while a<17:

    print(a,sep=" ",end=" ")
    a+=1

#Q.9

num=input('Enter the no to be reversed:')
print('Given Number:',num)
rev=num[::-1]
print('Reverse:',rev)

if num==rev:
    print('The no is Palindrome')
else:
    print('The no is not Palindrome')

#Q.10

#Square star pattern


a="*"

for i in range(4):
    for j in range(4):
        print(a,sep=" ",end=" ")
    print()

#Square with gaps

a='*'

for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
            print(a,sep=" ",end=" ")
        else:
            print(" ",sep=" ",end=" ")
    print()

#pyramid

a=1

for i in range(5):
    print(" "*(4-i) + "*"*a)
    a+=2