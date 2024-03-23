def main():
    displayMenu()
    while True:
        choice = input("choice")
        
    if(choice == 1):
        mysql_connect.viewCitiesByCountry()
        displayMenu()
    
    

    elif (choice == "x"):
        print("goodbye thanks for using our database")

    else: 
            
        displayMenu()
    

def displayMenu():
    print("-------------------")
    print("ATU DB PROJECT")
    print("-----------------------------")
    print("Welcome To The Database Menu")
    print("1 - View Cities By Country")
    print("2 - View Countries by Independence Year")
    print("3 - Add New Person")
    print("4 - View Countries By name")
    print("5 - View Countries By Population")
    print("6 - Find Students By Address")
    print("7 - Add New Course")
    print("x - To Exit The Database")
    print("------------------------")

if __name__ == "__main__":
    # only execute if run as a script
    main()
