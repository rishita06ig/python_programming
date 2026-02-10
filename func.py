a=[1,2,1,3,4,5,1,3,6,6]

b=a.copy()
print("a =",a)
print("b =",b)

c=a.count(1)
print("c =",c)

str1="Hello World"
e=str1.split("o")
print(e)

str2=("This is","ME")
str="..".join(str2)
print(str)

a=[1,2,1,3,4,5,1,3,6,7]
b=a
c=a.copy()
print(c)
b.append(3)
c.append(4)
print(b)
print(c)
