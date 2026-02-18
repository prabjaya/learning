data  =[1,2,1,1,2,3,4,5,5,4]

def occurance(data):

    result = {}

    for item in data:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

print(occurance(data))