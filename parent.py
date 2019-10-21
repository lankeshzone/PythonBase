class Automobile:
    tyres = " test"
    def __init__(self):
        self.Engine  = 1000 #data member1
        self.Steering ="3 spoke" # data member2
        self.wheels = 4 # data member3

    #methd member
    def initialize(self, steer, eng, wheel):
        self.Steering = steer
        self.Engine = eng
        self.wheels = wheel



class car(Automobile):
    def __init__(self):
        Automobile.__init__(self)
        print("this is child init method")

    def function2(self): #methdd
        print("This is kchild class functions")



c1 = car()
#c1.initialize(100,20,300)
c1.Engine=2000
print(c1.Engine)
print(c1.Steering)
print(c1.wheels)
c2 = car()
c2.Engine=500
c3 = car()
c3.Engine=6000


li = [c1,c2,c3]

for i in range(li.__len__()):
    if(li[i].Engine > 1500):
        print("Heavy")
    else:
        print("Light")

print(li)
