class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello Student")

    def get_average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "your average score is", sum / len(self.marks))

s1 = Student("Pradeep", [90, 80, 70])
print(s1.name, s1.get_average())
s1.hello()

s1.name = "Pradeepkumar B C"
s1.get_average()