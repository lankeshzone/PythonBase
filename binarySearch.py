arr = [23,45,67,96,114]
l=0
r=len(arr)
m=0
search = 135
while l<=r:
    x=int((l+r)/2)
    if(x<=len(arr)):
        m=x
    else:
        break
    if(arr[m]<search):
        l=m+1
    elif (arr[m]==search):
        print("search found at ", m)
        break
    else:
        r=m-1
print("Value is at position" , m)
