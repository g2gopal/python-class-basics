q={1,2,3,4,5,6,7,8,1,2}    #repeated values
print(q)
print(len(q))
print(type(q))


print(set((11,12,13)))
print(12 in q)
print(1 in q)
print(1 not in q)
print(0 not in q)


for i in q:
    print(i)


q.add("hello")
print(q)


w={11,12,13,14}


q.update(w)
print(q)

q.remove("hello")
print(q)

#q.remove("world")
#print(q)

q.discard("hi")
print(q)


q.discard(14)
print(q)


x=q.pop()
print(x)
print(q)

# q.clear()
# print(q)

# del q
# print(q)

i={1,2,3,4,5,6,"orange"}
j={"mango","orange","apple","kiwi"}

x=i.union(j)
print(x)


y=i.union(j,q)
print(y)

z=i.intersection(j)
print(z)


r=i.difference(j)
print(r)