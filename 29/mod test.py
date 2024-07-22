import math
import random
import datetime
import moduletype
print(moduletype.sum(5,8))
print(moduletype.sub(9,6))
print(moduletype.mult(5,9))
print(moduletype.divi(9,3))



#builtin
print(max(8,9,10,6,2,99,1,100))
print(min(11,22,33,44,55))
print(abs(-435))     #absolue value
print(pow(3,4))      #power 

print(math.pi)
print(math.sqrt(16))
print(math.ceil(7.8))
print(math.ceil(2.1))
print(math.floor(-9.6))
print(math.floor(9.6))
print(math.factorial(4))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))

print(random.randrange(1,6))


print(datetime.datetime.now())
x=datetime.datetime(2022,1,31)
print(x.strftime("%A"))

       
print(x.strftime("%a"))

print(x.strftime("%B"))
print(x.strftime("%b"))

print(x.strftime("%y"))
print(x.strftime("%Y"))


