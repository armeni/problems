class converter(int):
    def roman2arab(self,s):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ar = 0
        for i in range(len(s)):
            if i > 0 and rom[s[i]] > rom[s[i - 1]]:
                ar += rom[s[i]] - 2 * rom[s[i - 1]]
            else:
                ar += rom[s[i]]
        return ar

    def arab2roman(self,s):
        ar = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        rom = ''
        while s > 0:
            for i, r in ar:
                while s >= i:
                    rom += r
                    s -= i
        return rom

s=input('Введите число: ')
is_int=s.isnumeric()

if is_int:
    print('Это число римскими цифрами: ', converter().arab2roman(int(s)))
else:
    print('Это число арабскими цифрами: ', converter().roman2arab(s))
