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

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        if not self.has_elements():
            return None
        return self.items.pop(0)
    
    def has_elements(self):
        return len(self.items) > 0


class PrinterTasks:
    def __init__(self):
        self.queue = Queue()  # Initialize the Queue instance for storing tasks
      
    def add_document(self, document):
        # Add the document to the queue
        self.queue.enqueue(document)
      
    def print_documents(self):
        # Iterate over the queue while it has elements
        while self.queue.has_elements():
            # Remove the document from the queue and print it
            print("Printing", self.queue.dequeue())


tasks = PrinterTasks()

# Add documents to the printer queue
tasks.add_document("Document1")
tasks.add_document("Document2")
tasks.add_document("Document3")

# Print all documents in the queue
tasks.print_documents()
