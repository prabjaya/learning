def unique_char(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None

print(unique_char("ppy"))


# def unique_char(s):
#     result = []
#     for ch in s:
#         if s.count(ch) == 1:
#             result.append(ch)
    
#     if not result:
#         return None
#     return result

# print(unique_char("ppyabc"))
