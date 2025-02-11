# Creating same method in subclasses and calling it for instances of different classes. sound_horn()
#Method overriding
class Car():
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"Make: {self.make} \nModel: {self.model} \nYear: {self.year}"
    
    def sound_horn(self):
        print("Car Horn: Beep Beep!")


class Sedan(Car):
    
    def __init__(self, make, model, year, num_doors):
        Car.__init__(self, make, model, year)
        self.num_doors = num_doors

    def car_type(self):
        print("Sedan")

    def sound_horn(self):
        print("Sedan Horn: Beep Beep!")
        

class ElectricCar(Car):

    def __init__(self, make, model, year, battery_capacity):
        Car.__init__(self, make, model, year)
        self.battery_capacity = battery_capacity

    def battery_info(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")

    def sound_horn(self):
        print("Electric Car Horn: Silent Beep Beep!")

class HybridCar(Sedan, ElectricCar):
     
    def __init__(self, make, model, year, num_doors, battery_capacity, mileage):
        Sedan.__init__(self, make, model, year, num_doors)  # Initialize Sedan part (Car + Sedan)
        ElectricCar.__init__(self, make, model, year, battery_capacity)  # Initialize ElectricCar part (Car + ElectricCar)
        self.mileage = mileage
        

    def fuel_efficiency(self):
        return self.mileage * (self.battery_capacity / 100) # combine fuel efficiency with battery power
    
    def display_info(self):
        return f"{super().display_info()} \nType: Hybrid"
    
    def sound_horn(self):
        print("Hybrid Car Horn: Silent Beep Beep!")

vehicles = [Car("Suzuki", "Swift", 2021), Sedan("Honda", "City", 2018, 4), ElectricCar("Tata", "Nexon", 2024, 0.73), HybridCar("Maruti", "Grand Vitara", 2024, 4, 0.76, 20)]
# c1 = Car("Hyundai", "Verna", 2020)
# c2 = Sedan("Honda", "City", 2018, 4)

# print(c2.display_info())
# # print(c1.display_info())

for i in vehicles:
    i.sound_horn()
