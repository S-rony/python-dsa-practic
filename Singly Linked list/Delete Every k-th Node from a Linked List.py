class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeEveryKthNode(self, head: "ListNode | None", k: int) -> "ListNode | None":
        temp = head
        prev = temp
        position = 1
        while temp is not None:
            if k == position:
                prev.next = temp.next
                temp = prev
                temp = temp.next
                position = 1
            else:
                prev = temp
                temp = temp.next
                position += 1



        return None


def build_linked_list(values):
    """Helper: turn [1,2,3] into a linked list, return the head."""
    dummy = ListNode()
    tail = dummy

    for v in values:
        tail.next = ListNode(v)
        tail = tail.next

    return dummy.next


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    sol = Solution()
    sol.removeEveryKthNode(head, 2)