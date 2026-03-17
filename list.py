##Create and print list
list_ = [10,20,3,50]
print(list_)

##Access elements in list
print(list_[1])
print(list_[-2])

##Modify list
list_[2]=40
print("modified ",list_)

##add and remove elements
list_.append(60)
print("added ",list_)
list_.insert(2,30)
print("added ",list_)

list_.pop(-1)
print("removed ",list_)
list_.remove(50)
print("removed ",list_)

##copy using slicing
copy_list = list_[:]
print("copy list ",copy_list)

##copy list using constructor
new_list=list(list_)
print(new_list)
