'''
Implementing a Stack with the push method
In the last video, you learned how to implement stacks in Python. As you saw, stacks follow the LIFO principle; the last element inserted is the first element to come out.

In this exercise, you will follow two steps to implement a stack with the push() operation using a singly linked list. You will also define a new attribute called size to track the number of items in the stack. You will start coding the class to build a Stack(), and after that, you will implement the push() operation.

To program this, you will use the Node() class that has the following code:

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
        self.top = None  # The top of the stack
        self.size = 0    # Initialize size to 0

    def push(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.top is None:
            # If the stack is empty, the new node becomes the top
            self.top = new_node
        else:
            # Otherwise, point the new node to the current top
            new_node.next = self.top
            self.top = new_node  # Update the top to the new node
        self.size += 1  # Increment the size of the stack

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_node = self.top  # Get the current top node
        self.top = self.top.next  # Update the top to the next node
        self.size -= 1  # Decrement the size
        return popped_node.data  # Return the data of the popped node

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data  # Return the data of the top node

    def is_empty(self):
        return self.size == 0  # Return True if the stack is empty

    def get_size(self):
        return self.size  # Return the current size of the stack

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top element is:", stack.peek())  # Output: Top element is: 3
print("Stack size is:", stack.get_size())  # Output: Stack size is: 3

print("Popped element is:", stack.pop())  # Output: Popped element is: 3
print("Stack size is now:", stack.get_size())  # Output: Stack size is now: 2