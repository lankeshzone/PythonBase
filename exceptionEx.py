x=[0,2,4,5]
num1 = 10
num2 = 2
n=6


try:
    x[2]=30
    def fun1():
        print("inside try")
    div= num1/num2 #person trying to reach the office
    fun1()
except ZeroDivisionError:
    print("Divide by zero error")
except IndexError:
    print("index out of range")


print("continued Execution")



