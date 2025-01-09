# tuple : collection of heterogenious type of data which is indexed
# ordered, it is immutable (unchangeable), 
# creating a tuple we need to use parentheses () and we can't change the value of tuple after it is created.
# example: a=(2,4,5.3,...ETC)
# tuple is faster than list because it is immutable.
# tuple is more memory efficient than list because it is immutable.

# Indexing a Tuple:

# Tuple: (10, 20, 30, 40, 50)

# Index:  0    1    2    3    4
#         +----+----+----+----+----+
#         | 10 | 20 | 30 | 40 | 50 |
#         +----+----+----+----+----+

# To access a value, use the index:
# my_tuple[2] = 30
# my_tuple[4] = 50

# Example in Python:

# my_tuple = (10, 20, 30, 40, 50)
# print(my_tuple[2])  :: Output will be 30

# Positive Indexing:

# a = (3, 9.3, "abc", [1, 2], True, 45)

# Index:  0      1      2       3        4      5
#         +------+-------+-------+--------+------+------+
#         |  3   |  9.3  | "abc" | [1, 2] | True |  45  |
#         +------+-------+-------+--------+------+------+

# Negative Indexing:

# a = (3, 9.3, "abc", [1, 2], True, 45)

# Index:  -6     -5     -4      -3       -2     -1
#         +------+-------+-------+--------+------+------+
#         |  3   |  9.3  | "abc" | [1, 2] | True |  45  |
#         +------+-------+-------+--------+------+------+

a=(3,9.3,"abc",[1,2],True,45)
print(a)
print(type(a))