class _Node:
    def __init__(self, _element, _sitename, _previous, _next):
        self._element =_element
        self._sitename =_sitename
        self._previous =_previous
        self._next =_next

class dlb:
    def __init__ (self):
        self._head = _Node(0, None, None, None)
        self._t = _Node(100000, None, None, None)
        self._head._next = self._t
        self._t._previous = self._head
        self._size = 0

    def size(self):
        return self._size == 0

    def _insert(self, e, a, p, s):
        new = _Node(e, a, p, s) 
        p._next = new
        s._previous = new
        self._size += 1
        return new
    
    def _delete(self, node):
        p = node._previous
        s = node._next
        p._next = s
        s._previous = p
        self._size -= 1
        node._previous = node._next = node._element = None
       
    def _find(self, name):
        x = self._head
        while(x != self._t):
            if x._sitename == name:
                return x
            x = x._next
        return False
            
class DoublyLinkedList(dlb):
    def from_site(self, a):
        s = self._find(a)
        if s == False:
            return self._insert(1, a, self._head, self._head._next)       
        x = s
        c = s._element
        while(x != self._t):
            if c + 1 <= x._next._element:
                self._insert(c + 1, a, x, x._next)
                return self._delete(s)
            x = x._next
        return self._insert(c + 1, a, self._t._previous, self._t)
    
    def from_client(self, c):
        if not self.size():
            x = self._t._previous  
            i = 1
            print('Топ', c, 'сайтов: ')
            while x != self._head and i <= c:
                print(str(i) + '.', x._sitename)
                i += 1
                x = x._previous

s = DoublyLinkedList()

def main():
        print('Введите количество запросов: ')
        n = int(input())
        print('Введите адреса сайтов: ')
        for i in range(n):  
            k = str(input())
            s.from_site(k)
		
        print('Введите k (Top k): ')
        k = int(input())
        s.from_client(k)

main()
