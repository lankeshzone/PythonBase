import self as self
num1 = 100  #integer number
num2 = 45.035 # float number
print(num1)
print(num2)

print(num2.__abs__())


name = 'Rajeev127457'
print(name)
print(name[4])
print(name[3:])
print(name[1:4])
print(name.lstrip('Ra'))
print(name.replace('jeev','test'))
print(name.swapcase())
print(name.__contains__('clos'))
print(name.isalpha())
print(name.lstrip())
print(name)
print(name.partition('Ra'))


setex = {'violet','indigo','blue','yellow','orange'}
print(setex)
#setex.pop('yellow')
print('setex contains',setex.__contains__('violet'))
setex.pop()
setex.discard('yellow')
setex.add('test123')
print(setex)


dict = {100:'Rajeev',200:'usha',300:'Beena'}
dict2 = {1:'Reva',2:'SVC',3:'MVIT'}
print(dict)
dict.pop(200)
print(dict)
print(dict.keys())
print(dict.get(100))
print(dict2)
#dict2 = dict.copy()
print(dict.values())
dict.popitem()
print(dict)


li = [100,'Test',3.14,84237983749,'rajeev']
print(li)
li.pop(3)
print(li)

li.insert(3,'Aptech')
print(li)
li.insert(4,'Raju')
print(li)
li.reverse()
print(li)
li.__setitem__(3,'Test123')
print(li)


#tuples
tup = ('Mon','Tue','Wed','Thu','Fri','Sat','Sun')
print(tup)


num1 = 100
num2 = 15
x = num1//num2
print(x)

if((num1 <100) and (num2>10)):
    print(num1, num2)
else:
    print('Not equal')

num1 += 20 # num1 = num1 + 20

print(num1**2)


dict3 = {1:'lankesh',2:'Raju',3:'Reema'}
print(dict3)
dict3.pop(2)
print(dict3)
dict3.popitem()
print(dict3)