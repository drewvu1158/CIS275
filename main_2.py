from class_atc import ATC
def main():

    num_arrivals = int(input("What is the chance a Plane will arrive? "))
    num_departures = int(input("What is the chance a Plane will show up and depart? "))
    num_of_simulations = int(input("How many simulations would you like to run? "))

    atc = ATC(num_arrivals, num_departures, num_of_simulations)
    atc.run_simulation()

    atc.runway.print_statistics()


main()





