'''
Implementing a queue for printer tasks
In the last video, you learned that queues can have multiple applications, such as managing the tasks for a printer.

In this exercise, you will implement a class called PrinterTasks(), which will represent a simplified queue for a printer. To do this, you will be provided with the Queue() class that includes the following methods:

enqueue(data): adds an element to the queue
dequeue(): removes an element from the queue
has_elements(): checks if the queue has elements. This is the code:
    def has_elements(self):
      return self.head != None
You will start coding the PrinterTasks() class with its add_document() and print_documents() methods. After that, you will simulate the execution of a program that uses the PrinterTasks() class.
'''


'''
Question
The following code shows you how to enqueue() an element into a queue and dequeue() an element from a queue using singly linked lists. Can you calculate the complexity of both methods using Big O Notation?

  def enqueue(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node 
  def dequeue(self):
    if self.head:
      current_node = self.head
      self.head = current_node.next
      current_node.next = None

      if self.head == None:
        self.tail = None
Possible answers
'''

'''
Possible answers
O(n)
O(1)
O(log n)
O((n^2))
The correct answer is O(1) for enqueue() and O(1) for dequeue().
'''



