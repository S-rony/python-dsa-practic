# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    """Helper: build a linked list from a Python list, return head."""
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_list(head):
    """Helper: print a linked list starting at the given node."""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # TODO: implement
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                print(slow.val)

























# --- quick manual tests ---
if __name__ == "__main__":
    sol = Solution()

    head1 = build_list([1, 2, 3, 4, 5])
    result1 = sol.middleNode(head1)
    print_list(result1)  # Expect: 3 -> 4 -> 5

    # Expect: 3 -> 4 -> 5 -> 6