import random

# result=[]
# for i in range(0,5):
#     result.append(random.randint(-5000,5000))
# print(result)



def gen(count,upper,lower):
    result = []
    for i in range(count):
        result.append(random.randint(upper,lower))
    return result


print(gen(5,-5000,5000))


result1 = gen(6,-5000,5000) 
assert len(result1) == 6
print(result1)


result2 = gen(20,-5000,5000)
assert len(result2) == 20
print(result2)

print(type(gen(1,-5000,5000)))

