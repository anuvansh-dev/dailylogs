# A class named Employee having one class attribute and one method
class Employee:
    company = "seasia" #class attribute
    
    def __init__(self, name, age, salary):
        # print("Object created")
        #instance attributes
        self.name = name 
        self.age = age
        self.salary = salary
    
    
    def get_salary(self):
        print(f"Hi {self.name}, Your salary is {self.salary}.")
    

emp1 = Employee("Anuvansh", 21, 2000000)
print(emp1.name)
print(emp1.age)
print(emp1.salary)
emp1.get_salary()
print(emp1.company)

