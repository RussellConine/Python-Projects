# parent class
class Organism:
    name = 'one'
    species = 'two'
    legs = 0
    size = None
    origin = 'three'
    carbon_based = True

    def information(self):
        msg = '\nName: {}\nSpecies: {}'.format(self.name,self.species)
        return msg

# child class
class Human(Organism):
    name = 'Joe'
    species = 'homo sapien'
    legs = 2
    origin = 'earth'

    def ingenuity(self):
        msg = 'human message'



class Dog(Organism):
    name = 'Max'
    species = 'canine'
    legs = 4
    origin = 'earth'


    def bite(self):
        msg = 'bite message'
        return msg



if __name__ == '__main__':
    human = Human()
    print(human.information())

    dog = Dog()
    print(dog.bite())

    