

class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next

class Single_Linked_list:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insert_in_mid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while t1.next is not None:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next


    def insert_at_end(self,value):
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp


    def delete_ll(self,value):
        t1 = self.head
        prev = t1
        if t1.data == value:
            self.head = t1.next
        while t1.next is not None:
            if t1.data == value:
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if t1.data == value:
            prev.next = None

    def print_ll(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data)
            t1 = t1.next
        print(t1.data)


obj = Single_Linked_list()
obj.insert_at_end(20)
obj.insert_at_end(10)
obj.insert_at_end(19)
obj.insert_at_beg(3)

obj.insert_in_mid(80,10)
obj.delete_ll(19)
obj.print_ll()

