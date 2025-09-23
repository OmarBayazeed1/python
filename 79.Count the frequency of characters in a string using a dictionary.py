#79.Count the frequency of characters in a string using a dictionary
text = "omar mo"
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)

