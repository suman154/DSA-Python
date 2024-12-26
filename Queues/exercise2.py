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
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def has_elements(self):
        return not self.is_empty()

class PrinterTasks:
    def __init__(self):
        self.queue = Queue()

    def add_document(self, document):
        self.queue.enqueue(document)

    def print_documents(self):
        while self.queue.has_elements():
            document = self.queue.dequeue()
            print(f"Printing: {document}")

printer_tasks = PrinterTasks()
# Add some documents to print
printer_tasks.add_document("Document 1")
printer_tasks.add_document("Document 2")
printer_tasks.add_document("Document 3")
# Print all the documents in the queue
printer_tasks.print_documents()