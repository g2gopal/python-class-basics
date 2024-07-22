# #area of A CIRCLE

import math
r=int(input("enter radius vale "))
area=math.pi*r**2
print(area)


# #surface area of cone
# x=int(input("enter radius vale "))
# l=int(input("enter lateral length"))
# area1=math.pi*x*l
# print(area1)


# areab trapizoid
a1=int(input("enter a "))
b1=int(input("enter b"))
h=int(input("enter height h"))
area2=(a1+b1)*h/2
print(area2)


a=[7,8,120,25,44,20,27]
for i in a:
    if i%2!=0:
        print(i)
