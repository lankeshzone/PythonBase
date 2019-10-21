a = [231,132,105,3452,1230]
print("Original Array : ", a)

for i in range(len(a)):
    hadSwap = 0
    for j in range(0, len(a)-i-1):
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            print("after swap", a)
            hadSwap = 1
    if(hadSwap == 0):
        print("\nHad no swap in the last inner loop so exiting outer for loop")
        print("Final Sorted Array is : ", a)
        break