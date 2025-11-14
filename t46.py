from collections import deque

d=deque()

d.append(100)
d.append(200)
d.append(300)
d.append(400)
d.append(500)
print(d)
print(d[0])
print(d[-1])
print(d.pop())
print(d.popleft())

print(d.append(800))
print(d.appendleft(900))

print(d)
