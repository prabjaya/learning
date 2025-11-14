class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __lt__(self,other):
        return self.age < other.age

    def __repr__(self):
        return f"name='{self.name},age = '{self.age}'"

data = [Person('A',10),Person('B',4),Person('C',2)]

print(data)

data.sort()

print(data)