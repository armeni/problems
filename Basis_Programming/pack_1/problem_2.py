def dividers(n):
    lst = list(range(1,n+1))
    div = []

    for num in lst:
        if n % num == 0:
            div.append(num)
    return div

if (__name__=="main"):
    n = int(input("Введите число: "))
    print(dividers(n))