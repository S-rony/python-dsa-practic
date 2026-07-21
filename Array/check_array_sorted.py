def is_sorted(arr):
    # start = 0
    # end = len(arr) - 1
    for i in range(len(arr) - 1):

        # start+=1
        # sorted = True
        if arr[i] > arr[i+1]:
            sorted = False
            break
    else:
        sorted = True
    if sorted:
        return True
    else:
        return False

arr = [1,3,7,9,8]
print(is_sorted(arr))
