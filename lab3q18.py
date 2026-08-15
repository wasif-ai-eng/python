s = input("Enter a sentence: ")
words = s.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("Word frequency:")
for key, value in freq.items():
    print(key, ":", value)
