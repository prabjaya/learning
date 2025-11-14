class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"name='{self.name}' age ='{self.age}'"


data = [Employee('A',10),Employee('C',2),Employee('B',5)]
print(data)

data.sort(key = lambda x : x.name)

print(data)

data.sort(key = lambda x : x.age)
print(data)