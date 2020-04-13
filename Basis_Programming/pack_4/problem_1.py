def get_time(s):
    return int(s[0:2]) * 3600000 + int(s[3:5]) * 60000 + int(s[6:8]) * 1000 + int(s[9:12])

def time(t):
    h = t // 3600000 
    m = (t - h *3600000) // 60000
    s = (t - h *3600000 - m * 60000) // 1000
    ms = (t - h *3600000 - m * 60000 - s * 1000)
    return str(h) + ":" + str(m) + ":" + str(s) + ":" + str(ms)

class Cell():
    def __init__(self):
        self.s = list()
    def append(self, n):
        self.s.append(n)
    def pop(self):
        if len(self.s) > 0:
            self.s.pop(0)
    def f(self):
        if len(self.s) > 0:
            return self.s[0]
        else:
            return 0
    def l1(self):
        return len(self.s) == 0
    def l2(self):
        return len(self.s)

f = open("TRD2.csv", "r")
a = f.readline()
			
dic = {'V': None, 'D': None, 'X': None, 'Y': None, 'B': None, 'J': None, 'Q': None, 'Z': None, 'K': None, 'P': None, 'All': None}
max1 = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}
maxl = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}
l = 0	

for i in dic:
    dic[i] = Cell()
			
def input():
    a = f.readline()
    p = a.split(',')
    return p

def c():
    global l 
    f = False	
    while True:
        s = input()
        if(s[0] == ''):
            return 0
        if not f:
            l = get_time(s[0])
            f = True
        t1 = get_time(s[0]) - l
        t2 =  dic[s[3][0]].f()
        while t1 - t2 > 1000 and not dic[s[3][0]].l1():
            t2 =  dic[s[3][0]].f()
            dic[s[3][0]].pop()	
        dic[s[3][0]].append(t1)
        if max1[s[3][0]] < dic[s[3][0]].l2():		
            max1[s[3][0]] = dic[s[3][0]].l2()
            maxl[s[3][0]] = dic[s[3][0]].f()
        t2 =  dic['All'].f()	
        while t1 - t2 > 1000 and not dic['All'].l1():
            t2 =  dic['All'].f()
            dic['All'].pop()
        dic['All'].append(t1)
        if max1['All'] < dic['All'].l2():		
            max1['All'] = dic['All'].l2()
            maxl['All'] = dic['All'].f()

def out():
    for i in dic:
        print(i, "Max:", max1[i], "Time:", time(maxl[i] + l))
c()
out()
