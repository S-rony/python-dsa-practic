class Solution:
    def findMissingNumber(self, arr):
        """
        arr: List[int] - distinct integers from 1 to n with exactly one missing.
        Returns the missing integer.
        """
        # Your implementation here

        # max = float('-inf')
        # min = float("+inf")
        # for i in range(len(arr)):
        #     if arr[i] > max:
        #         max = arr[i]
        #     if arr[i] < min:
        #         min = arr[i]
        # # for i in range(int(max), int(min), 1):
        #     # new_ = max - i
        #     print(i)



ar = [12, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]

max = float('-inf')
min = float("+inf")
for i in range(len(ar)):
    if ar[i] > max:
        max = ar[i]
    if ar[i] < min:
        min = ar[i]
fond = False
for i in range(int(min), int(max)+1):
    if i not in ar:
        print(i)
        fond = True
        break
if not fond:
    print(max+1)