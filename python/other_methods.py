# SOME OTHER METHODS ARE
# INDEX() -> ACCESSNIG THE INDEX ValueError
# COUNT() -> COUNT THE NUMBER OF ELEMENTS IN THE LIST
# REVERSE() -> REVERSE THE LIST
# SORT() -> SORT THE LIST IN ASCENDING ORDER OR DESCENDING ORDER 
# COPY() -> CREATE A COPY OF THE LIST

# a=[2,7,4,9,2,5,6,5,2,2,7,1]
# print(a)
# print(a.count(2)) # COUNT THE NUMBER OF OCCURENCE OF 2 IN THE LIST
# print(a.index(7)) # ACCESS THE INDEX OF 2 IN THE LIST
# a.reverse()
# print(a)
# a.sort(reverse=False)
# print(a)

a=[11,22]
b=[33,44]
c=a.copy()
d=a
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d)) # id() function returns the “identity” of the object, which is
a.append(45)
print(a)
print(b)
print(c)