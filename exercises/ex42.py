# Animal is-a object
class Animal(object):
    pass

#Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        #dog has-a name
        self.name = name

# Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        #cat has-a name
        self.name = name

# person is-a object
class Person(object):

    def __init__(self, name):
        #person has a name
        self.name = name

        #person has a pet
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        # probably making a new person on the new instance of Employee
        super(Employee, self).__init__(name)
        # employee has-a salaray
        self.salary = salary

#fish is-a object
class Fish(object):
    pass

#salmon is an instance of a fish
class Salmon(Fish):
    pass

#halibut is also a fish, but different than a Salmon
class Halibut(Fish):
    pass

# rover is-a dog
rover = Dog("Rover")

# satan is a cat (agree)
satan = Cat("Satan")

# mary is a person
mary = Person("Mary")

#mary has a pet named satan
mary.pet = satan

#frank is an employee that makes 120000
frank = Employee("Frank", 120000)

# frank has a pet, that is a dog name rover
frank.pet = rover

#flipper is an instance of fish
flipper = Fish()

#crouse is an instance of salmon that is a fish
crouse = Salmon()

#harry is an instance of halibut that is a fish
harry = Halibut()
