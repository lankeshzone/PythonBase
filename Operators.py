#Arithmetic operators
n1 = 10
n2 = 6

Sum = n1 + n2
subtract = n1-n2
multi = n1 * n2
div = n1/n2
mod = n1 % n2
florDiv = n1 // n2
exp = n1 ** n2

print(Sum)
print(subtract)
print(multi)
print(div)
print(mod)
print(florDiv)
print(exp)


#Comparison Operators

print(n1 == n2)
print(n1 < n2)
print(n1 <= n2)
print(n1>n2)
print(n1>=n2)
print(n1 != n2)


#Assignment operators
n1+=3 #n1 = n1 +3
print(n1) #13

n1 -= 3  #n1=n1-3
print(n1)  #10

n1*=2  #n1=n1*2
print(n1) #20

n1/=4  #n1=n1/4
print(n1) #5

n1%=3  # n1 = n1 % 3
print(n1) #2

n1 = 10
n1//=4   # n1 = n1 // 4
print(n1) #0

n1**=5 # n1 = n1 ^ 5
print(n1) # 0

n1 = 5
n2 = 7
#logical operators
print(n1>4 and n2>5) # T and T ==> T
print(n1<4 and n2>5) # F and T ==> F
print(n1>4 and n2<5) # T and F ==> F
print(n1<4 and n2<5) # F and F ==> F

print (n1>4 or n2>5) # T or T ==> T
print(n1<4 or n2>5) # F or T ==> T
print (n1>4 or n2<5) # T or F ==> T
print (n1<4 or n2<5) # F or F ==> F

print(not(n1>4)) # not(True) ==> false
print(not(n1<4)) # not(false) ==> true

n1=10
n2=11
#Bitwise operator
print(n1 & n2)
print(n1 | n2)
print(~n2)
print(n1^n2)








