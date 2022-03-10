list = []
count = 0
fname = input("Enter file: ")
try:
    fhand = open(fname)
except:
    print("Cannot open that file try again.")
    quit()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        names = words[1]
        print(names)
        count = count + 1

print("There were " + str(count) + " lines in the file with From as the first word")
