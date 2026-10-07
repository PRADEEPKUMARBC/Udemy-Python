# class Student:
#     name = "Pradeep"

# S1 = Student()
# print(S1.name)

# class Car:
#     color = "Red"
#     brand = "jaguar"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# car2 = Car()
# print(car2.color)
# print(car2.brand)

# class Student:
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("Adding new student in database")

# s1 = Student("Pradeep")
# print(s1.name)  

# s2 = Student("Ramesh")
# print(s2.name)



class Student:

    # default constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding New Student to Database")

S1 = Student("Pradeep", 98)
print(S1.name, S1.marks)

S2 = Student("Karan", 100)
print(S2.name, S2.marks)




class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database")

s1 = Student("Pradeep", 90)
print(s1.name)

class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome Student", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Pradeep" , 99)
print(s1.name)
print(s1.marks)