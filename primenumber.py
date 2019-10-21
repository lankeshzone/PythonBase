n = input()

for num in range(2,int(n)+1):
    prime = 0
    temp = 2
    while( temp<num ):
        if((num % temp) != 0):
            prime = 1
        else:
            prime = 0
            break
        temp+=1
    if(prime == 1):
        print("It is a prime number ", num)
    else:
        print("It is not a prime number",num)


