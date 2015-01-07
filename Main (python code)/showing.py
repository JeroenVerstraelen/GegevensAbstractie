from stack import *
from ticket import *
from datetime import *

class Showing:

    def __init__(self):
        self.ID = 0
        self.screenID = 0
        self.timeSlot = None
        self.date = None
        self.filmID = 0
        self.freeseats = 0
        self.tickets = Stack()
        self.tickets.createStack()
        self.empty_ts = datetime.now()

    def setID(self, ID):
        self.ID = ID

    def setScreenID(self, screenID):
        self.screenID = screenID

    def setTimeSlot(self, timeSlot):
        self.timeSlot = timeSlot

    def setDate(self, date):
        self.date = date

    def setFilmID(self, filmID):
        self.filmID = filmID

    def setFreeSeats(self, seats):
        self.freeseats = seats

    def getID(self):
        return self.ID

    def getScreenID(self):
        return self.screenID

    def getTimeSlot(self):
        return self.timeSlot

    def getDate(self):
        return self.date

    def getFilmID(self):
        return self.filmID

    def getFreeSeats(self):
        return self.freeseats
		
    def getTickets(self):
        ''' Returns a pointer to the Stack containing the tickets. '''
        return self.tickets

    def isStarted(self):
        if not self.date == None and not self.timeSlot == None:
            dt = datetime.combine(self.date, timeSlot.getTime)
            if dt <= datetime.now():
                if empty_ts > dt:
                    return empty_ts
                return dt
            return -1

    def reserve(self, ticket_am):
        if not self.date == None and not self.timeSlot == None:
            dt = datetime.combine(self.date, self.timeSlot.getTime())
            if datetime.now() < dt:
                for i in range(ticket_am):
                    ticket = Ticket()
                    if not self.tickets.push(ticket):
                       return False
                    self.freeseats -= 1
                return True 
            print("This showing has already started, you can no longer make a reservation.")  
        return False 
       
    def checkIn(self):
        if not self.date == None and not self.timeSlot == None:
            if not self.tickets.isEmpty():
                if self.tickets.pop():
                    if self.tickets.isEmpty():
                        self.empty_ts = datetime.now()
                return True
            print("\nI'm sorry, there are no more reservations left. Press enter to return")
            input("")
        return False
        

    def __str__(self):
        return ("ID: "+str(self.getID())+"\n ScreenID: "+str(self.getScreenID())+ "\n TimeSlot: "+str(self.getTimeSlot().getTime())+ "\n Date: "+str(self.getDate())+
                "\n FilmID: "+str(self.getFilmID())+ "\n FreeSeats: "+str(self.getFreeSeats()))


    def __eq__(self, other):
        return self.ID == other
 
    def __ne__(self, other):
        return not self.ID == other

    def __lt__(self, other):
        return self.ID < other

    def __le__(self, other):
        return self.ID <= other

    def __gt__(self, other):
        return self.ID > other
   
    def __ge__(self, other):
        return self.ID >= other
