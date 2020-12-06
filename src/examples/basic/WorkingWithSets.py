# Sets have unique elements, not sorted in any order
# https://www.programiz.com/python-programming/set

# A set is an unordered collection of items. Every set element is unique (no duplicates)
# and must be immutable (cannot be changed).
# However, a set itself is mutable. We can add or remove items from it.
# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.
#   ->  error !!
#   my_set = {1, 2, [3, 4]}

# -----------------------------
# Making an empty set is tricky
# Distinguish set and dictionary while creating empty set

# initialize a with {} - this creates an empty dictionary !
a = {}

# check data type of a  -> dict
print(type(a))

# initialize a with set()
a = set()

# check data type of a  -> set
print(type(a))

# ============================
# initialize my_set
my_set = {1, 3}
print(my_set)

# if you uncomment
# you will get an error
# TypeError: 'set' object does not support indexing  - since its not stored in any order
# my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)


# ====================================
# Difference between discard() and remove()
#  remove() on a missing entry will raise an error
#  discard() on a missing entry will leave set unchanged

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

#  my_set.remove(2)  # ERROR !


# =====================
# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element  - random order ! there is no ordering
# Output: random element
print(my_set.pop())

# pop another element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)

print(my_set)

# ===============
# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

# use union function
A.union(B)
#{1, 2, 3, 4, 5, 6, 7, 8}

# use union function on B
B.union(A)
#{1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)

# use intersection function on A
A.intersection(B)
#{4, 5}

# use intersection function on B
B.intersection(A)
#{4, 5}


# Difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)


# use difference function on A
A.difference(B)
#{1, 2, 3}

# use - operator on B
B - A
#{8, 6, 7}

# use difference function on B
B.difference(A)
#{8, 6, 7}


# =============================================
#Symmetric Difference of A and B is a set of elements in A and B but not in both (excluding the intersection).

#Symmetric difference is performed using ^ operator. Same can be accomplished using the method symmetric_difference().

# Symmetric difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)

# use symmetric_difference function on A
A.symmetric_difference(B)
#{1, 2, 3, 6, 7, 8}

# use symmetric_difference function on B
B.symmetric_difference(A)
#{1, 2, 3, 6, 7, 8}