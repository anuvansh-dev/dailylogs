class Student:

    school = "Kendriya Vidyalaya" # Class or static attribute- shared accross all the objects.
    
    def __init__(self, m1, m2, m3):
        # Instance Attributes- Unique to each object
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    #Instance methods- works with instance attributes
    def result(self):
        if self.m1 >= 35 and self.m2 >= 35 and self.m3 >= 35:
            print("Congrats! You are Pass")
        else:
            print("Sorry, You failed.")
    #Instance Accessor or getter methods- accesses or gets the instance attributes
    def get_marks(self):
        print(f"Your marks are {self.m1}, {self.m2}, {self.m3}")
    #Instance setter or mutator methods- modifies or sets instance attributes
    def set_m1(self, value):
        self.m1 = value

    #class method- defined using decorator '@classmethod'- works with class attributes
    @classmethod
    def get_sch(cls):
        print(Student.school)
    #static method- not concerned about any of the instance or class attributes.
    @staticmethod
    def greet():
        print("Welcome User!")
    

st1 = Student(38, 56, 60)
st2 = Student(35, 16, 41)

print(st1.m1)
print(st1.school)
st1.get_marks()
st1.result()
st2.result()
Student.greet()