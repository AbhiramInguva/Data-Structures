
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class list:
    def __init__(self):
        "Initalziing the lisked list class"
        self.head = None
        self.tail = None
    
    def display_l(self):
        "Display the entire linked list"
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
    def traverse(self, n):
        " display the nth element of linked list"
        temp = self.head
        count = 1
        while temp is not None:
            if n == count:
                return temp.data
            count += 1
            temp = temp.next
        return "Not found"
    def insert_at_start(self,data):
        "insert node into the start of the linkedlist"
        temp = self.head
        self.head = node(data)
        self.head.next = temp

    def insert_at_end(self,data):
        "insert node at the end of the linkedlist"
        temp = self.head
        while True:
            if temp.next is None:
                self.tail = temp
                break
            temp = temp.next
        temp1 = node(data)
        temp1.next = self.tail
        self.tail = temp1










