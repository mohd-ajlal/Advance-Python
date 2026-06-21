from collections import deque

queue = deque()

queue.append(10)   # Enqueue
queue.append(20)

print(queue.popleft())  # Dequeue