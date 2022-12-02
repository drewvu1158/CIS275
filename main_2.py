import random


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
        self._items[index] = new_item



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
      bottom_item = self._heap[self._size - 1]

      self._heap[0] = bottom_item

      last_valid_index = self._size - 2

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


class plane:
    """Represents a plane"""
    @classmethod
    def generate_plane(cls, current_time, probability_of_arrval, fuel_level = random.randint(5,15)):
        """ Generates a plane with a random fuel level and arrival time """
        if random.random() < probability_of_arrval:
            return plane(current_time)
        else:
            return None
        
    def __init__(self, arrival_time, transaction_time = random.randint(1,3)):
        self._arrival_time = arrival_time
        self._transaction_time = transaction_time
    
    @property
    def arrival_time(self):
        return self._arrival_time
    
    @property
    def transaction_time(self):
        return self._transaction_time


    def serve(self):
        self._transaction_time -= 1

class cashier:
    def __init__(self):
        self.planes_serverd_takeoff = 0
        self.planes_serverd_landing = 0
        self.longest_wait_time_to_takeoff = 0
        self.longest_wait_time_to_land = 0
        self.avg_wait_time_to_takeoff = 0
        self.avg_wait_time_to_land = 0
        self.current_plane_queue = None
        self.current_priority_queue = MinHeap() #make a minheap sort
        self.current_regular_queue = LinkedQueue()
        self.plane_crashed = 0

    def add_landing_plane(self, current_time, fuel_level):
        """Sort using minheap"""
        if plane.fuel_level < current_time:
            self.plane_crashed += 1
        else:
            self.current_priority_queue.add(plane)

    def add_takeoff_plane(self):
        self.current_regular_queue.add(plane)

    def serve_plane(self, current_time):
        if self.current_plane_queue is None:
            if self.current_priority_queue.is_empty():
                if self.current_regular_queue.is_empty():
                    return
        elif self.current.plane_queue is None:
            #serve priority queue
            if self.current_plane_queue.is_empty():
                if self.current_priority_queue.is_empty() == False:
                    self.current_plane_queue = self.current_priority_queue.pop()
                    self.current_plane_queue.serve()
                    self.planes_serverd_landing += 1
                    if self.current_plane_queue.arrival_time > self.longest_wait_time_to_land:
                        self.longest_wait_time_to_land = self.current_plane_queue.arrival_time
                    self.avg_wait_time_to_land += current_time - self.current_plane_queue.arrival_time

                        
        elif self.current_plane_queue is None:
            #serve regular queue
            if self.current_priority_queue.is_empty() == False:
                self.current_plane_queue = self.current_priority_queue.pop()
                time_waited = current_time - self.current_plane_queue._arrival_time
                if time_waited > self.longest_wait_time:
                    self.longest_wait_time = time_waited
                self.total_customer_wait_time += time_waited
                self.current_plane_queue.serve()
                if self.current_plane_queue._transaction_time == 0:
                    self.current_plane_queue = None
                    self.planes_serverd_takeoff += 1


    def print_statistics(self):
        print("What is the average time spent waiting for takeoff? {}".format(self.avg_wait_time_to_takeoff/self.planes_serverd_takeoff))
        print("What is the average time spent waiting for landing? {}".format(self.avg_wait_time_to_land/self.planes_serverd_landing))
        print("What is the longest time spent waiting for takeoff? {}".format(self.longest_wait_time_to_takeoff))
        print("What is the longest time spent waiting for landing? {}".format(self.longest_wait_time_to_land))
        print("Did a plane crash? {}".format(self.plane_crashed))
        print("How many planes total took of and landed {}".format(self.planes_serverd_landing + self.planes_serverd_takeoff))




class air_traffic_control:
    def __init__(self, length_of_simulation, probability_of_arrival, prob_of_depart):
        self._length_of_simulation = length_of_simulation
        self._probability_of_arrival = probability_of_arrival
        self._prob_of_depart = prob_of_depart
        self.cashier = cashier()


    def _run_simulation(self):
        for current_time in range(self._length_of_simulation):
            new_arrival = plane.generate_plane(current_time, self._probability_of_arrival)
            new_arrival_landing = plane.generate_plane(current_time, self._prob_of_depart)
            if new_arrival is not None:
                self.cashier.add_takeoff_plane()
            if new_arrival_landing is not None:
                self.cashier.add_landing_plane(current_time, new_arrival_landing.fuel_level)
            
            self.cashier.serve_plane(current_time)

        self.cashier.print_statistics()

    
def main():
    
    num_arrivals = float(input("What is the chance a Plane will arrive? "))
    num_departures = float(input("What is the chance a Plane will show up and depart? "))
    num_of_simulations = int(input("How many simulations would you like to run? "))

    atc = air_traffic_control(num_of_simulations, num_arrivals, num_departures)
    atc._run_simulation()

main()