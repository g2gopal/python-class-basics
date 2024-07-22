a=(1,2,3,5,"apple")
print(a)
print(len(a))
print(type(a))
print(a[4])
print(1 in a)
print(6 not in a)
print(3 not in a)

print(a[0:4])

print(a[-1])

print(a[-4:-1])

print(a[-3:])

x=tuple(("mango","kiwi","banana"))
print(x)



v=("hi")
print(type(v))

j=(1,)    # , 
print(type(j))






a=list(x)
print(a)
print(type(a))
a.append("joy")
print(a)

a[1]=("orange")
print(a)
x=tuple(a)
print(x)
print(type(x))

for i in x:
    print(i)



q=(1,2,3,4,5)
print(type(q))
w=(x+q)
print(w)


e=(w*2)
print(e)
print(e.count("mango"))


 