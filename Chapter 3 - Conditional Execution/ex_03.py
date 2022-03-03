ss = input("Please enter your score: ")
try:
    fs = float(ss)
except:
    print("Bad score")
    quit()
if fs > 1.0 or fs < 0:
    print("Bad score")
elif fs >= 0.9:
    print("A")
elif fs >= 0.8:
    print("B")
elif fs >= 0.7:
    print("C")
elif fs >= 0.6:
    print("D")
else:
    print("F")
