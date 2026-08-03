class DoublyListNode:
    def __init__(self, val: int, prev: 'DoublyListNode' = None, next: 'DoublyListNode' = None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def flipDoublyLinkedList(self, head):
        if head is None or head.prev is None and head.next is None:
            return head
        curr = head
        new_head = None
        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            new_head = curr
            curr = curr.prev
        return new_head















