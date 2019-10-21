'''addition, subtraction, multiplication, division
num1, num2, operation'''

n1 = int(input("enter first number"))
n2 = int(input("Enter Second number"))
ops = input("Enter the option")
error = 0
if(ops.__eq__("Add")):
    result = n1 + n2
    print("Result of addition ", result)

if(ops.__eq__("Sub")):
    result = n1 - n2
    print("Result of Subtraction ", result)

if(ops.__eq__("Mul")):
    result = n1 * n2
    print("Result of Multiplication ", result)

if(ops.__eq__("Div")):
    result = n1 / n2
    print("Result of Division ", result)

if(ops != "Add" and ops != "Sub" and ops != "Mul" and ops != "Div"):
    print("Invalid operation ", ops)
def test():
    '''hello this is sample
    docstring of method'''
    print('method')

print(__doc__)
print(test.__doc__)