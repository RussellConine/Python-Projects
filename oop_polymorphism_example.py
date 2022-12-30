# parent class
class Bike:
    # parent class attributes
    brand = 'Specialized'
    wheel_count = 2
    wheel_size_in = 29
    location = 0

    # parent class method
    def ride(self):
        print('You are riding a bike.')

# child class- road bike
class RoadBike(Bike):
    # child class attributes
    color = 'black'
    terrain = 'road'
    gears = 24

    # child class method- unique to RoadBike child class
    def ride(self):
        print('Your {} gear bike is made to ride on the {}.'.format(str(self.gears),self.terrain))


# child class- mountain bike
class MountainBike(Bike):
    # child class attributes
    suspension = 'full'
    brakes = 'hydraulic'
    gears = 8
    
    # child class method- unique to RoadBike child class
    def ride(self):
        print('Your {} gear mountain bike has a {} suspension.'.format(str(self.gears),self.suspension))


if __name__ == '__main__':
    # create bike object
    bike = Bike()
    # call ride method of bike class
    bike.ride()

    # create road bike object
    road_bike = RoadBike()
    # call ride method of road bike object
    road_bike.ride()

    # create mountain bike object
    mountain_bike = MountainBike()
    # call ride method of mountain bike object 
    mountain_bike.ride()