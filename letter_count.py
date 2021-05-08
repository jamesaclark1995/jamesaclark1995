# This program tells you the number of each character in a file

try:
    file_name = input("Enter file name: ")

    letter_count = {} # Dictionary will store characters and their number

    file = open(file_name, 'rt')
    data = file.read()
    data = data.lower()

    count = 0 # This will become the letter_count values

    for char in data:
        count = data.count(char)
        letter_count[char] = count
        count = 0

    for key, value in letter_count.items():
        print(key, "->", value)

    file.close()

except:
    print("File doesn't exist")
