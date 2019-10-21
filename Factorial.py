#Factorial  of number... n!=> n * (n-1)*(n-2)...*1

n = int(input("enter the number"))
fact = 1
temp = 1

if(n<0):
    print("invalid input ", n)
else:
    if(n==0):
        print("factorial of number", n ,"is ", fact)
    else:
        while (temp <= n):
            fact = fact * temp
            temp+=1
        print("factorial of number", n ,"is ", fact)
