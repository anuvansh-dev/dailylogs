'''Abstraction- Hiding Implementation details from the user and shpwing only the essential functionalities.
- Can be acheived by using Abstract classes and Abstract methods(from abc module).
- Abstract Classes serves as a blueprint for creating other classes but cannot be instantiated directly(or we cannot create an object of an abstract class).
- Abstract classes contains abstract methods(doesnt contain any implementation/empty) defined under @abstractmethod decorator.
- Subclasses must implement all the abstract classes.
- Concrete classes are the classes which can be instantiated and contains implementations of all methods.
'''
#Example- A shape class which is an abstract class contains abstract methods like area() and perimeter().
#Any specific shape('subclass'- like circle, rectangle etc.) must implement area() and perimeter() methods.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass



#Concrete Subclass 1: Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

#implementation of abstract methods of Shape class   
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

#Concrete Subclass 2: Rectangle
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

# implementation of abstract methods of Shape class
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    

#instantiating concrete classes
c1 = Circle(4)
area = c1.area()
print(area)
perimeter = c1.perimeter()
print(perimeter)

r1= Rectangle(2, 5)
r_area = r1.area()
print(r_area)
r_perimeter = r1.perimeter()
print(r_perimeter)

#here we simply defined a common interface or blueprint (what methods shapes must have) while leaving the implementaion to subclasses.
#And we are interacting with the subclasses(circle) through the interface defined by the abstract class(shape).

#Example2- 

#Abstract Class
class Vehicle(ABC):
     
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):

    def __init__(self, model):
        self.model = model
        
    def start_engine(self): 
        print(f"The {self.model} car's engine has started!")

    def stop_engine(self):
        print(f"The {self.model} car's engine has stopped!")

class Motorcycle(Vehicle):

    def __init__(self, model):
        self.model = model
        
    def start_engine(self):
        print(f"The {self.model} motorcycle's engine has started!")

    def stop_engine(self):
        print(f"The {self.model} motorcycle's engine has stopped!")


civic = Car("Honda Civic")
civic.start_engine()
civic.stop_engine()

r15 = Motorcycle("Yamaha R15")
r15.start_engine()
r15.stop_engine()