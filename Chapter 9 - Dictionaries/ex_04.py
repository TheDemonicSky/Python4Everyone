maximum = None
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
        address = words[1]
        if address not in counts:
            counts[address] = 1
        else:
            counts[address] += 1

for address in counts:
    if maximum is None or counts[address] > maximum:
        maximum = counts[address]

print(list(counts.keys())[list(counts.values()).index(maximum)], maximum)
