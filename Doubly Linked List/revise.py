class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None


class double_linked_list:

    def __init__(self, head = None):
        self.head = head

    def insert_at_end(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = temp
        temp.prev = t

    def insert_at_beg(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insert_at_med(self):




    def print_dll(self):
        t = self.head
        while t.next is not None:
            print(t.data)
            t = t.next
        print(t.data)


obj = double_linked_list()

obj.insert_at_beg(5)
obj.insert_at_beg(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.insert_at_end(50)
obj.print_dll()



