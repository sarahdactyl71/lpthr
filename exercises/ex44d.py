class Parent():

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("Parent altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

#This will borrow the implicit function from the Parent class
dad.implicit()
son.implicit()

#This will override the override() function from the Parent class
# and use its own logic in the Child class
dad.override()
son.override()

#shows both the methods of the same name: altered() from parent and child
dad.altered()
son.altered()
