'''
Question
The following algorithm shows you how to add a node at the beginning of a singly linked list using the Node() class and the insert_at_beginning() method. What is the complexity of this algorithm?

 def insert_at_beginning(self,data):
    new_node = Node(data)
    if self.head:
      new_node.next = self.head
      self.head = new_node
    else:
      self.tail = new_node      
      self.head = new_node
'''


"""Possible answers
O(1)
O(n)
O(log n)
O(n^2)
The correct answer is O(1).
The time complexity of this algorithm is O(1) because it takes the same amount of time to execute, regardless of the size of the input. This is because the algorithm only performs a constant number of operations, such as creating a new node and updating the head pointer, to add a node at the beginning of the linked list.
"""




