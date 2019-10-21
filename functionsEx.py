#Even number function
n1= int(input("enter the number One \n"))
n2=300


#n = int(input("enter the value to find"))

def evenFun():
    result = ""
    if (n%2 == 0):
        print("True")
        #result = "True"
    else:
        print("False")
        #result ="False"
  #  return result


def fact():
    var = 1
    fact = 1
    while(var <= n):
        fact = var * fact
        var += 1
    return fact

def calc(n1=23,n2=50):
    print("number one is :" , n1)
    print("number two is :", n2)

#evenFun()
#print (str)

#print(fact())

calc(n1,n2)

calc(n2,n1)

calc()

def fun1(*var):
    print("this is variable with")
    for x in var:
        print(x)

fun1(10,2,30,'test123')
