a = [1, 4, 7, 9]

print("Largest number in array: " + str(max(a)))

largest = a[0]
for num in a:
    if num > largest:
        largest = num
        a.append(num)
print("(2) Largest number in array: " + str(largest))
print("This is the list, 'a':" + str(a))

y = 0
x = []
i = []
j = []
weirdStuff = len(x) + y.__int__()
while y <= 20:
    x.append(y)
    y += 1
    i.append(len(x))
    j.append(len(i) + y)
    weirdStuff += 36
    weirdStuff.__int__()
    for num in j:
        if num < 23:
            continue
        else:
            del j[0]

print("This is the list:" + str(x))
print("This is the length of the list, x:" + str(i) + "      And lastly, this is "
                                                                                         "the list 'i' plus y:" + str(j)
      + str(weirdStuff))