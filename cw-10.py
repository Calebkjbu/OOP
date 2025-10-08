class Student:
    def __init__(self):
        self.stu_id = ""
        self.stu_Name = ""
        self.major = ""
        self.gpa = 0.0
        self.dop = ""
    def add_student(self):
        self.stu_id = input("Enter Stu ID")
        self.stu_Name = input("Enter Student Name")
        self.major = input("Enter Student's Major")
        self.gpa = input("Enter Student's Gpa")
        self.dop = input("Enter Date of Birth")
    def edit_student(self):
        self.stu_id = input("WHat you wanna change")
    def display_student(self):
        print("stuid:", self.stu_id)
        print("name", self.stu_Name)
        print("major", self.major)
        print("gpa",self.gpa)
        print("dop", self.dop)


class Courses:
    def __init__(self):
        self.type = ""
        self.credits = 0
        self.course_Id = ""
        self.name = ""

    def add_Course(self):
        self.type = input("What is the course type?")
        self.credits = input("how many credits in this course?")
        self.course_Id = input("What is the course id?")
        self.name = input("What is the name of the course?")

    def edit_Course(self):
        self.type = input("What is the course type?")
        self.credits = input("how many credits in this course?")
        self.course_Id = input("What is the course id?")
        self.name = input("What is the name of the course?")

class Proffesor:
    def __init__(self):
        self.faculty_id = ""
        self.name = ""
        self.department = ""
        self.qualifications = ""


    def add_prof(self):
        self.name = input("What is the name of the prof?")
        self.faculty_id = input("What is the id of the prof?")
        self.department = input("What is their department?")
        self.qualifications = input("what degree do they got?")

s1 = Student()

s1.add_student()
s1.display_student()

p1 = Proffesor()

p1.add_prof()