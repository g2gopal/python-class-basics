
def printname() : #def 'name of fuction
       print("HELLO")
printname()

def sums():
       x=4
       y=7
       sum=x+y
       print(sum)
sums()

#arguments
def subtra(a,b):    #a,b parameters
       print(a-b)
subtra(9,8)         #arguments 9,7


#arbitrary arguments(based on number of arguments)
#key word arguments
#arbitrary keyword arguments


def numbers(*q):             # *args
       print(q[3])
numbers("apple","orange","kiwi","grapes")


def su(*w):
      print(w[1]*w[1])
su(2,4,6)



#kwargs
def multi(x,y,z):
       print(x*y*z)
multi(x=2,y=7,z=9)



#**kwar0gs



def sum(**x):
       print(x["i"]+x["j"])
sum(i=8,j=9,k=54,l=4)




#default parameter
def mycountry(c="India"):
       print("I'm from "+c)
mycountry("usa")
mycountry("uk")
mycountry()




def fruits(f):
       for i in f:
        print(i)
s=["apple","banana","jackfruit","kiwi"]
fruits(s)





#return statement

def sum1(x1):
      return 10+x1
print(sum1(8))      
      


def series():
      pass





#LAMDA

y=lambda x:x+5
print(y(10))



z=lambda x,y:x+y
print(z(1,2))


