total = 0
count = 0

while True:
    number = input("Enter a number: ")
    #Use if/else to check for "done" input
    if number != str("done"):
        try:
            #Make the input an integer and create a running
            #total as well as a count of the number of inputs
            number = int(number)
            total = total + number
            count = count + 1
        except:
            #Exception handler
            print("Invalid Number")
    else:
        #Calculating the average across the inputs and ending the loop
        avg = total / count
        print(total, count, avg)
        quit()
