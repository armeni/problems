import math

class Figure:
    def S(self):
        pass

    def P(self):
        pass

class Circle(Figure):
    def __init__(self,r):
        self.r = r
    def S(self):
        return self.r**2*math.pi
    def P(self):
        return 2*self.r*math.pi

class Rectangle(Figure):
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def S(self):
        return self.l*self.w

str = str(input('Введите название фигуры (круг или прямоугольник): '))
if str == 'Круг' or str == 'круг':
	r = float(input('Введите радиус окружности: '))
	print('Площадь окружности: ', Circle(r).S())
	print('Длина окружности: ', Circle(r).P())
elif str == 'Прямоугольник' or str == 'прямоугольник':
	l, w = map(float,input('Введите длину и ширину прямогольника: ').split())
	print('Площадь прямоугольника: ', Rectangle(l,w).S())
else:
	print('Ошибка ввода')
