class Student:
    school_name = "HEKKMAH SCHOOL"

    def __init__(self, name): 
        self.name = name
        self.grades = []  

    def add_grade(self, score):
        if 0 <= score <= 100:
            self.grades.append(score)
            print("Added grade:", score)
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def average_grade(self):
        if len(self.grades) == 0:
            return 0  
        total = sum(self.grades)
        return total / len(self.grades)

    def student_info(self):
        avg = self.average_grade()
        return "Name: " + self.name + " School: " + Student.school_name + " Average: " + str(avg)


s = Student("Qusai")
s.add_grade(90)
s.add_grade(80)
s.add_grade(100)   
print(s.student_info())   
print("Average grade:", s.average_grade())