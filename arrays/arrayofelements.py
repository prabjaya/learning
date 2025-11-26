def gen(num):
    res = []
    for i in range(num):
        res.append(i)
    return res

print("Array of elements")
print(gen(5))

    
result1 = gen(6) 
assert len(result1) == 6
print(result1)

result2 = gen(20)
assert len(result2) == 20
print(result2)

result3 = gen(30)
assert len(result3) == 30
print(result3)

print(type(gen(5)))

