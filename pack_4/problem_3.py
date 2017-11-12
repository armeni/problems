import random
from random import randint

class Animal:
    pass

class Fish(Animal):
    def __str__(self):
        return 'F'

class Bear(Animal):
    def __init__(self):
        self.without_food = 0

    def __str__(self):
        return 'B'

class River:
    def __init__(self, l, dead):
        self.fish = 0
        self.bears = 0
        self.l = l
        self.dead = dead
        self.cells = []        
        self.animals()

    def animals(self):
        for i in range(0, self.l):
            rand = randint(0, 2)
            if rand == 0:
                self.cells.append(None)
            elif rand == 1:
                self.bears += 1
                self.cells.append(Bear())
            else:
                self.fish += 1
                self.cells.append(Fish())

    def rand(self, animal):
        if self.none() > 0:
            choices = [i for i, x in enumerate(self.cells) if x is None]
            index = random.choice(choices)
            self.cells[index] = animal

    def none(self):
        return self.cells.count(None)

    def check(self, i, m):
        if self.cells[i].without_food == self.dead - 1:
            self.cells[i] = None
        else:
            self.cells[i + m] = self.cells[i]
            self.cells[i + m].without_food += 1
            self.cells[i] = None

    def upd_cell(self, i):
        if self.cells[i] is not None:
            m = randint(-1, 1)
            if m != 0 and 0 <= i + m < self.l:
                if self.cells[i + m] is None:
                    if type(self.cells[i]) == Bear:
                        self.check(i, m)
                    else:
                        self.cells[i + m] = self.cells[i]
                        self.cells[i] = None
                elif type(self.cells[i]) == type(self.cells[i + m]):
                    if type(self.cells[i]) == Bear:
                        self.check(i, 0)
                        self.check(i + m, 0)
                        self.rand(Bear())
                        self.bears += 1
                    else:
                        self.rand(Fish())
                        self.fish += 1
                else:
                    if type(self.cells[i]) == Bear:
                        self.cells[i + m] = self.cells[i]
                        self.cells[i + m].without_food=0
                        self.cells[i] = None
                        self.fish -= 1

    def __str__(self):
        s = ''
        for i in range(0, self.l):
            if self.cells[i] is None:
                s += '_'
            else:
                s += self.cells[i].__str__()
        return s

    def upd(self):
        for i in range(0, self.l):
            self.upd_cell(i)
        print(self.__str__())

s = input('Введите длину реки и сколько шагов медведь может жить без еды: ').split()
river = River(int(s[0]), int(s[1]))
print('Начальное состояние экосистемы: ', river.__str__())
iter=int(input('Введите количество итераций: '))
for i in range(0, iter):
    print('Состояние экосистемы после',i+1,'шага: ')
    river.upd()
