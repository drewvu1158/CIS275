

class AbstractCollection:

    def __init__(self, source_collection=None):
        self._numitems = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    def __add__(self, other):
        """ Overloads the + operator. Returns a new Collection containing the contents of self and other """
        result = type(self)(self)
        for item in other:
            result.add(item)

        return result

    def is_empty(self):
        """ Returns True if len(self) == 0, False otherwise """
        return len(self) == 0

    def __len__(self):
        """ Returns the number of items in self """
        return self._numitems

    def count(self, item):
        """ Returns the number of times 'item' exists in self """
        result = 0
        for i in self:
            if i == item:
                result += 1

        return result

class Array:

    def __init__(self, capacity, fill_value=None):
        """ Capacity is the static size of the array
            Each index in the array is filled with fill_value """
        self._items = []
        for count in range(capacity):
            self._items.append(fill_value)

    def __len__(self):
        """ Returns the length of this array """
        return len(self._items)

    def __str__(self):
        """ Returns a string representation of this array """
        return str(self._items)

    def __iter__(self):
        """ Supports iteration with a for loop """
        return iter(self._items)

    def __getitem__(self, index):
        """ Retrieves the item at 'index' """
        return self._items[index]

    def __setitem__(self, index, new_item):
        """ Sets the internal list's index to 'new_item' """
        print(index)
        # self._items[index] = new_item
        self._items.append(new_item)


class Node:
    """ Represents a singly linked node """

    def __init__(self, data, next=None):
        """ By default, this Node will not link to another Node """
        self._data = data
        self._next = next


class MinHeap(AbstractCollection):
   """ An array-based min-heap implementation """

   DEFAULT_CAPACITY = 10

   def __init__(self):
      self._heap = Array(MinHeap.DEFAULT_CAPACITY)
      AbstractCollection.__init__(self)

   def peek(self):
      """ Return the value at the root """
      if self.is_empty():
         raise IndexError("Heap is empty!")
      return self._heap[0]

   def add(self, item):
      """ Adds 'item' to the MinHeap, finding its correct location """

      # Begin by placing the new item in the first empty index
      self._heap[len(self)] = item
      cur_index = len(self)

      while cur_index > 0:
         # Find the parent of the current index of the new item
         parent_index = (cur_index - 1) // 2
         parent_item = self._heap[parent_index]
         if parent_item <= item:
            # Parent is less than the new item (or equal): new item is in correct index
            break
         # Swap the parent and the child
         self._heap[cur_index] = parent_item
         self._heap[parent_index] = item
         cur_index = parent_index

      self._numitems += 1

   def pop(self):
      """ Remove the item at the root and reheapify the remaining items """
      if self.is_empty():
         raise IndexError("Heap is empty!")
      top_item = self._heap[0]
      bottom_item = self._heap[self._numitems - 1]

      self._heap[0] = bottom_item

      last_valid_index = self._numitems - 2

      cur_index = 0

      # In a loop, move the original final leaf (now at the root) down to its correct location
      while True:
         left_child_index = 2 * cur_index + 1
         right_child_index = 2 * cur_index + 2
         if left_child_index > last_valid_index:
            # We have no left child, therefore we have no right child. We're done
            break

         if right_child_index > last_valid_index:
            # We just have a left child, so it is the smallest
            min_child_index = left_child_index

         else:
            # We have two children, check to see which is smaller
            left_child = self._heap[left_child_index]
            right_child = self._heap[right_child_index]

            if left_child < right_child:
               min_child_index = left_child_index
            else:
               min_child_index = right_child_index

         min_child = self._heap[min_child_index]

         if bottom_item <= min_child:
            # Item being moved is less than both children. Stop here
            break

         # Item being moved is larger than its min child. Swap and continue
         self._heap[cur_index] = min_child
         self._heap[min_child_index] = bottom_item
         cur_index = min_child_index

      self._numitems -= 1
      return top_item

class LinkedQueue(AbstractCollection):

    """ A linked list-based queue implementation """
    def __init__(self):
        self._front = None
        self._rear = None
        AbstractCollection.__init__(self)

    def add(self, new_item):
        """ Add 'new_item' to the back of the queue """
        new_node = Node(new_item)
        if self.is_empty():
            """ No nodes in the linked list """
            self._front = new_node
            self._rear = new_node
        else:
            """ At least one node already in the linked list. Point the last node to it """
            self._rear._next = new_node
            self._rear = new_node
        self._numitems += 1

    def pop(self):
        """
        Precondition: Queue is not empty
        Postcondition: Queue has one less item in it
        Raises: ValueError if Queue is empty
        :return: The item previously at the front of the queue
        """
        if self.is_empty():
            raise ValueError("Queue is empty!")
        return_item = self._front._data
        self._front = self._front._next

        if self._front is None:
            """ Queue had only one item in it """
            self._rear = None

        self._numitems -= 1
        return return_item

    def clear(self):
        """ Makes self empty """
        self._front = None
        self._rear = None
        self._numitems = 0

    def peek(self):
        """ Returns the entry at the front of the Queue
        Precondition: Queue is not empty
        Raises: ValueError if the Queue is empty
        """
        if self.is_empty():
            raise ValueError("Queue is empty!")
        return self._front._data


    def __str__(self):
        """ For testing purposes only """
        return_string = "Front:"
        probe = self._front
        while probe is not None:
            return_string += " " + str(probe._data)
            probe = probe._next

        return_string += " :Back"
        return return_string
