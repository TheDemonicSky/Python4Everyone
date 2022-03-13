counts = dict()
fname = input("Enter file: ")
try:
    fhand = open(fname)
except:
    print("Cannot open that file try again", fname)
    quit()

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        day = words[2]
        if day not in counts:
            counts[day] = 1
        else:
            counts[day] += 1

print(counts)
