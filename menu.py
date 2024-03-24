
def main():
    displayMenu()
    while True:
        choice = input("choice")
        
    if(choice == 1):
        mysql_connect.viewCitiesByCountry()
        displayMenu()
    
    elif (choice == 2):
        print("View Countries by Independence Year")
        while True:
            try:
                year = int(input("Please Enter the Year you wish to query: "))
                break 
            except ValueError:
                 print("Invalid year entered. Please enter a valid number for the year")
            countries = mysql_connect.viewCountriesByIndependenceYear(year)
            for countries in countries:
                print(country['Name'], ":", country['Continent'], ":", country["IndepYear"])
            displayMenu()
    
    elif (choice == 3):
        print("Add a person to the database")
        person_name = input("personname: ")
        age = input("Age: ")
        salary = input("Salary: ")
        city = input("city:")
        results = mysql_connect.addNewPerson(person_name, age, salary, city)
        print("The database has been updated would you like to View people")
        if choice == "yes":
            mysql_connect.viewPeopleByPerson()
        if choice == "no":
            displayMenu()
            
    elif (choice == 4):
        country_name = str(input("Please enter the Country Name: "))
        countries = mysql.connect.getCountryData()
        for country in countries:
             if str.casefold(country_name) in str.casefold(country["Name"]):
                    print(country["Name"],":",country["Continent"],":",country["Population"],":",country["HeadOfState"])
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
    print("6 - View Twinned Cities")
    print("7 - Twin with Dublin")
    print("x - To Exit The Database")
    print("------------------------")

if __name__ == "__main__":
    # only execute if run as a script
    main()
