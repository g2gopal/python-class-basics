
#object oriented program
#class
class chair:
    height=10
obj=chair()
print(obj.height)

class person:
    def __init__(self,name,age):          #to access self paramaters
        self.name=name
        self.age=age
x=person("Jithu",31)
print(x.name,x.age)


#inheritance

class person:
    def __init__(self,name,age):      #1.single inheritance  #function called method
        self.name=name
        self.age=age
    def sample(self):                
        print(self.name,self.age)

class employee(person):
    pass
y=employee("jithu",31)
y.sample()



#2.multiple inheritance ----1 chil
#3.multilevel inheritance
#4.hirarchi
#5.hybrid inheritance


#polymorphism
#1.function Based
#2.class based
x="how much you can see"
print(len(x))
print(type(x))
y=[1,2,3,4,5,6,7]
print(len(y))
print(type(y))
z={2,3,4,5,56,7,0}
print(len(z))
print(type(z))
a={"name":"jithu","age":31,"place":"ernakulam"}
print(len(a))
print(type(a))



#data en capsilation=protect data



#method overloading
#operator overloading