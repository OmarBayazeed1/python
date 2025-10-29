#Implement a queue using collections.deque
#[],[1],[1,3],[1,3,4],append()->[1,3,4]->pop()->4
from collections import deque
class Queue:
    def __init__(self):
        self.queue=deque()
    def enqueue(self,element):
        self.queue.append(element)
    def dequeue(self):
        if self.isEmpty():
            return 'sorry but the queue is empty , can not remove elements'
        else:
            return self.queue.popleft()
    def isEmpty(self):
        return self.size()==0
    def size(self):
        return len(self.queue)
    def __str__(self):
        return str(list(self.queue))

q1=Queue()
q1.enqueue(1)
q1.enqueue(3)
q1.enqueue(4)
print(q1)
print(q1.dequeue())
print(q1)
print(q1.size())
