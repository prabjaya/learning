import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self,value):
        heapq.heappush(self.heap,-value)
    
    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return  str([-e for e in self.heap])


max= MaxHeap()

max.push(10)
max.push(20)
max.push(30)
max.push(40)
max.push(50)

print(max)

print(max.pop())

print(max)


print(max.peek())
print(max)