
"""
class Person:
    def __init__(self,nn,dd,gg):
        self.pname = nn
        self.dob = dd
        self.gender = gg

    def display(self):
        print("person_name:", self.pname)
        print("Person_dob:", self.dob)
        print("person_gender:", self.gender)


class student(Person):
    def __init__(self,x,y,z,a,b):
        Person.__init__(self,x,y,z)
        self.dept = a
        self.id = b

    def display(self):
        Person.display(self)
        print("stud_dept:", self.dept)
        print("stud_id", self.id)


class faculty(Person):

    def __init__(self,x,y,z,a,b):
        Person.__init__(self,x,y,z)
        self.salary = a
        self.dept = b

    def display(self):
        Person.display(self)
        print("Fac_salary:", self.salary)
        print("Fac_dept:", self.dept)



s1 = student("johnny", "20/20/20", "male", "somecomputerstuff", "67")
s1.display()
f1 = faculty("Bob", "19/19/19", "male", "99,000", "infosec")
f1.display()"""

class automobile:
    def __init__(self,a,b,c):
        self.size = a
        self.tire_cnt = b
        self.length = c


    def display(self):
        print("Size:", self.size)
        print("tire amount: ", self.tire_cnt)
        print("Length of automobile:", self.length)


class car(automobile):

