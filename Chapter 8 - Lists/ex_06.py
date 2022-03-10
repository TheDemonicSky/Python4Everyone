list = []

while True:
    number = input("Enter a number: ")
    #Use if/else to check for "done" input
    if number != str("done"):
        try:
            number = int(number)
            list.append(number)
        except:
            #Exception handler
            print("Invalid Number")
    else:
        print("Smallest: ", min(list), "Biggest: ", max(list))
        quit()
