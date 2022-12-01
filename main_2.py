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

class Node:
    """ Represents a singly linked node """

    def __init__(self, data, next=None):
        """ By default, this Node will not link to another Node """
        self._data = data
        self._next = next


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
    def generate_plane(cls, current_time, probability_of_arrval):
        """ Generates a plane with a random fuel level and arrival time """
        if random.random() < probability_of_arrval:
            return plane(current_time, random.randint(1,3))
        else:
            return None
        
    def __init__(self, arrival_time, fuel_level, transaction_time):
        self._arrival_time = arrival_time
        self._fuel_level = fuel_level
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
        self.current_priority_queue = LinkedQueue()
        self.current_regular_queue = LinkedQueue()
        self.plane_crashed = 0

    def add_landing_plane(self, current_time,fuel_level):
        if plane.fuel_level < current_time:
            self.plane_crashed += 1
        else:
            if plane.fuel_level < 3:
                self.current_priority_queue.add(plane)

    def add_takeoff_plane(self):
        self.current_plane_queue.add(plane)

    def serve_plane(self, current_time):
        if self.current_plane_queue is None:
            if self.current_priority_queue.is_empty():
                if self.current_regular_queue.is_empty():
                    return
        elif self.current.plane_queue is None:
            #serve priority queue
            if self.current_plane_queue.is_empty():
                if self.current_priority_queue.is_empty() == False:
                    self.current_plane_queue = self.current_regular_queue.pop()
                    time_waited = current_time - self.current_plane_queue._arrival_time
                    if time_waited > self.longest_wait_time_to_land:
                        self.longest_wait_time_to_land = time_waited
                    self.avg_wait_time_to_land += time_waited
                    self.current_plane_quque.serve()
                    if self.current_plane_queue._transaction_time == 0:
                        self.current_plane_queue = None
                        self.planes_serverd_landing += 1

                        
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
    def __init__(self, length_of_simulation, probability_of_arrival):
        self._length_of_simulation = length_of_simulation
        self._probability_of_arrival = probability_of_arrival
        self.cashier = cashier()


    def _run_simulation(self):
        for current_time in range(self._length_of_simulation):
            new_arrival = plane.generate_plane(current_time, self._probability_of_arrival)

            if new_arrival is not None:
                self.cashier.add

def main():
    
    num_arrivals = int(input("What is the chance a Plane will arrive? "))
    num_departures = int(input("What is the chance a Plane will show up and depart? "))
    num_of_simulations = int(input("How many simulations would you like to run? "))

    atc = air_traffic_control(num_of_simulations, num_arrivals, num_departures)

main()