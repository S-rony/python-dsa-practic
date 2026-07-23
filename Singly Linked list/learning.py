class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next

class SinglyLinkedlist:
    def __init__(self,head = None):
        self.head = head

    def insert_at_end(self, value):
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def print_link_list(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data)
            t1 = t1.next
        print(t1.data)
obj = SinglyLinkedlist()
obj.insert_at_end(20)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.print_link_list()