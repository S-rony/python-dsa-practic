class DoublyNode:
    def __init__(self, val: int, next: 'DoublyNode' = None, prev: 'DoublyNode' = None):
        self.val = val  # stored value
        self.next = next  # next node or None
        self.prev = prev  # previous node or None


class Solution:
    def deleteNode(self, head, target):
        """Deletes *target* from the doubly linked list whose head is *head*.

        Parameters
        ----------
        head : DoublyNode | None
            The first node of the list (or None for an empty list).
        target : DoublyNode | None
            The node that must be removed.

        Returns
        -------
        DoublyNode | None
            The (possibly new) head of the list after removal.
        """
        # Your implementation here
        if head is None or target is None:
            return head
        if target.prev:
            target.prev.next = target.next
        else:
            head = target.next

        if target.next:
            target.next.prev = target.prev

        target.prev = None
        target.next = None
        return head


