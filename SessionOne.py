'''helo this is the doc string
check this for multi-line comment
but can  be done only at the begining of the file'''
# this is my first program in Python
integernum = 100
floatnum = 45.05
longnum = 34567

''' test '''

country = "India"

print("Integer ", integernum)
print("Float nume", floatnum)
print("long nume", longnum)

print("String ", country)
print("String formats", country[4])
def test():
    '''test this docstring
    only'''
    print("in the function")
print(test.__doc__)