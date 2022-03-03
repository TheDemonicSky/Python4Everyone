fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("Cannot open that file, please try again.")
    quit()

for line in fhand:
    print(line.upper())
