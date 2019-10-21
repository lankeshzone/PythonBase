class student:
    university = "Christ College"
    def fees(self, af,sf,tf):
        fee = af+sf+ tf
        print("Fees for the student" , fee)
    def __init__(self,roll, name, dept):
        self.roll = roll
        self.name = name
        self.dept = dept
        print("Iam init method \n")

lankesh = student(1,"Lankesh H", "Computers")
lankesh.fees(100,20,30)
print(lankesh.roll)
print(lankesh.name)
print(lankesh.dept)
print(student.university)