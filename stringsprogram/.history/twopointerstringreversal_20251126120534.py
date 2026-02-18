def twopointer_string(chars):
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left],chars[right] = chars[right],chars[left]
        l