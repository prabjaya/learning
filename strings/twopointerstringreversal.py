def twopointerreversal(chars):
    left = 0
    right = len(chars) - 1
    while left < right:
        chars[left],chars[right] = chars[right],chars[left]
        left +=1
        right -=1
    return chars

chars = ['a','b','c']
twopointerreversal(chars)
s1 = ''.join(chars)
print(s1)

print("Testcases")
result1 = ['a','b']
print(result1)
assert len(twopointerreversal(result1)) == 2
print(result1,"=Testcase pass")
