#Adding elements inside the list 
#  1.append() --> add 1 ele at the last of the list 
#  2.insert() --> add 1 ele at the specified position
#  3.extend() --> add multiple elements at the last of the list
a=[3,11,56,67,45,90,"abc"]
print(a)

# append() -->
# a.append(100)
# print(a)
# a.append(True)
# print(a)
# a.append([1,2])
# print(a)
# print(a[::-1]) #reversing the list

# insert() -->
# a.insert(1,100)
# print(a)
# a.insert(3,[1,2,3])
# print(a)
# a.insert(-1,200)
# print(a)

a.extend([11,22,33])
print(a)