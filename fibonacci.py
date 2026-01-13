a=0
b=1
n=10
count=0
while count<n:
    sum=a+b
    a=b
    b=sum
    count+=1
    print(a,end=" ")
