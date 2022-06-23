"""
Queues

To-Do list:
    - Make the Queue class[].
    - Add enqueue function[].
    - Add dequeue function[].
    - Test[]. 
                                            
"""

from queue import Empty


class Queue():
    def __init__(self, head):
        self.storage = [head]
        
    def enqueue(self, new_node):
        if self.storage:
            
            self.storage.append(new_node)
            return new_node
        else:
            self.storage = [new_node]
            return new_node   
    
    def dequeue(self):
        if self.storage:
            node = self.storage[0]
            self.storage.pop(0)
            return node
        else:
            return 'No node to be dequeued'
        
    def peek(self):
        if self.storage:
            return self.storage[0]
        else:
            return 'There is No nodes to be peeked.'
        
    
q = Queue(0)
print(q.peek())
q.enqueue(12)
q.enqueue(33)
print(q.dequeue())
print(q.peek())
print(q.dequeue())
print(q.peek())

