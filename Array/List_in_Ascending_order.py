class Solution:
    def isAscending(self, arr):
        """
        Determines if the given list is in non‑decreasing order.
        :param arr: List[int] - the integer list to check
        :return: bool - True if sorted ascending (allowing equals), otherwise False
        """
        # Your implementation here
        is_asc = True
        for i in range(0, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                is_asc = True
            else:
                is_asc = False
        if is_asc:
            return True

        return False