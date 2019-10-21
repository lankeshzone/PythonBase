class priority_queue:

    def __init__(self,q, prio, n, count1, count2, count3, count4, count5):
        q=[]#no self should be written here
        self.prio=int(input("enter the priority"))
        self.n=input("enter the passenger's name: ")
        self.count1=count1
        self.count2=count2
        self.count3=count3
        self.count4=count4
        self.count5=count5

    def add_pasnger(self, q, n):
        if(self.prio==1):
            print("she is pregnant ")
            q.insert((self.count1), self.n)
            sex=input("enter the sex of the passenger ")
            age=input("enter the age of passenger ")
            self.count1+=1
            print(self.count1, "=count1 ")

        if(self.prio==2):
                print("physically handicap or medical emergency ")
                q.insert((self.count1+self.count2), self.n)
                sex=input("enter the sex of the passenger ")
                age=input("enter the age of passenger ")
                self.count2+=1
                print(self.count2, "=count2")

        if(self.prio==3):
                print("senior citizen ")
                q.insert((self.count2+self.count3+self.count1), self.n)
                sex=input("enter the sex of the passenger ")
                age=input("enter the age of passenger ")
                self.count3+=1
                print(self.count3, "=count3 ")

        if(self.prio==4):
                    print("passenger with an infant ")
                    q.insert((self.count3+self.count4+self.count2+self.count1), self.n)
                    sex=input("enter the sex of the passenger ")
                    age=input("enter the age of passenger ")
                    self.count4+=1
                    print(self.count4, "=count4")

        if(self.prio==5):
                        print("No priority is needed ")
                        q.insert((self.count4+self.count3+self.count2+self.count1+self.count5), self.n)
                        sex=input("enter the sex of the passenger ")
                        age=input("enter the age of passenger ")
                        self.count5+=1
                        print(self.count5, "=count5")

        print("list of passengers is: ", q)

q=[]
prio=[]
n=[]
count1=0
count2=0
count3=0
count4=0
count5=0

for i in range(7):
   a1=priority_queue(q, prio, n, count1, count2, count3, count4, count5)
   a1.add_pasnger(q,n)


#empty queue
#queue is full
#if a person is elgible for more than one priorities
#Queueoverflow
#type of data
