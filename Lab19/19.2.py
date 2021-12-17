words = []
letter='A'
with open('words.txt', 'r') as file:
    for line in file:
        if letter in line:
            words.append(line)
words.reverse()
print(words)