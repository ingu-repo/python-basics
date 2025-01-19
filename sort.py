# list
list = [2, 5, 1, 9, 7]
list.sort()
print (list)

# by length
list = ["kepler", "sean", "jonathan", "taylor", "sam"]
list.sort(key=len)
print (list)

# tuple in list
list = [("john", 30), ("pole", 8), ("sean", 21)]
list.sort(key = lambda list:list[1])
print (list)


