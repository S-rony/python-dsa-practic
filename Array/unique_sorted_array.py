from os import write

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
arr_2 = []
# 0: 0,0 : empty
# 1: 0,1 : arr[i] arr[j] : arr[1] arr[0] : 2,1
# 2:0,1,2
# 3:0,1,2,3
# arr = [1,2,3]


#make a unique element output: [1,2,3,4,5], we need the size of the arr with unique element
#brute force time n*n
# time complexity is o(n*n) and space is o(n)

for i in range(0,len(arr),1):
    is_duplicate = False
    for j in range(0,i):
        if arr[i] == arr[j]:
            is_duplicate = True
            break
    if is_duplicate is False:
        arr_2.append(arr[i])

print(arr_2)

#time complexity o(n) and space is o(1)
#arr = 1,2,2,5
# write = 0  index = 0 element = 1
# i = 1 index = 1 element = 2      arr[i] != arr[write] , 2!=1 true,
# w = 1 index = 1 , element = 2    ,  arr[1] = arr[1], so in the place of the
# write the i element will come


def uniqueSortedElements(arr):
    if len(arr) == 0:
        return 0
    write = 0
    for i in range(1,len(arr)):

        if arr[i] != arr[write]:
            write += 1
            arr[write] = arr[i]
    return write + 1


arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(uniqueSortedElements(arr))



# for i in range(0, len(arr), 1):
#     is_similar = False
#     for j in range(0, i):
#         if arr[i] == arr[j]:
#             is_similar = True
#             break
#     if is_similar is False:
#         arr_2.append(arr[i])
#
# print(arr_2)
