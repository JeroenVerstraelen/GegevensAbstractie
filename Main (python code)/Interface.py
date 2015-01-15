# This file provides a user interface with a menu structure and     methods
# to interact with the program.
import os
from movietheatre import * 

theatre = Movietheatre()

# defining function clear to clear the screen.
# call "clear" on linux, "cls" on windows.
if os.name == "nt":
    def clear():
        os.system("cls")
else:
    def clear():
        os.system("clear")
        
##########################################################################
# USER INPUT METHODS
# The following methods provide the basic interaction with the program,
# asking for input and calling the appropriate methods.
##########################################################################

def create_reservation():
    ''' Asks for input and creates a reservation '''
    print("** making reservation ***********")
    userID = int(input("Please enter your user ID: "))
    showingID = int(input("Please enter a showing ID: "))
    amount = int(input("How many tickets would you like? "))
    reservationID = len(theatre.listReservations())
    if theatre.makeReservation(reservationID, userID, showingID, amount):
        print("reservation made. press enter to return")
    else:
        print("reservation failed. press enter to return")
    input("")

def create_user():
    ''' Asks for input and creates a user '''
    print("** creating user ***********")
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")
    email = input("Please enter your e-mail: ")
    userID = len(theatre.listUsers())
    theatre.addUser(userID, firstname, lastname, email)
    print("User created. Your userID is "+str(userID)+".")
    print("Press enter to return")
    input("")

def remove_user():
    ''' Asks for input and removes a user '''
    print("** removing user ***********")
    userID = int(input("Please enter the userID: "))
    if theatre.removeUser(userID):
        print("User removed. press enter to return")
    else:
        print("User could not be removed. press enter to return")
    input("")  

def create_film():
    ''' Asks for input and creates a film '''
    print("** adding a new film ***********")
    filmID = int(input("Please enter the filmID: "))
    title = input("Please enter the title: ")
    rating = float(input("Please enter a rating: "))
    if theatre.addFilm(filmID, title, rating):
        print("Film Added. press enter to return")
    else:
        print("Film could not be created. press enter to return")
    input("")

def delete_film():
    ''' Asks for input and deletes a film '''
    print("** Deleting a new film ***********")
    id = int(input("Please enter the ID of the film: "))
    if theatre.removeFilm(id):
        print("Film Removed. press enter to return")
    else:
        print("Film could not be removed. press enter to return")       
    input("")

def change_film():
    ''' Asks for input and changes the implementation of the film_table '''
    print("** changing film implementation ***********")
    print("\nValid implementations are: ", theatre.listImplementations())
    implementation = input("Please enter the new implementation: ")
    probingtype = 0
    if implementation == "hashmap":
        print("choose a probing type for the hashmap. Valid types are:")
        print("0: separate chaining")
        print("1: linear probing")
        print("2: quadratic probing")
        probingtype = input("Please enter probing type number: ")
    if theatre.changeFilm(implementation, probingtype):
        print("Implementation changed. press enter to return")
    else:
        print("Implementation does not exist. press enter to return")
    input("")    

def create_showing():
    ''' Asks for input and creates a showing '''
    print("** adding a new showing ***********")
    showingID = int(input("Please enter the showingID: "))
    screenID = int(input("Please enter the screenID: "))
    timeslotID = int(input("Please enter the timeslotID: "))
    filmID = int(input("Please enter the filmID: "))
    day = int(input("Please enter the day of the month: "))
    month = int(input("Please enter the month (numeric): "))
    year = int(input("Please enter the year: "))
    if day <= 0 or day > 31 or month <= 0 or month > 12 or year < 0:
        int("t")
    date1 = date(year, month, day)
    if theatre.addShowing(showingID, screenID, timeslotID, date1, filmID):
        print("Showing added. press enter to return")
    else:
        print("Showing could not be created. press enter to return")
    input("")

def delete_showing():
    ''' Asks for input and deletes a showing '''
    print("** deleting showing ***********")
    showingID = int(input("Please enter the showingID: "))
    if theatre.removeShowing(showingID):
        print("Showing removed. press enter to return")
    else:
        print("Showing could not be removed. press enter to return")
    input("")

def change_showing():
    ''' Asks for input and changes the implementation of the showing_table '''
    print("** changing showing implementation ***********")
    print("\nValid implementations are: ", theatre.listImplementations())
    implementation = input("Please enter the new implementation: ")
    probingtype = 0
    if implementation == "hashmap":
        print("choose a probing type for the hashmap. Valid types are:")
        print("0: separate chaining")
        print("1: linear probing")
        print("2: quadratic probing")
        probingtype = input("Please enter probing type number: ")
    if theatre.changeShowing(implementation, probingtype):
        print("Implementation changed. press enter to return")
    else:
        print("Implementation does not exist. press enter to return")
    input("")    

def sort_showing():
    ''' Asks for input and sorts the showing_table '''
    print("** sorting showing ***********")
    keyType = input("Please input the type of the searchKey (Date/Slot/Screen): ")
    if theatre.sortShowing(keyType):
        print("Showings sorted. press enter to return")
    else:
        print(" Press enter to return")
    input("")   

