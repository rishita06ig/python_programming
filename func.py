import copy

a=[1,2,1,3,4,5,1,3,6,6]

b=a.copy()
print(a)
print(b)

c=a.count(1)
print(c)

str1="Hello World"
d=str1.split("o")
print(d)

str2=("This is","ME")
str="..".join(str2)
print(str)

aa=[[1,2],[3,4]]
bb=aa
cc=copy.deepcopy(aa)
print(cc)
bb[0].append(5)
cc.append(4)
print(bb)
print(cc)

a1="I'm busy right now"
word=a1.split()
word1=word[::-1]
rev_word=" ".join(word1)
print(rev_word)


strr=[2,5,4,10,1,5,3]
print(strr[-2:-6:-1])

strb=([2,3],[4,5,10])
strb[0].append(5)
print(strb)
strb[0][0] = 1
print(strb)
