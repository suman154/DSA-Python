class Node:
    def __init__(self, data):
        self.data = None
        self.next = None


    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

        if self.head == None:
            self.tail = None
        


    