A = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3]
B =[4, 5, 6, 7, 8, 9, 10, 9, 8, 11]


def fun():
    c = []
    d = []
    for i in A:
        if i in B:
            d.append(i)
            B.remove(i)
    for i in d:
        A.remove(i)
    c = A + B
    c = list(set(c))
    print(c)
    print(d)
fun()
a = 3 & 4
print(a)
y = 2
z = 1
a ={1:2}



try:
    f = open('ssssssssssss', 'r')
except:
    print('ffffffffffffffff')
else:
    print('ddddddd')

class A():
    def __init__(self):
        self.name = 'x'
        return
    def __str__(self):
        self.name = 'xx'

a = [9, 9, 9, 9]
print(a)
c =a.append(7)
print(c)
print(a)

try:
    open('fdsfds', 'r')
except:
    print('fsdfddddddddddddddddddd')