'''Practice Exercise:-
a)Create a class called Car with the following properties:
-make (brand of the car, e.g., "Toyota")
-model (model of the car, e.g., "Camry")
-year (production year of the car)

b)A method display_info() to print the car's details.

c)Create a subclass Sedan that inherits from Car and adds an additional property num_doors (number of doors).

d)Add a method car_type() in Sedan to return "Sedan" (or print it).
'''

class Car():
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"Make: {self.make} \nModel: {self.model} \nYear: {self.year}"


class Sedan(Car):
    
    def __init__(self, make, model, year, num_doors):
        super().__init__(self, make, model, year)
        self.num_doors = num_doors

    def car_type(self):
        print("Sedan")
        

'''Multiple Inheritance
Exercise:
a)Create a new class ElectricCar that inherits from Car and has an additional property battery_capacity (in kWh).

b)Add a new method named battery_info() to print battery capacity.

c)Then create a HybridCar class that inherits from both Sedan and ElectricCar.
This class should have methods that display both fuel efficiency and battery capacity. 
The __init__ method of HybridCar should take parameters for make, model, year, num_doors, and battery_capacity.

d)Override the fuel_efficiency() method to return a combined fuel efficiency that factors in both fuel and battery power.

Objective: Practice multiple inheritance and understanding how to deal with properties and methods from multiple parent classes.
'''

class ElectricCar(Car):

    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def battery_info(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")

class HybridCar(Sedan, ElectricCar):
     
    def __init__(self, make, model, year, num_doors, battery_capacity, mileage):
        Sedan.__init__(self, make, model, year, num_doors)
        ElectricCar.__init__(self, make, model, year, battery_capacity)
        self.mileage = mileage
        

    def fuel_efficiency(self):
        return self.mileage * (self.battery_capacity / 100) # combine fuel efficiency with battery power
    
    def display_info(self):
        return f"{super().display_info()} \nType: Hybrid"

grand_vitara = HybridCar("Maruti", "Grand Vitara", 2024, 4, 0.76, 20)
print(grand_vitara.fuel_efficiency())
print(grand_vitara.display_info())
tesla = ElectricCar("Tesla", "v", 2020, 2.0)
print(tesla.display_info())




    



