import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self,value):
        heapq.heappush(self.heap,value)
    

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]


    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return str(self.heap)

min = MinHeap()

min.push(10)
min.push(20)
min.push(30)
min.push(40)
min.push(50)
print(min)

n1=min.pop()
print(n1)
print(min)
n2=min.peek()
print(n2)
n3 = min.is_empty()
print(n3)