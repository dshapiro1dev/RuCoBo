# numbers in python can take different forms
# integers:  round numbers like  1, 12, -5
# floats:    numbers with decimals like 3.553 , 1.0505,  3.1415, and 5.000000
integer1 = 37
integer2 = 12

divd = integer1 / integer2

print(type(integer1))  # integer
print(type(integer2))  # integer
print(type(divd))      # float
# notice: if we divide one integer by another - and dont get a clean integer, the result is a float

i1 = 6
i2 = 3
print(type(i1/i2))  # even if the result is an integer - python automatically says a division of 2 integers gets a float

# we can also convert from one type to another
# lets say we have a string - and we want an integer
mystr = "37"
theint = int(mystr)  # int() converts the string into an integer
print(theint)

# now what happens if we try convert a float to an int
myflt = 3.1415926
myint = int(myflt)
print(myint)  # 3  -> we drop the decimal and converted to an integer (close enough to PI)

# all the arithmetic operations are natural - but Python has some specific charaters
f1 = 2.17
f2 = 3.22
f3 = -333.33

print(f1+f2)  # addition
print(f1-f2)  # subtraction
print(f1==f2) # equivalence test (note: the double ==  tests if 2 things are equal, the single = assigns a value)
print(f1/f2)  # division
print(f1*f2)  # multiplication
print(f1 ** f2) # f1 to the power of f2
print(abs(f3))  # absolute value

# for the mathematically inclined - python even has complex numbers
c1 = complex(2,3)  # 2 + 3i    2 = real part    3 = imaginary part
print(c1)  # prints out:  2 + 3j