'Lifo Queue implementation'

import queue
my_book_stack = queue.LifoQueue(maxsize=0)
my_book_stack.put('C Programming')
my_book_stack.put('C++ Programming')
my_book_stack.put('Java Programming')
my_book_stack.put('Python Programming')

print("The size is:", my_book_stack._qsize()) # The size is: 4

print(my_book_stack.get()) # Python Programming
print(my_book_stack.get()) # Java Programming
print(my_book_stack.get()) # C++ Programming
print(my_book_stack.get()) # C Programming

print("Empty Stack:", my_book_stack.empty()) # Empty Stack: True)