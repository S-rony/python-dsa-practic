class DoublyListNode:
    def __init__(self, val: int, prev: 'DoublyListNode' = None, next: 'DoublyListNode' = None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def countNodes(self, head: DoublyListNode | None) -> int:
        """Counts the number of nodes in a doubly linked list.

        Args:
            head: The head node of the list (or None for an empty list).

        Returns:
            The total number of nodes in the list.
        """
        # Your implementation here
        curr = head
        count = 0
        temp = curr
        while temp is not None:
            count += 1
            temp = temp.next
        return count

node1 = DoublyListNode(1)
node2 = DoublyListNode(2)
node3 = DoublyListNode(3)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

# Ab Solution class ka object banao
sol = Solution()

# Method call karo aur result ek variable mein rakho
result = sol.countNodes(node1)

# Print karo
print("Total nodes:", result)