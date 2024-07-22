course=["python","da","ds","flutter","mern"]
fees=[20000,30000,40000,50000,60000]


print(course)
print(fees)
print(type(course))
print(type(fees))
print(len(course))
print(len(fees))
print(course[2])
print(course[0:4])
print(course[-1])
print(course[-4:-1])
for i in course:
    print(i)

x=course+fees
print(x)

course.append("java")     #add last

print(course)

course[5]="data analyst"
print(course)


course.insert(2,"data sciense")
print(course)


course.pop(3)
print(course)


course.remove("da")
print(course)



del course[3]
print(course)

course.clear
print(course)
num=98

x=20
y=30
print(x,"is greater than",y)