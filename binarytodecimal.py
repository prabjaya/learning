def binary_to_decimal(binary_num):
    decimal = 0
    power = 0

    for bit in reversed(binary_num):
        decimal += (int(bit) * 2 ** power)
        power +=1
    return decimal

binary_num = "1101"
result= binary_to_decimal(binary_num)
print( f"{result}")