c=list(input("Введите числа: ").split())
s=int(input("Введите сдвиг: "))
while s>0:
    c.insert(0, c.pop())
    s-=1
print("После сдвига: ", *c)