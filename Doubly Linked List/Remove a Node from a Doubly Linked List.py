class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Double_Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,val):
        temp = Node(val)
        if self.head is None:
            self.head = temp
            return
        if self.head is not None:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def del_node(self,val):
        #if node is empthy
        if self.head is None:
            print("Node is Empty")
            return
        t = self.head
        if t.data == val:
            self.head = t.next
            if self.head is not None:
                self.head.prev = None
                return
        while t.next is not None:
            if t.data == val:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next
        if t.data == val:
            t.prev.next = None
            return



        #if delete value at head

        # if t  == delete value


        # del value at last




    def print_node(self):
        t = self.head
        while t is not None:
            print(t.data)
            t = t.next

obj = Double_Linked_List()
obj.insert_at_beg(50)
obj.insert_at_beg(40)
obj.insert_at_beg(30)
obj.insert_at_beg(20)
obj.del_node(30)
obj.print_node()

