from showing import *
from screen import *
from film import *
from reservation import *
from slot import *
from user import *

from table import *
from queue import *
from datetime import *

class Movietheatre:
    ''' Represents a movie theatre '''

    def __init__(self):
        # Queue for reservations
        self.reservationQueue = Queue()
        self.reservationQueue.createQueue()

        # Tables (Showing and Film)
        self.showing_table = Table()
        self.showing_table.setImplementation("doublylinkedchain")
        self.showing_table.createTable()

        self.film_table = Table()
        self.film_table.createTable()

        self.reservation_table = Table()
        self.reservation_table.createTable()
       
        # data lists
        self.screens = []
        self.slots = []
        self.dates = []
        self.users = []
        self.implementations = ["binaryTree","doublylinkedchain","hashmap","redBlackTree","234Tree","23Tree"]
        

    def populate(self, textfile):
        ''' loads data into our datastructures from a text file '''
        try: # open given data file, return False if it fails
            handle = open(textfile, "r")
        except:
            print("Error opening file")
            return False
        lines = handle.readlines()
        handle.close
        # getting screens
        start = lines.index("SCREENS\n") + 1
        end = lines.index("END SCREENS\n")
        screens = lines[start:end]
        for screen in screens:
            if not self.addScreen(len(self.screens), screen.rstrip()):
                print("Error loading screens. Check data file syntax")
                return False
        # getting slots
        start = lines.index("SLOTS\n") + 1
        end = lines.index("END SLOTS\n")
        slots = lines[start:end]
        for string in slots:
            slot = string.split(",")
            hour = time(int(slot[0]), int(slot[1].rstrip()))
            if not self.addSlot(len(self.slots), hour):
                print("Error loading slots. Check data file syntax")
                return False
        # getting films
        start = lines.index("FILMS\n") + 1
        end = lines.index("END FILMS\n")
        films = lines[start:end]
        for string in films:
            film = string.split(",")
            if not self.addFilm(film[0], film[1], film[2].rstrip()):  
                print("Error loading films. Check data file syntax")
                return False
        # getting showings
        start = lines.index("SHOWINGS\n") + 1
        end = lines.index("END SHOWINGS\n")
        showings = lines[start:end]
        for string in showings:
            showing = string.split(",")
            showdate = date(int(showing[3]), int(showing[4]), int(showing[5]))
            if not self.addShowing(showing[0], showing[1],
                       int(showing[2]), showdate, int(showing[6].rstrip())):
                print("Error loading showings. Check data file syntax")
                return False
        return True


    def addScreen(self, screennumber, seats):
        ''' Adds a screen to our theatre '''
        screen = Screen()
        screen.setScreenNumber(screennumber)
        screen.setSeats(seats)
        self.screens.append(screen)
        return screen

    def addSlot(self, slotID, time):
        ''' Adds a time slot to the theatre '''
        slot = Slot()
        slot.setID(slotID)
        slot.setTime(time)
        self.slots.append(slot)
        return slot

    def addUser(self, userID, firstname, lastname, email):
        ''' Adds a user '''
        user = User()
        user.setID(userID)
        user.setFirstName(firstname)
        user.setLastName(lastname)
        user.setEmail(email)
        self.users.append(user)

    def listUsers(self):
       ''' Returns a list of our current users '''
       return self.users

    def removeUser(self, userID):
        ''' Removes the user with the given ID '''
        if userID in self.users:
            self.users.remove(userID)
            return True
        return False
       
          
    def addFilm(self, filmID, title, rating):
        ''' Adds a film '''
        film = Film()
        film.setID(filmID)
        film.setTitle(title)
        film.setRating(rating)
        if self.film_table.tableInsert(film):
            return film
        return False

    def listFilms(self):
       ''' Returns a list of our current films '''
       return self.film_table.traverseTable()

    def getFilm(self, filmID):
       ''' Returns the film with the given ID '''
       return self.film_table.tableRetrieve(filmID)

    def removeFilm(self, filmID):
       ''' Removes the film with the given ID '''
       return self.film_table.tableDelete(filmID)


    def changeFilm(self, implementation, probingtype = 0):
       ''' Changes implementation of the films table '''
       if implementation not in self.implementations:
           return False
       items = self.film_table.traverseTable()
       self.film_table.destroyTable()
       self.film_table = Table()
       self.film_table.setImplementation(implementation)
       self.film_table.setProbingType(probingtype)
       self.film_table.createTable()
       for item in items:
           self.film_table.tableInsert(item)
       return True


    def addShowing(self, showID, screenID, slotID, date, filmID):
        ''' Adds a showing '''
        showing = Showing()
        if (len(self.screens) > int(screenID) and len(self.slots) > int(slotID) and
            self.film_table.tableRetrieve(filmID)):
            showing.setID(showID)
            showing.setScreenID(screenID)
            timeslot = self.slots[slotID]
            showing.setTimeSlot(timeslot)
            showing.setDate(date)
            showing.setFilmID(filmID)
            screen = self.screens[int(screenID)]
            showing.setFreeSeats(screen.getSeats())
            return self.showing_table.tableInsert(showing)
        return False

    def listShowings(self):
       ''' Returns a list with all showings '''
       return self.showing_table.traverseTable()
   
    def getShowing(self, showingID):
       ''' Returns the showing with the given ID '''
       return self.showing_table.tableRetrieve(showingID)

    def removeShowing(self, showingID):
       ''' Removes the showing with the given ID '''
       return self.showing_table.tableDelete(showingID)

    def changeShowing(self, implementation, probingtype = 0):
       ''' changes implementation of the showings table '''
       if implementation not in self.implementations:
           return False
       items = self.showing_table.traverseTable()
       self.showing_table.destroyTable()
       self.showing_table = Table()
       self.showing_table.setImplementation(implementation)
       self.film_table.setProbingType(probingtype)
       self.showing_table.createTable()
       for item in items:
           self.showing_table.tableInsert(item)
       return True

    def sortShowing(self, keyType):
       ''' Sorts the internal list of showings by the given keytype
      (only possible if currently using doubly linked chain) '''
       if self.showing_table.getImplementation() == "doublylinkedchain":
           if keyType == "Date":
               sorted = self.showing_table.sortObjectList(self.showing_table.traverseTable(), Showing.getDate)
           elif keyType == "Slot":
               sorted = self.showing_table.sortObjectList(self.showing_table.traverseTable(), Showing.getTimeSlot)
           elif keyType == "Screen":
               sorted = self.showing_table.sortObjectList(self.showing_table.traverseTable(), Showing.getScreenID)
           else:
               return False
           for item in sorted:
               self.showing_table.tableDelete(item)
           for item in sorted:
               self.showing_table.tableInsert(item)
           return True
       print("The implementation of showing_table is not doublylinkedchain.", end='')
       return False

    def makeReservation(self, reservationID, userID, showingID, amount):
        ''' Adds a new reservation '''
        reservation = Reservation()
        reservation.setID(reservationID)
        reservation.setTimestamp(datetime.now())
        reservation.setShowingID(showingID)
        reservation.setAmount(amount)
        self.reservationQueue.enqueue(reservation)
        pr_res = self.reservationQueue.dequeue()
        showing = self.getShowing(showingID)
        if len(self.users) <= userID or not showing:
            return False
        self.reservation_table.tableInsert(reservation)
        if showing != None:
            if showing.getFreeSeats() - amount > 0:
                return showing.reserve(amount)
            print("I'm sorry, there are not enough free seats in this showing ("+str(showing.getFreeSeats())+").")
        print("We don't know a showing with this ID.")
        return False
		
    def checkIn(self, showingID):
        ''' Checks in a viewer for the given showing '''
        return self.getShowing(showingID).checkIn()

    def listReservations(self):
        ''' Returns a list of all our reservations '''
        return self.film_table.traverseTable()
	   
    def getTickets(self, showingID):
        ''' Returns the stack with all the tickets for the given showing '''
        return self.getShowing(showingID).getTickets()
	
    def listImplementations(self):
        ''' Returns a list with all supported table implementations '''
        return self.implementations

    def sortObjectList(self, olist, getter):
        ''' this function takes lists of objects and getter methods to sort the
            objects by different properties '''
        def quicksort(lst):
            if len(lst) < 2:
                return lst
            pivotindex = int((len(lst) - 1)/2)
            newpivotindex = int((len(lst) - 1)/2)
            pivot = lst[pivotindex]
            for i in range(pivotindex - 1, -1, -1):
                if lst[i] >= pivot:
                    lst.insert(newpivotindex, lst.pop(i))
                    newpivotindex -= 1
            for i in range(pivotindex + 1, len(lst)):
                if lst[i] <= pivot:
                    lst.insert(newpivotindex, lst.pop(i))
                    newpivotindex += 1
            leftlist = quicksort(lst[0:newpivotindex])
            leftlist.append(pivot)
            rightlist = quicksort(lst[newpivotindex + 1:len(lst)])
            lst = leftlist + rightlist
            return lst
        templist = []
        for obj in olist:
            templist.append((getter(obj), obj))
        sortedlist = quicksort(templist)
        resultlist = []
        for item in sortedlist:
            resultlist.append(item[1])
        return resultlist
    
        

