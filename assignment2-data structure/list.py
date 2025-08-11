#my empty list
my_list = []

#append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("This is my appended list", my_list)

#insert
my_list.insert(1,15)

print("This is my list with insert value", my_list)

#extending my list with additional elements
my_list.extend([50, 60, 70])

print("My extended list", my_list)

#removing the last element can use pop() or remove
my_list.pop(7)

print("Removed the last element using pop",my_list)

my_list.remove(60)

print("Removed the last element using remove",my_list)

#sort my list in ascending order

my_list.sort()

print("sorted list", my_list)

#finding and printing index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)


#final list
print("Final list:", my_list)