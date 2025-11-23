def is_anagram(s1,s2):
    return sorted(s1.lower())== sorted(s2.lower())


print(is_anagram("listen","silent"))

def sort_string(s):
    s = list(s.lower())  # convert string to list of chars
    n = len(s)
    for i in range(n):
        for j in range(0, n-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
    return s

def is_anagram(s1, s2):
    return sort_string(s1) == sort_string(s2)

print(is_anagram("listen", "silent"))  # True