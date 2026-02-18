def twopointerreversal(chars):
    left = 0
    right = len(chars) - 1
    while left < right:
        chars[left],chars[right] = chars[right],chars[left]
        left +=1
        right -=1

chars = ['a','b','c']
twopointerreversal(chars)
s1 = ''.join(chars)
print(s1)

print("Testcases")
result1 = ['a','b']
assert len(twopointerreversal(chars)) == 2
print(result1)
