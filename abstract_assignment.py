from abc import ABC, abstractmethod

# implement abstract class of Car
class Car(ABC):

    # print cost of car, based on user input
    def print_cost(self, cost):
        print('This vehicle costs {}.'.format(cost))

    # abstract method to calculate range of vehicle
    @abstractmethod
    # pass in energy capacity
    def range_calculation(self, capacity, mileage):
        pass


class Gasoline_Car(Car):

    # for gas car, capcity is gallons of gas
    # mileage is mpg
    def range_calculation(self, capacity, mileage):
        return capacity*mileage

    
class Electric_Car(Car):

    # for electric car, capacity is kilowatt*hours
    # mileage is kilowatt*hours per 100 miles
    def range_calculation(self, capacity, mileage):
        return capacity/mileage*100

# instantiate gasoline car object
gas_car = Gasoline_Car()

gas_car_tank_capacity = 17      # gallons of gas
gas_car_mpgs = 30               # mileage in miles per gallon
# print calculated range, round to nearest integer
print("Gas car range is {} miles.\n".format(round(gas_car.range_calculation(gas_car_tank_capacity, gas_car_mpgs))))

electric_car_energy_capacity = 88   # energy capacity in kilowatt hours
electric_car_efficiency = 37        # efficiency in kilowatt hours per 100 miles
electric_car = Electric_Car()
# print calculated range, round to nearest integer
print("Electric car range is {} miles.".format(round(electric_car.range_calculation(88,37))))