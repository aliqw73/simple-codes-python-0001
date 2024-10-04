#How to Remove Duplicates From a Python List

mylist_1 = ["a", "b", "a", "c", "c"]
mylist_1 = list(dict.fromkeys(mylist_1))
print(mylist_1)

