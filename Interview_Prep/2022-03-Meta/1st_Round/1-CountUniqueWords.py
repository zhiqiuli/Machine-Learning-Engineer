unique_words = {}
with open('1-UniqueWords.txt', 'r') as file:
    a = file.readline() # read the single line
    for w in a.split(','):
        unique_words[w] = 0

with open('1-Book.txt', 'r') as file:
    a = file.readlines() # read the entire file
    for line in a:
        for w in line.split(' '):
            if w in unique_words:
                unique_words[w] += 1