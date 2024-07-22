# #1.calculate the product and sum 0f two numbers(num1=20,num2=30)

def sum():
    num1=20
    num2=30
    pro=num1*num2
    sum=num1+num2
    print(pro)
    print(sum)
sum()
# #2calculate the average of30,100,2000
# a1=30
# a2=100
# a3=2000
# sum1=a1+a2+a3
# print(sum1/3)

# #3create a function that takes an integer n as input and returns the sum of all numbers from 1 to n 'use a loop'
# def function(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     print(sum)
# function(8)
# #4.write a function to calculate the factorial of a given number
# def factorial(n):
#     fact=1
#     for i in range (1,n+1):
#         fact=fact*i
#         i+=1
#     print(fact)
# factorial(4)

# #5.create a function that checks whether a given year leap year or not
# def leap():
#     year=int(input("enter a year to check whether leap year or not "))
#     if (year % 4)==0 and (year % 100)!=0 or (year % 400)==0:
#         print("leap year")
#     else:
#         print("not a leap year")
# leap()
#6.write a function to generate th fibinacii sequence upto aspecified number 'n' use a loop to print the sequence
# def fibinacii(x):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range (2,x):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fibinacii(3)
  
#prime number
def num():
    num=59
    if num == 1:
        print("number is not a prime number")
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
               print("number is not a prime number")
               return False
    else:
       print(num,"is a prime number")
       return True
num()



     