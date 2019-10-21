#Program for odd or even...

n = int (input("Enter the number"))
temp=1

for x in range(1,int(n)+1):
    if(temp == x):
        temp += 2
        print('odd', x)
    else:
        print('even', x)