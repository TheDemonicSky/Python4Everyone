count = 0
total = 0
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("Cannot open that file, please try again.")
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find(':')
        length = len(line)
        extracted = float(line[pos + 1 : length])
        count = count + 1
        total = total + extracted

average = total / count
print("Average spam confidence: ", average)
