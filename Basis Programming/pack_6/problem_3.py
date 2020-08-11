import DLB

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

l = DLB.PositionalList()
print('Введите последовательность чисел: ')
s = input().split()
for i in s:
    l.add_last(int(i))
print('Введите число v: ')
v = int(input())
    
def search(v):
    i = l._header._next
    j = l._trailer._prev
    while j != i:
        if i._element + j._element == v:
            return Pair(i._element, j._element)
        if i._element + j._element > v:
            j = j._prev
        if i._element + j._element < v:
            i = i._next
    return None

n = search(v)

if n == None:
    print(n)
else:
    print(n.first, n.second)
