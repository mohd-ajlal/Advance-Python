# Queue in Python
# A queue is a linear data structure that follows the First In First Out (FIFO) principle. It means that the first element added to the queue will be the first one to be removed. Queues are commonly used in scenarios where order matters, such as task scheduling, breadth-first search algorithms, and handling requests in web servers.

# Creating a queue
queue = []

# Adding elements to the queue
queue.append(1)
queue.append(2)
queue.append(3)

# Removing elements from the queue
print(queue.pop(0))  # Output: 1
print(queue.pop(0))  # Output: 2
print(queue.pop(0))  # Output: 3

# all methods of queue
# Adding elements to the queue
queue.append(1)
queue.append(2)

# Removing elements from the queue
print(queue.pop(0))  # Output: 1
print(queue.pop(0))  # Output: 2

# Checking if the queue is empty
if not queue:
    print("Queue is empty")  # Output: Queue is empty

# Checking the size of the queue
print(len(queue))  # Output: 0

