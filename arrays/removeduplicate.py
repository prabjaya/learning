my_list = [1, 2, 3, 2, 4, 5, 1, 6]
result = set(my_list)
print(result)


def duplicate(my_list):
    duplicate =[]
    seen = set()

    for item in my_list:
        if item in seen:
            duplicate.append(item)
        else:
            seen.add(item)
    return duplicate

print(duplicate(my_list))