def computepay(hours, rate):
    #Exception handler for non-numeric inputs
    try:
        fh = float(hours)
        fr = float(rate)
    except:
        print("Error, please enter numeric input")
        quit()
    #Overtime calculations    
    if fh > 40:
        fh = ((fh - 40) * 1.5) + 40
        pay = fh * fr
    else:
        pay = fh * fr
    return pay

#Input for hours and rate of pay
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

#Calling the function and assigning a variable
xp = computepay(hours, rate)
print("Pay", xp)
