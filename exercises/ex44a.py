#Inheritance

class Parent():

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass #tells python you want an empty block

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
