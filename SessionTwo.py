
#addition piece of code
num1 = 100  #num1 as the variable with 100 assigned to it
num2 = 200 #num2 as the variable with 200 assigned to it
sum = num1 + num2  #variable sum which is assigned to num1+um2
print("Addition of two numbers ",sum) # print statements allows the user to print on the console

#Multiplicateion piece of code
#num3 = int(input("enter number one")) #num3 as the variable with input from console which is converted to integer type.
#num4 = int(input("enter number two")) #num4 as the variable with input from console which is converted to integer type.
#multiply = num3 * num4 #num5 as a variable assigned with multiplication of nu3 and num4
#print("Multiplication of two number is ",multiply)

#data types
x = 100 #integer number
y = 3.14 #float number


print (x)
print (y)
name = 'lankesh' #defining the string variable and assigning a value
print(name[6]) #prints the character pertaining to the index passed
print(name[3:]) #prints the rest of the string from the index number passed
print(name[2:6]) #prints the substring in the range

# Set data type declaration and usage of different methods
rainbow = {"violet","indigo","blue","green","yellow","orange","red"}
print(rainbow)
rainbow.add("black")
print(rainbow)
normalcolor = {"black","yellow","white"}
print(rainbow.difference(normalcolor))
print(rainbow.issubset(normalcolor))
print(rainbow.issuperset(normalcolor))

#print(rainbow)

#Dictionary - Key and value pair
emp = {1:'lankesh',2:'usha',3:'Beena'} #defining employee dictionary with three values
print(emp)
print(emp.get(2)) #retriving the 2nd value from the dictionary using the key..
print(emp.keys()) #retrieving all the keys from Dictonary
print(emp.values())  #retriving all the values from dictionary
emp.pop(3) #deleting a value using key
print(emp.values())
emp.pop(1)
emp.__setitem__(1,'lankesh') #adding a new item to dictionary
emp.__setitem__(3,'Beena')
print(emp.values()) #retriving all the values from dictionary...










