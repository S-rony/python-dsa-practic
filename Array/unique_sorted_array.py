arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# 1 - 2,2,3,4,4,4,5,5
# 2- 2,3,4,4,4,5,5
# 2- 3,4,4,5,5

# arr = [1,2,3]
arr_2 = []

#make a unique element output: [1,2,3,4,5], we need the size of the arr with unique element
#brute force time n*n


for i in range(0, len(arr), 1):
    is_similar = False
    for j in range(0, i):
        if arr[i] == arr[j]:
            is_similar = True
            break
    if is_similar is False:
        arr_2.append(arr[i])

print(arr_2)