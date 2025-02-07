#1. Create a class programmer for storing info about programmers working at 'Microsoft'
class Programmer:

    company = "Microsoft"

    def __init__(self, name, domain, salary):
        self.name = name
        self.domain = domain
        self.salary = salary

    def get_info(self):
        print(f"Name: {self.name} \n Domain: {self.domain} \n Salary: {self.salary}")


p1 = Programmer("Rahul", "UI/UX", 50000)
p2 = Programmer("Shyam", "Web Dev", 40000)
p1.get_info()
p2.get_info()

#2.Create a class calculator capable of performing opeartions like square and cube
class Calculator:

    def square(self, n):
        return n * n
    
    def cube(self, n):
        return n * n * n
    

c1 = Calculator()
sqr = c1.square(2)
cube = c1.cube(2)
print(sqr)
print(cube)

#3. Add a static method to greet the user in calculator class in prob 2
class Calculator:

    def square(slf, n):
        return n * n
    
    def cube(self, n):
        return n * n * n
    
    @staticmethod
    def greet():
        print("Hello User")
    

c2 = Calculator()
c2.greet()
 