a={"name":"jithu","age":31,"place":"ernakulam","house name":"maniyalil"}   #item keys values
print(a)
print(type(a))
print(len(a))
print(a["age"])
b=dict(color="red",fruit="apple")
print(b)
print(b["color"])
print(b.get("fruit"))
print(b.keys())
print(b.values())
print(b.items())
print("year" in b)
print("year" not in b)
b["color"]="black"
print(b)
b.update({"fruit":"kiwi"})
print(b)
b["veg"]="tomato"
print(b)
b.update({"age":31})
print(b)
b.pop("age")
print(b)
b.popitem()
print(b)



del b["color"]
print(b)
# b.clear()
# print(b)


# del b
# print(b)



for i in b:
    print(i)


for i in b:      #keys
    
    print(b[i])



for i in a.keys():
    print(i)

for i in a.values():
    print(i)

for i in a.items():
    print(i)






b=a.copy()
print(b)

c=dict(a)
print(c)


family={"child1":{"name":"eva","age":3},"child2":{"name":"oreo","age":4},"child3":{"name":"paaru","age":21}}
print(family)

print(family["child2"])

print(family["child2"]["name"])


print(family["child3"]["age"])
b={"car":"audi","model":"q7"}
print(b)