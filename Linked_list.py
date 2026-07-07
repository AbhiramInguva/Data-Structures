class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class list:
    def __init__(self):
        self.head = None
    
    def display_l(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next


