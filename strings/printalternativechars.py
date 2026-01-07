string = "abcdefghijk"
print("alternativecharacter from left side")
print(string)
for ch in range(0,len(string),2):
    print(string[ch])

print("alternativecharacter from right side")
for i in range(len(string)-1,-1,-2):
    print(string[i])

