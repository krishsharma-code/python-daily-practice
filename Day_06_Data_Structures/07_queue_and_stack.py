# 07_queue_and_stack.py
# Concept: Using lists for Stack (LIFO) and Queue (FIFO) operations

# --- STACK (Last-In, First-Out) ---
# Similar to a stack of plates: You add to the top and take from the top.
browser_history = []

# Pushing items onto the stack
browser_history.append("google.com")
browser_history.append("github.com")
browser_history.append("python.org")
print(f"Browser History (Stack): {browser_history}")

# Popping items from the stack (the most recent)
current_page = browser_history.pop()
print(f"Clicked Back: {current_page}")
print(f"New Current Page: {browser_history[-1]}")
print(f"Stack after pop: {browser_history}")

# --- QUEUE (First-In, First-Out) ---
# Similar to a line at a store: First person in line is the first to be served.
from collections import deque # More efficient than list for queues

print("\n--- Queue Operations ---")
customer_queue = deque(["Alice", "Bob", "Charlie"])
print(f"Initial Queue: {customer_queue}")

# Adding to the queue (enqueue)
customer_queue.append("David")
print(f"David joined the line: {customer_queue}")

# Removing from the queue (dequeue)
first_customer = customer_queue.popleft()
print(f"Serving {first_customer}")
print(f"Queue after serving: {customer_queue}")
