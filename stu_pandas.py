import pandas as pd 
data1 = {
    "Name" : ['a','b','c','d','e','f'],
    "Roll No." : [1,2,3,4,5,6],
    "Marks" : ['45','50','33','35','40','43']
}
data2 = {
    "Name" : ['a','b','c','d','e','f'],
    "Roll No." : [1,2,3,4,5,6],
    "Attendance" : ['85','99','78','79','85','90']
}
f1 = pd.DataFrame(data1)
f2 = pd.DataFrame(data2)

df_merge=pd.merge(f1,f2,on=['Roll No.','Name'],how='outer')
print(df_merge)