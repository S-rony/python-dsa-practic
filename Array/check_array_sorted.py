def is_sorted(arr):
    start = 0
    end = len(arr) - 1
    for i in range(len(arr)):
        start+=1
        if arr[start] >= arr[start+1]:

            return False
        else:
            return True






arr = [1,3,7,9]
print(is_sorted(arr))