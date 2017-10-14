def arithmetic (a, b, с):
    res="Неизвестная операция!"
    if с == '+':
        res=a+b
    elif с == '-':
        res=a-b
    elif с == '*':
        res=a*b
    elif с == '/' and b!=0:
        res=a/b
    elif с == '/' and b==0:
        res="Деление на ноль невозможно!"
    return res

a,b,c=input("Введите числа и знак операции: ").split()
print(arithmetic(int(a), int(b), c))