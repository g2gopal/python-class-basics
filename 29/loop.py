i=0
# while i<11:
#      print(i)
#      i+=1         


while i<21:
    print(i)
    i+=2

#break
x=1
while x<11:
    print(x)
    if x==5:
        break
    x+=1
#continue
y=0
while y<12:
    y+=1

    if y==6:
        continue
    print(y)

x="hello world"
for i in x:
    print(i)

list=[9,8,7,6,5,4,3,2,1]
for i in list:
    print(i)


tuple=(22,23,24,25,26)
for i in tuple:
    print(i)

y={"name":"jithu","age":31,"location":"ernakulam"}
for i in y:
    print(i)

for i in y.values():
    print(i)

for i in list:
    print(i)
    if i==5:
        break

for i in list:
    if i==5:
        continue
    print(i)



for i in range(5):
    print(i)


for i in range(1,5):
    print(i)

for i in range(1,21,2):
    print(i)



a=[1,2,3]
b=["a","b","c"]

for i in a:
    for j in b:
        print(i,j)


