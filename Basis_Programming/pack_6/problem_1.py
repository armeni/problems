import DLB

class DoublyLinkedCircularList(DLB.DoublyLinkedBase):
    def __init__(self):
        self._header=DLB._Node(None,None,None)
        self._header._prev=self._header
        self._header._next=self._header
        self._size=0

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._header._prev, self._header)

    def delete_first(self):
        if self.is_empty():
            raise DLB.Empty('List is empty')
        else:
            self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise DLB.Empty('List is empty')
        else:
            self._delete_node(self._header._prev)

    def __str__(self):
        s = '['
        if self._size != 0:
            a = self._header._next
            s += str(a._element)
            while a._next._element != None:
                a = a._next
                s += ' ' + str(a._element)
        s+=']'
        return s

c = DoublyLinkedCircularList()
c.insert_first('WINTER IS COMING!')
c.delete_first() 
c.insert_first('WINTER IS HERE!')
c.insert_last('SESSIA IS COMING!')
c.delete_last() 
c.insert_last('SESSIA IS HERE!')

x = c._header._next 
print('Example (3 раза): ')
count = 0      
 
while count < 3:
	if x._element != None:
		print(x._element)
	x = x._next
	if x._element == None:
		count += 1
        
print('List: ', c)
