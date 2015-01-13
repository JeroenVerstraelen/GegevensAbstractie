class Film:
    ''' Represents a film '''

    def __init__(self):
        self.ID = 0
        self.title = ""
        self.rating = 0.00
   
    def __str__(self):
        ''' Returns a string containing ID, title and rating '''
        return str(self.ID) + " " + str(self.title) + " " + str(self.rating)
   
    def setID(self, ID):
        ''' Sets the ID '''
        self.ID = ID

    def setTitle(self, title):
        ''' Sets the title '''
        self.title = title

    def setRating(self, rating):
        ''' Sets the rating '''
        self.rating = rating

    def getID(self):
        ''' Returns the ID '''
        return self.ID

    def getTitle(self):
        ''' Returns the title '''
        return self.title

    def getRating(self):
        ''' Returns the Rating '''
        return self.rating

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

    def __mod__(self, other):
        return self.ID % other
