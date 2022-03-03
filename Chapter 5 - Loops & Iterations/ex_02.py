biggest = None
smallest = None

while True:
    number = input("Enter a number: ")
    #Use if/else to check for "done" input
    if number != str("done"):
        try:
            number = int(number)
            #Initially assigns an input to the variable biggest
            #Checks if any given number is larger than the already
            #assigned number in variable biggest, if the number is
            #larger than it reassigns the new number to the variable
            if biggest == None:
                biggest = number
            elif number > biggest:
                biggest = number

            #Same as biggest variable but checking for the smallest number
            if smallest == None:
                smallest = number
            elif number < smallest:
                smallest = number
        except:
            #Exception handler
            print("Invalid Number")
    else:
        print("Smallest: ", smallest, "Biggest: ", biggest)
        quit()
