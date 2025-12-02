import random

# for i in range(5):
#     result = random.randint(1,100)
#     print(result)

def randomgen(n):
    return[random.randint(1,100) for i in range(n)]


print(randomgen(5))