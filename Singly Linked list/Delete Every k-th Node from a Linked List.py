class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeEveryKthNode(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 1:
            return None

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head
        pos = 1

        while curr:
            if pos % k == 0:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next
            pos += 1

        return dummy.next


def build_linked_list(values):
    dummy = ListNode()
    tail = dummy

    for v in values:
        tail.next = ListNode(v)
        tail = tail.next

    return dummy.next


def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next
    print("None")


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])

    sol = Solution()
    new_head = sol.removeEveryKthNode(head, 2)

    print_linked_list(new_head)
