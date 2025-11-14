import heapq

heap =[]

heapq.heappush(heap,100)
heapq.heappush(heap,200)
heapq.heappush(heap,300)
heapq.heappush(heap,400)

print(heap)

print(heap[0])

print(heap)
print(heapq.heappop(heap))

print(heap)