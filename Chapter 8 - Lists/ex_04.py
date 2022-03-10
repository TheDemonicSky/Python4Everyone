list = []
fname = input("Enter file: ")
try:
    fhand = open(fname)
except:
    print("Cannot open that file try again.")
    quit()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in list:
            list.append(word)

list.sort()
print(list)
