#Arithmetic operations
n1 = 10
n2 = 3
sum = n1 + n2
print("Sum ", sum)
sub = n1 - n2
print( "Subtract ", sub)
mult = n1 * n2
print("Multiply " , mult)
Div = n1/n2
print("Div ", Div)
mod = n1% n2
print ("Modulo ", mod)
floordiv = n1 // n2
print ("Floor div " , floordiv)
exp = n1 ** n2
print("power ", exp)


#Comparison Operators
print("Equal to oper " , n1 == n2)
print ("greater than op ", n1 > n2)
print ("greater than equal to op ", n1 >= n2)
print ("Less than op ", n1 < n2)
print ("Less than equal to op ", n1 <= n2)
print ("Not Equal to  op ", n1 != n2)


#Assignment Operators
n=5
n += 2 # n=n+2
print(n) #7

n-=2 # n=n-2
print(n) # 5

n*=2 # n=n*2
print(n) #10

n/=2 # n=n/2
print(n) #5

n%=2 # n=n%2
print(n) #1

n//=2  # n= n//2
print(n) # 0

n=4
n**=2 # n=n**2
print(n) #16


#Logical Operators and/or/not
x=10
y=15
print(x>5 and y>5) #true
print(x>5 and y<5) #false
print(x<5 and y>5) #false
print(x<5 and y<5) #false

print(x>5 or y>5) #true
print(x>5 or y<5) #true
print(x<5 or y>5) #true
print(x<5 or y<5) #false

print(not(x>5)) #false
print(not(x<5)) #true

#Bitwise operators
n1 = 10
n2= 5
print (n1 & n2) #Zero
print (n1 | n2) #15
print (n1 ^ n2) #Zero
print(~n2)  # MSB will be replaced with signed bit (1) and rest of the bits will be reversed



