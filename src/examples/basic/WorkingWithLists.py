
## https://towardsdatascience.com/15-things-you-should-know-about-lists-in-python-c566792eca98

# empty list
empty_list = []

# list of numbers
numbers = [1, 2, 3, 4, 5]

# list of cities
cities = ['Valencia', 'Munich', 'Madrid']

# lists can contain elements of different types as well as duplicated elements
elements = [1, 'A', 'A', False]




import numpy as np
import pandas as pd
### create a list from ###

# a string
list('Amanda')
# ['A', 'm', 'a', 'n', 'd', 'a']

# a tuple
list(('Madrid', 'Valencia', 'Munich'))
# ['Madrid', 'Valencia', 'Munich']

# a dictionary
list({'hydrogen': 1, 'helium': 2, 'carbon': 6, 'oxygen': 8})
# ['hydrogen', 'helium', 'carbon', 'oxygen']

# a set
list({'Madrid', 'Valencia', 'Munich'})
# ['Munich', 'Madrid', 'Valencia']

# a range object
list(range(15))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# a numpy array
list(np.array([1, 2, 3]))
# [1, 2, 3]

# a pandas series
list(pd.Series(['a', 'b', 'c']))
# ['a', 'b', 'c']

# the constructor list without any argument
empty_list = list()

print(empty_list)
# []

# list of cities
cities = ['Madrid', 'Munich', 'Valencia', 'Stuttgart']

# access the first element of the list
cities[0]
# 'Madrid'

# access the last element of the list
cities[3]
# 'Stuttgart'

# try to access an index out of range
cities[4]
# IndexError

# list of cities
cities = ['Madrid', 'Munich', 'Valencia', 'Stuttgart']

# access the first element of the list with a negative value
cities[-4]
# 'Madrid'

# access the last element of the list with a negative value
cities[-1]
# 'Stuttgart'

# try to access an index out of range
cities[-5]
# IndexError

# list of cities
cities = ['Madrid', 'Munich', 'Valencia', 'Stuttgart']

# access the first element of the list with a negative value
cities[-4]
# 'Madrid'

# access the last element of the list with a negative value
cities[-1]
# 'Stuttgart'

# try to access an index out of range
cities[-5]
# IndexError

# list of numbers
numbers_list = [1, 2, 3]

# we can access an item of the list because lists are ordered containers
numbers_list[0]
# 1

# set of numbers
numbers_set = {1, 2, 3}

# we can not access an item of the set because sets are unordered containers
numbers_set[0]
# TypeError

# list of products
products = ['table', 'chair', 'lamp', 'closet', 'bed']

# modify a single item
products[1] = 'shelf'

# print products to observe the modification
print(products)
# ['table', 'shelf', 'lamp', 'closet', 'bed']

# modify multiple items - modification of indexes 0 and 1
products[:2] = ['pillow', 'desk']

# print products to observe the modification
print(products)
# ['pillow', 'desk', 'lamp', 'closet', 'bed']

# list of products
products = ['table', 'chair', 'lamp', 'closet', 'bed', 'shelf', 'computer']

# remove the first item of the list using the del keyword
del products[0]
# check the modification
print(products)
# ['chair', 'lamp', 'closet', 'bed', 'shelf', 'computer']

# remove the last item of the list using the del keyword
del products[-1]
# check the modification
print(products)
# ['chair', 'lamp', 'closet', 'bed', 'shelf']

# remove the first and the second items of the list using the del keyword
del products[:2]
# check the modification
print(products)
# ['closet', 'bed', 'shelf']

# remove the entire list
del products
# check the modification
print(products)
# NameError

# list of cities
cities = ['Valencia', 'Munich', 'Ingolstadt', 'Stuttgart']

# remove the item at index 2
city_removed = cities.pop(2)

# the pop function returns the removed item
print(city_removed)
# Ingolstadt

# list of cities
print(cities)
# ['Valencia', 'Munich', 'Stuttgart']

# list of cities
cities = ['Valencia', 'Munich', 'Madrid', 'Barcelona', 'Valencia', 'Madrid']

# remove the first matching element with the list.remove() method
cities.remove('Valencia')

# check the modification
print(cities)
# ['Munich', 'Madrid', 'Barcelona', 'Valencia', 'Madrid']

# if the element we try to remove is not present an exception is raised
cities.remove('Paris')
# ValueError

# list of products
products = ['table', 'chair', 'lamp']

