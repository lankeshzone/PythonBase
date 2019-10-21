Age = 10

# if condition
if Age > 18 :
    print("He is allowed to Vote ", Age)

Age = 20
#If-else condition
if Age < 18:
    print("Age doesnot allow to travel ", Age) # executes when the condition is true
else:
    print("Age allows to travel ", Age) #execute when the codition is false

str = 'Rahul'
i=1
while(str=='Rahul'):
    print("Value of i is :", i)
    i+=1
    if(i>=20):
        break

Age = 3
if Age < 18:
    print('less than 18')
    if Age < 10 :
        print('Age less than 10')
        if(Age<5):
            print('Age is less than 5')
else:
    print('age is more than 18')


weekday = ['Mon','Tue','Wed','Thu','Fri']
for day in weekday:
    if day.__contains__('Wed'):
        print("I have a party on Weddnessday", day)
    else:
        print('Go to office', day)

rainbow = ['violet','indigo','blue','green','yellow','orange','red']
#for each loop
for color in rainbow:
    print('color of rainbow',color)

#generic for loop
for x in range(3):
    if(x==2):
        print("i need to goto canada")
    else:
        print('will stayback in bangalore')

for y in range(2,6):
    print("value of y",y)

# for(i=1;i<4;i++)
for z in range(0,20,5):
    print('each increment by 5',z)



