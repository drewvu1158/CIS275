import random
from data_structs import *
class Plane:
    @classmethod
    def generate_plane(cls, probability_of_arrival, current_time):
        if random.random() < probability_of_arrival:
            return Plane(current_time, random.randint(1,3), random.randint(5,15))
        else:
            return None
    
    def __init__(self, arrival_time, transaction_time, plane_fuel):
        self.arrival_time = arrival_time
        self.transaction_time = transaction_time
        self.plane_fuel = plane_fuel

    @property
    def arrival_time(self):
        return self.arrival_time

    @property
    def transaction_time(self):
        return self.transaction_time

    def serve(self):
        self.transaction_time -= 1

    def __lt__(self, other):
        return self.plane_fuel < other.plane_fuel


    def __le__(self, other):
        return self.plane_fuel <= other.plane_fuel


    def __eq__(self, other):
        return self.plane_fuel == other.plane_fuel
    
    def __gt__(self, other):
        return self.plane_fuel > other.plane_fuel

    def __ge__(self, other):
        return self.plane_fuel >= other.plane_fuel



class runway:
    def __init__(self):
        self.average_time_takeoff = 0
        self.average_time_landing = 0
        self.longest_wait_takeoff = 0
        self.longest_wait_landing = 0
        self.landing_queue = MinHeap()
        self.takeoff_queue = LinkedQueue()
        self.did_crash = False
        self.current_plane = None
        self.planes_total = 0

    def add_plane_landing(self, p):
        self.landing_queue.add(p)

    def add_plane_takeoff(self, p):
        self.takeoff_queue.add(p)

    def serve_plane(self, current_time):
        if self.landing_queue.is_empty() and self.takeoff_queue.is_empty():
            return
        elif self.landing_queue.is_empty() and self.takeoff_queue.is_empty() == False:
            self.current_plane = self.takeoff_queue.pop()
            time_waited = current_time - self.current_plane.arrival_time
            self.average_time_takeoff = (self.average_time_takeoff + time_waited) / 2
            if time_waited > self.longest_wait_takeoff:
                self.longest_wait_takeoff = time_waited
        else:
            self.current_plane = self.landing_queue.pop()
            time_waited = current_time - self.current_plane.arrival_time
            self.average_time_landing = (self.average_time_landing + time_waited) / 2
            if time_waited > self.longest_wait_landing:
                self.longest_wait_landing = time_waited
        
        self.current_plane.serve()
        if self.current_plane.transaction_time == 0:
            self.current_plane = None
            self.planes_total += 1

    
    def print_stats(self):
        print("Average Time Landing: " + str(self.average_time_landing))
        print("Average Time Takeoff: " + str(self.average_time_takeoff))
        print("Longest Wait Landing: " + str(self.longest_wait_landing))
        print("Longest Wait Takeoff: " + str(self.longest_wait_takeoff))
        print("Total Planes: " + str(self.planes_total))


class ATC:

    def __init__(self, lenth, odds_of_new_plane, odds_of_takeoff):
        self.sim_lenth = lenth
        self.odds_of_new_plane = odds_of_new_plane
        self.odds_of_takeoff = odds_of_takeoff
        self.runway = runway()

    def run_simulation(self):
        for cur_time in range(self.sim_lenth):
            new_arrival = Plane.generate_plane(self.odds_of_new_plane, cur_time)
            new_takeoff = Plane.generate_plane(self.odds_of_takeoff, cur_time)

            if new_arrival is not None:
                self.runway.add_plane_landing(new_arrival)
            if new_takeoff is not None:
                self.runway.add_plane_takeoff(new_takeoff)
            self.runway.serve_plane(cur_time)

        self.runway.print_stats()
    
def main():

    num_arrivals = 25
    num_departures = 25
    num_of_simulations = 25

    p = ATC(num_of_simulations, num_arrivals, num_departures)
    p.run_simulation()

main()