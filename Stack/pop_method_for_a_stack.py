'''
Implementing the pop method for a stack
In this exercise, you will implement the pop() operation for a stack. pop() will be used to remove an element from the top of the stack. Again, we will consider the size attribute to know the number of elements in the stack.

Recall the Node() class:

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
    
  def pop(self):
    # Check if there is a top element
    if self.top is None:
      return None
    else:
            popped_node = self.top
            # Decrement the size of the stack
            self.size -= 1
            # Update the new value for the top node
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data