# insert an element at index 0
products.insert(0, 'closet')

# check the modification
print(products)
# ['closet', 'table', 'chair', 'lamp']

# insert an element at the end of the list
products.insert(len(products), 'computer')

# check the modification
print(products)
# ['closet', 'table', 'chair', 'lamp', 'computer']

# insert an element at the second-to-last index
products.insert(-1, 'bed')

# check the modification
print(products)
# ['closet', 'table', 'chair', 'lamp', 'bed', 'computer']

# list of numbers
numbers = [5, 10, 16]

# insert an integer (4) at index 0
numbers.insert(0, 4)

# insert a list [2,3] at index 1
numbers.insert(1, [2, 3])

# check the modification
print(numbers)
# [4, [2, 3], 5, 10, 16]

# list of numbers
numbers = [1, 2, 3, 4]

# add an integer to the end of the list
numbers.append(5)

print(numbers)
# [1, 2, 3, 4, 5]

# add a list to the end of the list
numbers.append([6, 7])

print(numbers)
# [1, 2, 3, 4, 5, [6, 7]]

# sorted function - returns a sorted list
numbers = [3, 7, 1, 5, 4]
numbers_sorted = sorted(numbers)

# numbers is not modified
print(numbers)
# [3, 7, 1, 5, 4]

# sorted function returns a sorted list
print(numbers_sorted)
# [1, 3, 4, 5, 7]


# sort method - modifies the list in-place and returns None
letters = ['c', 'b', 'd', 'a']
letters_sorted = letters.sort()

# letters is modified
print(letters)
# ['a', 'b', 'c', 'd']

# sort method returns None
print(letters_sorted)
# None


numbers = [2, 8, 3, 1, 9]

numbers_ascending = sorted(numbers)
print(numbers_ascending)
# [1, 2, 3, 8, 9]

numbers_descending = sorted(numbers, reverse=True)
print(numbers_descending)
# [9, 8, 3, 2, 1]

cities = ['Munich', 'Rome', 'Barcelona', 'Paris']

# Sort strings by length ascending order
cities_sorted = sorted(cities, key=len)
print(cities_sorted)
# ['Rome', 'Paris', 'Munich', 'Barcelona']

# Sort strings by length descending order
cities_sorted_r = sorted(cities, key=len, reverse=True)
print(cities_sorted_r)
# ['Barcelona', 'Munich', 'Paris', 'Rome']

# function defined with def
def num_vowel(x):
    cnt = 0
    for char in x.lower():
        if char in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    return cnt


names = ['Paula', 'Amanda', 'Ana', 'Amaranta', 'Li']

names_sorted = sorted(names, key=num_vowel)

print(names_sorted)
# ['Li', 'Ana', 'Paula', 'Amanda', 'Amaranta']


# sort nested list by the third value
# list of lists [item,price,quantity]

shop_list = [['table', 150, 2], ['chair', 50, 4], ['carpet', 100, 1], ['painting', 200, 7]]

shop_list_sorted = sorted(shop_list, key=lambda x: x[2])
print(shop_list_sorted)
# [['carpet', 100, 1], ['table', 150, 2], ['chair', 50, 4], ['painting', 200, 7]]

# list of products
products = ['table', 'chair', 'lamp', 'closet', 'bed']

# reversed list
products_reversed = list(reversed(products))

print(products_reversed)
# ['bed', 'closet', 'lamp', 'chair', 'table']

# list of products
products = ['table', 'chair', 'lamp', 'closet', 'bed']

# the list.reverse() method reverses the list in-place returning None
print(products.reverse())
# None

print(products)
# ['bed', 'closet', 'lamp', 'chair', 'table']


# list of products 1
products_1 = ['table', 'chair', 'lamp']

# list of products 2
products_2 = ['closet', 'bed']

# list concatenation using + operator
products_total = products_1 + products_2
print(products_total)
# ['table', 'chair', 'lamp', 'closet', 'bed']

# we can also concatenate strings and tuples using + operator
print('Amanda ' + 'Iglesias')
# Amanda Iglesias

print(('table', 'chair', 'lamp') + ('closet', 'bed'))
# ('table', 'chair', 'lamp', 'closet', 'bed')

# list of products 1
products_1 = ['table', 'chair', 'lamp']

# list of products 2
products_2 = ['closet', 'bed']

# list of products 3
products_3 = ['shelf', 'computer']

