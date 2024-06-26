# Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Person name : ",self.name)
        print("Person age : ",self.age)

class Student(Person):
    def __init__(self,name,age,section):
        super().__init__(name,age)
        self.section = section
    def displayStudent(self):
        print("Student name : ",self.name)
        print("Student age : ",self.age)
        print("Student section : ",self.section)


P = Person("Tomas Wild", 37)
P.display()
print("-------------------------------")
S = Student("Albert", 23, "Mathematics")
S.displayStudent()
