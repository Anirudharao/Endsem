"""
str1 = "3x + 2y + 4z"
str2 = "2x + 4y + 3z"

l1 = str1.split(' ')
l2 = str2.split(' ')

x1 = int(l1[0][:-1])
x2 = int(l2[0][:-1])

y1 = int(l1[2][:-1])
y2 = int(l2[2][:-1])
z1 = int(l1[4][:-1])
z2 = int(l2[4][:-1])
print(x1, y1, z1, x2, y2, z2)


if l1[1] == '+':
    #print(x1+x2)
    print(str(x1+x2)+"x + ",str(y1+y2)+"y + ",str(z1+z2)+"z")

a = 100
print(int('1000', 2))


word = ""
s = "separated by space"
print(word.join(s))


def mainfunction():
    msg = "main"

    def nestedfunction():
        msg = "nested"
        print(msg)

    nestedfunction()
    print(msg)

mainfunction()
"""

f = lambda a,b,c: a+b+c
print(f(2, 3, 1))