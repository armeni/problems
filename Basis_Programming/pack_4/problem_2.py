a = str(input("Введите полином (например, 3x^2+4x+1): ")) 

def sympy_the_best():
    global k
    c = ''
    while k < len(a) and not (a[k] == "+" or a[k] == "-" or a[k] == "x"):
        c += a[k]
        k += 1
    if not c == '': 
        return int(c)
    else:
        return 1
	
p, s1, s2 = [], [], []
k = 0; b = 0

if a[0] == '-':
    s2.append("-")
    k += 1
else:
    s2.append("+")

while k < len(a):
    c = sympy_the_best()
    if k < len(a) and a[k] == 'x':
        if k + 1 < len(a) and a[k + 1] == '^':
            k += 2
            d = sympy_the_best()
            s1.append(d - 1)
            p.append(c * d)
        else:
            s1.append(0)
            p.append(c)
    else:
       s1.append(-1)
       p.append(-1)
    b = k + 1
    if  k < len(a) and (a[k] == "-" or a[k] == "+"):
       s2.append(a[k])
    k += 1

print("Его первая производная: ") 	
for i in range(len(p)):
    if not((i == 0) and s2[i] == "+"):  
        if not(p[i] == -1 and s1[i] == -1):
            print(s2[i], end = "")
    if p[i] > 0:
        print(p[i], end = "")
    if  s1[i] > 0:
        if s1[i] == 1:
            print("x", end = "")
        else:
            print("x^", end = "")
            print(s1[i], end = "")	
