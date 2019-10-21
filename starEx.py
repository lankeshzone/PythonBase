from collections import Counter

n = int(input("enter the number of max stars \n"))
def starPrint(n):
    for x in range(1,n):
        for y in range (x):
            print ("*", end=" ")
        print("")
    for i in range (n, 0, -1):
        for j in range(0, i):
            print("*", end=' ')
        print("")

starPrint(n)
ol=[]
def Matrix(n):

    li = []
    for i in range (1,n):
        for j in range (1,n):
            x = input()
            li.append(x)
        ol.__add__(li)
    tl=ol
    li.clear()
    for i in range(0,tl.__len__()):
        print(tl.__getitem__(i))
        #li.clear()

Matrix(n)