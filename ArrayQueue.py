from array_1 import Array
from abstractcollection import AbstractCollection


class ArrayQueue(AbstractCollection):
    def __init__(self, source_collection=None):
        self._front = 0
        self._rear = 0
        self._items = Array(10)
        AbstractCollection.__init__(self, source_collection)

    def ensure_capacity(self):
        new = Array(len(self._items) * 2)
        for i in range(len(self)):
            new[i] = self._items[self._front]
            self._front = (self._front + 1) % len(self._items)
        
        self._rear = len(self)
        self._items = new
        self._front = 0
        

    def add(self, item):
        if self._size == len(self._items):
            self.ensure_capacity()
        
        
        self._items[self._rear] = item
        self._rear = (self._rear + 1) % len(self._items)
        self._size += 1

    def clear(self):
        self._size = 0
        self._front = 0
        self._rear = 0
        for i in range(len(self._items)):
            self._items[i] = None

    def peek(self):
        if self.is_empty():
            raise KeyError("The queue is empty")
        else:
            return self._items[self._front]

    def pop(self):
        if self.is_empty():
            raise KeyError("The queue is empty")
        print("Popping: ", self._items[self._front])
        
        self._items[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % len(self._items)
        return self._items[self._front]

    def print_queue(self):
        print(self._items)


arrq = ArrayQueue()
arrq.add(1)
arrq.add(2)
arrq.add(3)
arrq.add(4)
arrq.add(5)
arrq.add(6)
arrq.add(7)
arrq.add(8)
arrq.add(9)
arrq.print_queue()
print(arrq.peek())
arrq.add(10)
print(arrq.peek())
arrq.print_queue()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.add(11)
arrq.pop()
print(arrq.peek())
arrq.print_queue()
arrq.pop()
arrq.print_queue()

arrq.clear()
arrq.add(1)
arrq.add(2)
arrq.add(3)
arrq.add(4)
arrq.add(5)
arrq.add(6)
arrq.add(7)
arrq.add(8)
arrq.add(9)
arrq.add(10)

arrq.print_queue()

arrq.add(11)
arrq.add(12)
arrq.add(13)

arrq.print_queue()
print(len(arrq))
arrq.add(14)
arrq.add(15)
arrq.add(16)
arrq.add(17)
arrq.add(18)
arrq.add(19)
arrq.add(20)
arrq.print_queue()
arrq.pop()
arrq.print_queue()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.pop()
arrq.print_queue()
arrq.pop()
arrq.add(21)
arrq.print_queue()
arrq.pop()
arrq.print_queue()
