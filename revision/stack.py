class stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)
    
    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)


s = stack()
s.push(10)
s.push(20)
s.push(40)
s.push(50)
print(s)

print(s.peek())
print(s)
print(s.pop())
print(s)