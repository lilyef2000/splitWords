english = open('english.txt', 'r')
english = english.readlines()


for line in english:
    file = open(str(len(line) - 1) + 'longWords.txt', 'a')
    file.write(line)

print('done')
