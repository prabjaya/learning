class Stack:
    def __init__(self):
        self.stack = []

    # def is_empty(self):
    #     return len(self.stack == 0)
    
    def push(self,item):
        return self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def pop(self):
         return self.stack.pop()
         
    
    def __str__(self):
        return f"{list(reversed(self.stack))}"


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s)

    

