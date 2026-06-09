msg = "This product is excellent excellent excellent and very useful"

words = msg.split()

# 1
print("Total Words:", len(words))

# 2
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print("Word Frequencies:")
for k in freq:
    print(k, "->", freq[k])

# 3
max_word = ""
max_count = 0
for k in freq:
    if freq[k] > max_count:
        max_count = freq[k]
        max_word = k

print("Most Frequent Word:", max_word)

# 4
once = []
for k in freq:
    if freq[k] == 1:
        once.append(k)

print("Words Appearing Once:")
print(once)

# 5
count = 0
for w in words:
    if len(w) > 5:
        count += 1
print("Words >5 characters:", count)

# 6
print("Reverse Order:", words[::-1])

# 7
print("Unique Words:", list(set(words)))
