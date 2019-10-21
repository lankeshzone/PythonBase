test = [[4, 5, 6, 8], [1, 2, 3, 1], [7, 8, 9, 4], [1, 8, 7, 5]]

n = len(test[0])

for j in range(0, n ):
    for k in range(0, n):
        print(test[j][k], end=" ")
    print("")

test.__len__()