def checkin():
    ''' get a showing ID and check in viewers for that showing '''
    print("** checking in ********************")
    showingID = int(input("Please input the showing ID: "))
    showing = theatre.getShowing(showingID)
    if showing:
        answer = "y"
        while answer == "y":
            clear()
            print("Now checking in for showing with ID: ",showingID)
            # print(" there are ", theatre.getTickets(showingID), "tickets still not checked in.\n") |A Stack does not have a getLength() function.
            # getTickets(showingID) returns the Stack itself.
            answer = input("type 'y' to check in a viewer, any other key to stop checking in: ")
            if answer == "y":
                if not theatre.checkIn(showingID):
                    input("")
                    break
            input("")
    else:
        print("I'm sorry, we don't know a showing with this ID.\npress enter to return")
        input("")

def importdata():
    ''' Asks for a data file and imports the data in that file '''
    print("** importing data ***********")
    datafile = input("Please enter data file name: ")
    if theatre.populate(datafile):
        print("Data imported. Press enter to return.")
    else:
        print("Import failed. Press enter to return.")
    input("")


###########################################################################
# MENU STRUCTURE
# following methods make up the menu structure of the program, allowing
# the user to navigate between menus and access the user input methods.
###########################################################################
def reservationmenu():
    ''' shows reservation menu, executes chozen input '''
    while True:
        clear()
        print("== RESERVATION MENU ==\n")
        print("Make your choice:\n")
        print(" 0. Return to main menu")
        print(" 1. Reserve for existing userID")
        print(" 2. Reserve for new user")
        print(" 3. Remove user")
        print(" 4. List users")
        choice = input("\n> ")
        try:
            if int(choice) == 0: return True
            elif int(choice) == 1:
                create_reservation()
            elif int(choice) == 2:
                create_user()
                create_reservation()
            elif int(choice) == 3:
                remove_user()
            elif int(choice) == 4:
                if len(theatre.listUsers()) == 0:
                    print("No users available.")
                else:
                    for user in theatre.listUsers():
                        print(user)
                input("\nPress enter to continue")
        except ValueError:
           input("Illegal value. Press enter to continue")
           continue

def filmsmenu():
    ''' shows films menu, executes chozen input '''
    while True:
        clear()
        print("== FILMS MENU ==\n")
        print("Make your choice:\n")
        print(" 0. Return to main menu")
        print(" 1. Add a film")
        print(" 2. Delete a film")
        print(" 3. List films")
        print("     31. sorted by title")
        print("     32. sorted by rating")
        print(" 4. Change Implementation")
        choice = input("\n> ")
        try:
            if int(choice) == 0: return True
            elif int(choice) == 1:
                create_film()
            elif int(choice) == 2:
                delete_film()
            elif int(choice) == 3:
                for film in theatre.listFilms():
                    print(film)
                input("\nPress enter to continue")
            elif int(choice) == 31:
                sorter = Table()
                for film in sorter.sortObjectList(theatre.listFilms(),
                                                  Film.getTitle):
                    print(film)
                input("\nPress enter to continue")
            elif int(choice) == 32:
                sorter = Table()
                for film in sorter.sortObjectList(theatre.listFilms(),
                                                  Film.getRating):
                    print(film)
                input("\nPress enter to continue")
            elif int(choice) == 4:
                change_film()
        except ValueError:
           input("Illegal value. Press enter to continue")
           continue

def showingsmenu():
    ''' prints showing menu, executes chozen input '''
    while True:
        clear()
        print("== SHOWINGS MENU ==\n")
        print("Make your choice:\n")
        print(" 0. Return to main menu")
        print(" 1. Add a showing")
        print(" 2. Remove a showing")
        print(" 3. List showings")
        print(" 4. Sort showings")
        print(" 5. check in viewers for a showing")
        print(" 6. Change implementation")
        choice = input("\n> ")
        try:
            if int(choice) == 0: return True
            elif int(choice) == 1:
                create_showing()
            elif int(choice) == 2:
                delete_showing()
            elif int(choice) == 3:
                for showing in theatre.listShowings():
                    print(showing)
                input("\nPress enter to continue")
            elif int(choice) == 4:
                sort_showing()
            elif int(choice) == 5:
                checkin()
            elif int(choice) == 6:
                change_showing()
        except ValueError:
            input("Illegal value. Press enter to continue")
            continue

def mainmenu():
    ''' prints the main menu and calls submenus '''
    while True:
        clear()
        print("== MAIN MENU ==\n")
        print("Make your choice:\n")
        print(" 1. Make reservation")
        print(" 2. Manage showings")
        print(" 3. Manage films")
        print(" 4. Import data")
        print(" 5. Quit")
        choice = input("\n> ")
        try:
            if int(choice) == 1: 
                reservationmenu()
            elif int(choice) == 2: 
                showingsmenu()
            elif int(choice) == 3: 
                filmsmenu()
            elif int(choice) == 4:
                importdata()
            elif int(choice) == 5:
                return 0
        except ValueError:
            input("Illegal value. Press enter to continue")
            continue

# Call our main menu to get the ball rolling
mainmenu()
