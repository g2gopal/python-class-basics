# 1+4+9+16+................. sqrs sum


numberofterms=int(input("enter the numbr of terms"))
sum=0
for i in range(2,numberofterms+1):
    sum+=i*i
print(sum)