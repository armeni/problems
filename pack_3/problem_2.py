class converter(int):
    lst = (('M', 1000),('CM', 900),('D', 500),('CD', 400),('C', 100),('XC', 90),('L', 50),('XL', 40),('X', 10),('IX', 9),('V', 5),('IV', 4),('I',1))
    
    def roman2arab(self,s):
        res = 0
        i = 0
        for m, n in self.lst:
            while s[i:i + len(m)] == m:
                res += n
                i += len(m)
        return res  
	
    def arab2roman(self,s):
        res = ""
        for m, n in self.lst:
            while s>=n:
                res += m
                s -= n
        return res
    
convert=converter()
s=input('Введите число: ')
is_int=s.isnumeric()

if is_int:
    print('Это число римскими цифрами: ', convert.arab2roman(int(s)))
else:
    print('Это число арабскими цифрами: ', convert.roman2arab(s))
