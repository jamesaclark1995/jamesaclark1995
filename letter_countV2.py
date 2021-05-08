# This program tells you the number of each character in a src

srcname = input("Enter file name: ")

letter_count = {} # Dictionary will store characters and their number

src = open(srcname, 'rt')
data = src.read()
data = data.lower()

count = 0 # This will become the letter_count values

for char in data:
    count = data.count(char)
    letter_count[char] = count
    count = 0

letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

letter_count = dict(letter_count)

for key, value in letter_count.items():
    print(key, "->", value)

src.close()

name = srcname.replace(".txt", "")
dstname = name + ".hist"

dst = open(dstname, 'wt')

for key, value in letter_count.items():
    dst.write(str(key) + "->" + str(value))

dst.close()



