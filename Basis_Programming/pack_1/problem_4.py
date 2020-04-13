w = str(input("Введите слово: "))
x = len(w)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if w[x - i] == w[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("Не полиндром")
else:
  print("Полиндром")