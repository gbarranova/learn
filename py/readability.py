text = input("Text: ")
text = text.lower()
words = text.count(" ") + 1
print(words)
sentences = text.count(".") + text.count("!") + text.count("?")
print(sentences)
letters = len(text) - sentences - text.count(" ") - text.count("'") - text.count(",")
print(letters)

L = letters*100/words
print(L)
S = sentences*100/words
print(S)
index = 0.0588 * L - 0.296 * S - 15.8
print(round(index))