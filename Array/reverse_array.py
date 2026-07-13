
# lis[::-1]
def reverse(lis):
    left = 0
    right = len(lis) - 1
    while left < right:
        temp = lis[left]
        lis[left] = lis[right]
        lis[right] = temp
        left += 1
        right -= 1
    print(lis)



l = [23,45,6,3,4]
reverse(l)
