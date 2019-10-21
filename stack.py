li=[]

def stack():
    print(li)
    x=int(input("enter the stack operation - '0' for Delete and '1' for insert \n"))
    while( x==1 or x==0):
       if(x==1):
           li.append(input("enter the element to insert"))
           print("After insert ", li)
 #          print(li[len(li)-1])
       else:
           if(len(li)==0):
               print("no elements in the stack to remove \n ")
               break
           else:
               li.remove(li[len(li)-1]) #li.__delitem__(last index)
               print("After delete ", li)
       x=int(input("Enter the stack operation - '0' for Delete and '1' for insert \n"))
    print("Final Stack ",li)


stack()








def que():
    q=[]
    print(q)
    x = int(input("enter the queue operation - '0' for Delete and '1' for Insert \n"))
    while (x == 1 or x == 0):
        if (x == 1):
            q.append(input("enter the element to insert \n"))
            print("After insert ", q)
        else:
            print(len(q))
            if(len(q)==0):
                print("no elements in the Queue to remove \n ")
                break
            else:
                q.__delitem__(0)
                print("After delete ", q)
        x = int(input("Enter the queue operation - '0' for Delete and '1' for insert \n"))
    print("Final Queue ", q)


