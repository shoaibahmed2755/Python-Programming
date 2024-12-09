#Adding elements inside the list 
#  1.append() --> add 1 ele at the last of the list 
#  2.insert() --> add 1 ele at the specified position
#  3.extend() --> add multiple elements at the last of the list
# a=[3,11,56,67,45,90,"abc"]
# print(a)

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

# append() -->
# a.extend([11,22,33])
# print(a)

# a=[3,5,6,7]
# print(a)
# a.append("aabc")
# print(a)
# a.extend("abc")
# print(a)
# a.extend(["abc"])
# print(a)

#Removing elements inside the list 
    # 1.pop() --> remove one ele form the list by using the Index
    # 2.remove() --> remove one ele
    # 3.del() --> remove one or more ele 
    # 4.clear() --> remove all the ele in the list
    
a=[1,2,3,4,5,6,7,8,9]
print(a)
a.remove(1)
print(a)
a.remove(9)
print(a)