

class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_at_end(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = temp
        temp.prev = t

    def insert_at_beg(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insert_at_mid(self, value, x):
        t = self.head
        while t.next is not None:
            if t.data == x:
                break
            t = t.next
        temp = Node(value)
        temp.next = t.next
        if t.next is not None:  # ✅ guard against crash
            t.next.prev = temp  # ✅ fix self-reference bug
        t.next = temp
        temp.prev = t

    def print_doubly_ll(self):
        t = self.head
        while t.next is not None:
            print(t.data, end = " <--> ")
            t = t.next
        print(t.data)

    def deletion_doubly_ll(self, value):
        if self.head is None:
            print("Linked List is empty")
            return
        t = self.head
        if t.data == value:
            self.head = t.next
            if self.head is not None:
                self.head.prev = None
            return
        while t.next is not None:
            if t.data == value:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next
        if t.data == value:
            t.prev.next = None
            return


obj = DoublyLL()
obj.insert_at_beg(5)
obj.insert_at_beg(10)
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.deletion_doubly_ll(30)
obj.insert_at_mid(50,20)
obj.print_doubly_ll()
