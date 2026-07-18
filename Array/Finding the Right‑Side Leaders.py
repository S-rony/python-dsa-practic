# Finding the Right_side leader
arr = [16, 17, 4, 3, 5, 2]
arr_1 = []
arr_2 = []
is_leader = True
for i in range(len(arr) ):
    for j in range(i+1, len(arr)):
        if arr[i] < arr[j]:
            arr_1.append(arr[i])



print(arr_1)