# to get the process down
# 1,2,3 and when selected it will print out what we want to do.
# 2nd Program done today 
# menuSelection  
print("1. Inches to Centimeters.")
print("2. Feet to Meters.")
print("3. Miles to Kilometers.")
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
        menuSelection
    
    case 2:
        feet = int(input("Enter the number of feet: "))
        meters = feet * 0.3048
        print("That is equal to ",meters, "meters.")
        menuSelection

    case 3:
        miles = int(input("Enter the number of miles: "))
        kilometers = miles * 1.60934
        print("That is equal to ",kilometers, "miles.")
        menuSelection
        
    case 4: 
        quit 
        
# menu-driven programs are lists of options for the user to choose from