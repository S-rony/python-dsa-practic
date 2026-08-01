# is array sported?
arr = [3,4,2,1]
arr_1 = [1, 3, 2, 4]
is_sorted = True
for i in range(len(arr_1) - 1):
    if arr_1[i] > arr_1[i+1]:
            is_sorted = False
            break
    # else:
    #     is_sorted = True

if is_sorted == False:
    print("Not sorted")
else:
    print("Sorted")

print()


# reverse_an_array:
start = 0
end = len(arr) - 1
temp = 0
while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1
print(arr)

print()

# 2. Check if Array is a Palindrome

arr_3 =  [1, 9, 9, 9, 2]
left = 0
right = len(arr_3) - 1

is_palindrome = False
if len(arr_3) == 0 or len(arr_3) == 1:
    is_palindrome = True
while left < right:
    if arr_3[left] == arr_3[right]:
        is_palindrome = True
    else:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Its palindrome")
else:
    print("Not palindrome")