# list concatenation (3 lists) using + operator
products_total = products_1 + products_2 + products_3
print(products_total)
# ['table', 'chair', 'lamp', 'closet', 'bed', 'shelf', 'computer']

# list of products 1
products_1 = ['table', 'chair', 'lamp']

# list of products 2
products_2 = ['closet', 'bed']

# list concatenation using list.extend() method
returned = products_1.extend(products_2)

# list products_1 is modified in-place
print(products_1)
# ['table', 'chair', 'lamp', 'closet', 'bed']

# list products_2 remains unchanged
print(products_2)
# ['closet', 'bed']

# the list.extend() method returns None
print(returned)
# None

# list of numbers
numbers = [1, 2, 3, 4, 5]

# membership operators
# check if the number 1 exists in the list
1 in numbers
# True

# check if the number 6 exists in the list
6 in numbers
# False

# check if the number 2 does not exists in the list
2 not in numbers
# False

# check if the number 7 does not exists in the list
7 not in numbers
# True

# membership operators - in / not in

# strings
'a' in 'Amanda'
# True

# dictionaries
'table' in {'table': 120, 'chair': 40, 'lamp': 14, 'bed': 250, 'mattress': 100}
# True

# tuples
3 not in (1, 2)
# True

# sets
'Valencia' not in {'Barcelona', 'Valencia', 'Madrid'}
# False


### list of strings ###
# a list with products
products = ['table', 'lamp', 'chair', 'shelf', 'closet', 'bed']

# create a shallow copy of the list
products_2 = products.copy()

# modify an element of the new list
products_2[0] = 'computer'

# the modification in products_2 is not observed in products since 'computer' is a string (primitive type)
print(products)
# ['table', 'lamp', 'chair', 'shelf', 'closet', 'bed']

print(products_2)
# ['computer', 'lamp', 'chair', 'shelf', 'closet', 'bed']


### nested list ###
# nested list with products and prices
products_prices = [['table', 40], ['lamp', 15], ['chair', 25], ['shelf', 35], ['closet', 150], ['bed', 250]]

# create a shallow copy of the nested list
products_prices_2 = products_prices.copy()

# modify the price of a table in the shallow copy
products_prices_2[0][1] = 35

# the modification in products_prices_2 is observed in products_prices
# since the list containing the product and the price is referenced and not duplicated
print(products_prices)
# [['table', 35], ['lamp', 15], ['chair', 25], ['shelf', 35], ['closet', 150], ['bed', 250]]

import copy

# nested list with products and prices
products_prices = [['table', 40], ['lamp', 15], ['chair', 25], ['shelf', 35], ['closet', 150], ['bed', 250]]

# create a deep copy
products_prices_2 = copy.deepcopy(products_prices)

# modify the price of a table
products_prices_2[0][1] = 35

# the modification in products_prices_2 is NOT observed in products_prices
# since we are working with a deep copy
print(products_prices)
# [['table', 40], ['lamp', 15], ['chair', 25], ['shelf', 35], ['closet', 150], ['bed', 250]]

print(products_prices_2)
# [['table', 35], ['lamp', 15], ['chair', 25], ['shelf', 35], ['closet', 150], ['bed', 250]]

# a list with products
products = ['table', 'lamp', 'chair', 'shelf', 'closet', 'bed']

# copy the list using the = operator
products_2 = products

# modify products_2
products_2[0] = 'computer'

# the modification is reflected in products
print(products)
# ['computer', 'lamp', 'chair', 'shelf', 'closet', 'bed']

# a list with products
products = ['table', 'lamp', 'chair', 'shelf', 'closet', 'bed']

# number of products
len(products)
# 6

# list of cities
cities = ['valencia', 'barcelona', 'madrid']

# new empty list
cities_capitalized = []

# we loop through the list (cities) and we append the capitalized word to the new list (cities_capitalized)
for city in cities:
    cities_capitalized.append(city.capitalize())

print(cities_capitalized)
# ['Valencia', 'Barcelona', 'Madrid']

# list of cities
cities = ['valencia', 'barcelona', 'madrid']

# new list with capitalized names
cities_capitalized = [city.capitalize() for city in cities]

print(cities_capitalized)
# ['Valencia', 'Barcelona', 'Madrid']

# list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# filter out odd numbers from the list
numbers_even = [number for number in numbers if number % 2 == 0]

print(numbers_even)
# [2, 4, 6]