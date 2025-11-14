class Queue:
    def __init__(self):
        self.data = []

    def add(self,element):
        self.data.append(element)


    def read(self):
        return self.data[0]

    def __str__(self):
        return str(self.data)
    

    def remove(self):
        return self.data.pop(0)

    def isEmpty(self):
        return len(self.data) == 0

q = Queue()
q.add(10)
q.add(20)
q.add(30)

print(q)

print(q.read())
print(q)
print(q.remove())
print(q)

print(q.isEmpty())