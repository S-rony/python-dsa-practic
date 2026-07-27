class Solution:
    def shiftZerosToEnd(self, arr):
        """
        arr: List[int] - The input integer array.
        Returns a new list with zeros moved to the end while preserving the order of non‑zero elements.
        """
        # Your implementation here
        curr = 0
        prev = 0

        for curr in range(len(arr)):
            if arr[curr] != 0:
                temp = arr[prev]
                arr[prev] = arr[curr]
                arr[curr] = temp
                prev+= 1

        return arr


obj = Solution()
print(obj.shiftZerosToEnd([1,2,0,4,3,0,5,0]))
