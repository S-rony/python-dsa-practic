class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next

class Singly_l_l:
    def __init__(self, head = None):
        self.head = head

    def at_beg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head= temp

    def insert_middle(self,value,x):
        temp = Node(value)
        t1 = self.head
        while t1.next is not None:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def at_end(self,value):
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def delete_node(self,value):
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



obj = Singly_l_l()

obj.at_beg(20)
obj.at_end(30)
obj.at_end(50)
obj.at_end(60)
obj.at_end(70)
obj.at_end(80)
obj.at_end(90)

obj.insert_middle(40,30)
obj.delete_node(50)
obj.print_ll()