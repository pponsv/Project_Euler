"""
How many of the words in 'words.txt' are triangle words?
"""
triangles = []
for i in range(1000):
    triangles.append(int(i*(i+1)/2))
triangles_set = set(triangles)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def is_triangle(word):
    tval = 0
    for letter in word:
        idx = alphabet.find(letter)
        tval += idx+1
    if tval in triangles_set:
        return 1
    else:
        return 0

print(is_triangle('SKY'))


fh = open('words.txt')
words = next(fh).split(',')
words = [word.strip("\"") for word in words]
n = 0
for word in words:
    n += is_triangle(word)
print(n)
