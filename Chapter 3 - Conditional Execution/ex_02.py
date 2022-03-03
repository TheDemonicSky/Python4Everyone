sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()
if fh > 40:
    fh = ((fh - 40) * 1.5) + 40
else:
    pay = fh * fr
print("Pay:", pay)
