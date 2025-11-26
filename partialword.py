all_words = ["apple", "app", "apply", "banana", "band"]
partial_word = "a"

res = []
for word in all_words:
    if word.startswith(partial_word):
        res.append(word)

print(res)