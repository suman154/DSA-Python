"""Question
The following algorithm searches for a given value within a linked list. What is its complexity?

This method uses the Node() class and search() method.

def search(self, data):
    current_node = self.head
    while current_node:
        if current_node.data == data:
            return True
        else:
            current_node = current_node.next
    return False
"""



"""
Possible answers
O(1)
O(n)
O(log n)
O(n^2)
The correct answer is O(n).
The time complexity of this algorithm is O(n) 
because the worst-case scenario involves iterating 
through all the nodes in the linked list to find the 
target value. The number of iterations required to find 
the target value is directly proportional to the size of the i
nput, making the time complexity of this algorithm linear in terms 
of the input size. Therefore, the correct answer is O(n).
"""

