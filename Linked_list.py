class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class list:
    def __init__(self):
        self.head = None
    def display(self):
        temp = self.head
        if self.head == None:
            print("Empty")
        else:
            while temp:
                temp = temp.next
                print(temp.data)

        