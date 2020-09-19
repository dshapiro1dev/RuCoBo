f = open("../../../data/project1/ya.encrypted", "r")
for x in f:
    x = x.replace('1','a')
    x = x.replace('5','e')
    x = x.replace('8','h')
    x = x.replace('9','i')
    x = x.replace('!','r')
    x = x.replace('@','s')
    x = x.replace('#','t')
    x = x.replace('&','v')
    x = x.replace('^','w')
    x = x.replace('`','y')

    print(x,end='')

print()
print()
print("that was underwhelming")