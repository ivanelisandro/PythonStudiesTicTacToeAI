text = input()

text = text.replace(",", "")\
    .replace(".", "")\
    .replace("!", "")\
    .replace("?", "")

text = text.lower()

print(text)
