#[0,1,1,2,3,5,8]

def fibinocii(x):
    z=[]
    a=0
    b=1
    z.append(a)
    z.append(b)
    
    for i in range(0,x+1):       #1,2,3,4,5
            c=a+b
            a=b
            b=c
            z.append(c)
    print(z)
    print(z[5])
fibinocii(5)

# e=int(input("enter a number "))
# i=0
# while i<=e:
#     print(i)
#     i+=2



t=int(input("enter a number "))
i=0
while i<=t:
     if (i % 2) == 0:
        print(i)
        i+=2