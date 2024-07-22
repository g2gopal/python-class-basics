""" list-set of items can  ,add datas indexed,mutable,ordered,duplicate datas allowed

"""
a=["apple","orange","mango","banana","grapes"]
print(a)
print(type(a))
print(len(a))   #count only items

b=list((1,2,3,4,5,6))
print(b)
print(a[1])
print(b[-1])

print(a[1:4])

print(b[1:])

print(a[:4])

print(a[-1])

print(b[-4:-1])

print("orange" not in a)


print("orange" in a)


a=["apple","orange","mango","banana","grapes"] 
a[1]="kiwi"   #replace

print(a)

a.append("orange")    #add one item

print(a)


a.insert(2,"papaya")  #paricular [position]

print(a)



a.extend(b)  #add A LIST
print(a)

#remove
a.remove("orange")

print(a)

a.pop(3)  
print(a)

a.pop()     #remove last
print(a)

del a[3]
print(a)




# a.clear()
# print(a)


# del a
# print(a)

for i in a:
    print(i)


x=["apple","orange","mango","banana","grapes"]

x.sort()
print(x)


x.sort(reverse=True)
print(x)


y=x.copy()
print(y)

z=list(x)
print(z)


print(x+b)


a.extend(b)
print(a)

c=a.count("papaya")
print(c)