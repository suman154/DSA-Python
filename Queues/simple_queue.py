import queue

# Create a SimpleQueue instance
orders_queue = queue.SimpleQueue()

# Add items to the queue
orders_queue.put("Suman")
orders_queue.put("Bhatta")
orders_queue.put("Python Developer")

# Print the size of the queue
print("The size is: ", orders_queue.qsize())

# Retrieve and print items from the queue
print(orders_queue.get())
print(orders_queue.get())
print(orders_queue.get())

# Check if the queue is empty
print("Empty queue: ", orders_queue.empty())
