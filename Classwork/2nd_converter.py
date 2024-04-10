# to get the process down
# 1,2,3 and when selected it will print out what we want to do.
# 2nd Program done today 
# menuSelection  
print("1. Convert inches to centimeters.")
print("2. Convert feet to meters.")
print("3. Convert miles to kilometers.")
print("4. Exit program")
menuSelection = int(input("Enter your selection: "))

while menuSelection < 1 or menuSelection > 3:
    print("invalid entry")
    print("Input valid entry: ")
    menuSelection = int(input("Enter your selection: "))
    
match menuSelection:
    case 1:
        inches = int(input("Enter the number of inches: "))
        centimeters = inches * 2.54
        print("That is equal to ",centimeters, "centimeters.")
    
    case 2:
        feet = int(input("Enter the number of feet: "))
        meters = feet * 0.3048
        print("That is equal to ",meters, "meters.")

    case 3:
        miles = int(input("Enter the number of miles: "))
        kilometers = miles * 1.609
        print("That is equal to ",kilometers, "miles.")
    case 4: 
        quit 
        
# menu-driven programs are lists of options for the user to choose from
