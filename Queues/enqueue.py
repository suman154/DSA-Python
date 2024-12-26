class Node:
    def __init__(self, data):
        self.data = None
        self.next = None

    
    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
