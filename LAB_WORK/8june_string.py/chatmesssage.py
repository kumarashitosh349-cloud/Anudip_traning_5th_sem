msg = "Python is awesome and Python is easy to learn"

chars = len(msg)

words = msg.split()
word_count = len(words)

longest = words[0]
shortest = words[0]

for w in words:
    if len(w) > len(longest):
        longest = w
    if len(w) < len(shortest):
        shortest = w

python_count = words.count("Python")

more_than_4 = []
vowel_words = []

for w in words:
    if len(w) > 4:
        more_than_4.append(w)
    if w[0].lower() in "aeiou":
        vowel_words.append(w)

vowels = 0
consonants = 0

for c in msg:
    if c.isalpha():
        if c.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(chars)
print(word_count)
print(longest)
print(shortest)
print(python_count)
print(more_than_4)
print(vowel_words)
print(vowels)
print(consonants)