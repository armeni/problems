import math

class Circle():
    def __init__(self, r):
        self.r = r

    def S(self):
        return self.r**2*math.pi

    def P(self):
        return 2*self.r*math.pi

class Rectangle():
    def __init__(self, l, w):
        self.l=l
        self.w=w

    def S(self):
        return self.l*self.w

r=int(input('Введите радиус окружности: '))
print('Площадь окружности: ', Circle(r).S())
print('Длина окружности: ', Circle(r).P())
l,w=map(int,input('Введите длину и ширину прямогольника: ').split())
print('Площадь прямоугольника: ', Rectangle(l,w).S())