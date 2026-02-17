def pset(a,lst):
    if len(a)==0:
        print(lst)
    else:
        pset(a[1:],lst)
        pset(a[1:],lst+[a[0]])

a=["a","b","c"]
pset(a,[])