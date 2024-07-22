# 1+3+5+7+...... first odd numbers
n=int(input("enter the number of terms"))
sum=0
start=1
for i in range(1,n+1):
    sum=start+sum
    start+=2
print(sum)
