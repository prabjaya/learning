class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
       self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def __str__(self):
        return f"{ list(self.queue)}"

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q)
print(q.dequeue())
print(q)
print(q.peek())
print(q)
