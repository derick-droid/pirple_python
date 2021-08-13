"""
inheritance in python
"""

# parent class


class ComputerScience:
    def __init__(self, school="computing and informatics", duration=4):
        self.school = school
        self.duration = duration

# child class


class Students(ComputerScience):

    def __init__(self, school, duration, StudentYear, StudentPoints, StudentName):
        ComputerScience.__init__(self, school, duration )

        self.StudentYear = StudentYear
        self.StudentsPoints = StudentPoints
        self.StudentsName = StudentName

    def students_name(self, name):
        self.StudentsName = name

    def students_scored_point(self,):

        self.StudentsPoints += 1

    def students_year(self, year):
        self.StudentYear = year


student_reg1 = Students("computing and informatics", 4,  1, 12, "derrick okinda")

print(f"{student_reg1.StudentsName} is in school of {student_reg1.school}")
print(f"he is in year {student_reg1.StudentYear}")
print(f"he has {student_reg1.StudentsPoints} points")
print(f"The course of computer science takes {student_reg1.duration} to study")

# accessing the methods inside a class and changing data

student_reg1.students_scored_point()
print(student_reg1.StudentsPoints)
student_reg1.students_name("Javies Odhiambo")
print(student_reg1.StudentsName)