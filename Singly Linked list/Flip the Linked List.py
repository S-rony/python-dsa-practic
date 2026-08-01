#
# prev = null
# curr = 1
#
# null    1 -> 2 -> 3 -> null
#         ↑
#        curr
class ListNode:



    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def reverseList( head):
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    print("Original list:")
    print_linked_list(head)

    new_head = reverseList(head)
    print_linked_list(new_head)


