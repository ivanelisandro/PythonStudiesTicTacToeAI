# the list with words from string
# please, do not modify it
some_iterable = input().split()

words = {word.upper(): word.lower() for word in some_iterable}

print(words)
