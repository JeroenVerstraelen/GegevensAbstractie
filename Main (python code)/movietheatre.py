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

    def __init__(self):
        # Queue for reservations
        self.reservationQueue = Queue()
        self.reservationQueue.createQueue()

        # Tables (Showing and Film)
        self.showing_table = Table()
        self.showing_table.setImplementation("hashmap")
        self.showing_table.createTable()

        self.film_table = Table()
        self.film_table.createTable()

        self.reservation_table = Table()
        self.reservation_table.createTable()
       
 
        # Populate datastructures
        self.screens = []
        self.slots = []
        self.dates = []
        self.users = []

        s1 = self.addScreen(0, 200)
        s2 = self.addScreen(1, 150)
 
        sl1 = self.addSlot(0, time(14,30))  # 14:30
        sl2 = self.addSlot(1, time(17))  # 17:00
        sl3 = self.addSlot(2, time(20))  # 20:00
        sl4 = self.addSlot(3, time(21,30)) # 22:30   


        f1 = self.addFilm(0, "Bloody Mary", 6.75)
        f2 = self.addFilm(1, "Star Wars", 2.25)
        f3 = self.addFilm(2, "Clockwork Orange", 8.56)
        f3 = self.addFilm(3, "Shining", 4.52)
        f4 = self.addFilm(4, "V for vendetta", 9.85)

        self.addShowing(0, self.screens[0].getScreenNumber(), 
        2, date(2015,12,25), f2.getID())

        self.addShowing(1, self.screens[1].getScreenNumber(), 
        3, date(2015,12,25), f1.getID())

        self.addShowing(2, self.screens[1].getScreenNumber(), 
        3, date(2015,12,26), f4.getID())

    def addScreen(self, screennumber, seats):
        screen = Screen()
        screen.setScreenNumber(screennumber)
        screen.setSeats(seats)
        self.screens.append(screen)
        return screen

    def addSlot(self, slotID, time):
        slot = Slot()
        slot.setID(slotID)
        slot.setTime(time)
        self.slots.append(slot)
        return slot

    def addUser(self, userID, firstname, lastname, email):
        user = User()
        user.setID(userID)
        user.setFirstName(firstname)
        user.setLastName(lastname)
        user.setEmail(email)
        self.users.append(user)
          
    def addFilm(self, filmID, title, rating):
        film = Film()
        film.setID(filmID)
        film.setTitle(title)
        film.setRating(rating)
        if self.film_table.tableInsert(film):
            return film
        return False

    def addShowing(self, showID, screenID, tID, date, filmID):
        showing = Showing()
        if (len(self.screens) > screenID and len(self.slots) > tID and
            self.film_table.tableRetrieve(filmID)):
            showing.setID(showID)
            showing.setScreenID(screenID)
            timeslot = self.slots[tID]
            showing.setTimeSlot(timeslot)
            showing.setDate(date)
            showing.setFilmID(filmID)
            screen = self.screens[int(screenID)]
            showing.setFreeSeats(screen.getSeats())
            if self.showing_table.tableInsert(showing):
                return True
        return False

    def makeReservation(self, reservationID, userID, showingID, amount):
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
	    return self.getShowing(showingID).checkIn()
	
    def listShowings(self):
       return self.showing_table.traverseTable()
   
    def getShowing(self, showingID):
       return self.showing_table.tableRetrieve(showingID)

    def removeShowing(self, showingID):
       return self.showing_table.tableDelete(showingID)

    def listFilms(self):
       return self.film_table.traverseTable()

    def getFilm(self, filmID):
       return self.film_table.tableRetrieve(filmID)

    def removeFilm(self, filmID):
       return self.film_table.tableDelete(filmID)

    def listUsers(self):
       return self.users

    def listReservations(self):
       return self.film_table.traverseTable()
	   
    def getTickets(self, showingID):
       return self.getShowing(showingID).getTickets()
	
