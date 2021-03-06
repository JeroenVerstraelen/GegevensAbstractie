import math
import doubly_linked_chain

class Hashmap:     
    def __init__(self,size,probingType=0):
        '''This class is a hashtable, size is the
        wished size of the table it will be set to
        the next higher prime number. The probing type
        can be set to the following: 0 = separate chaining,
        1  = linear probing, 2 = quadratic probing.
        If not specified otherwise the hashtable is set to separate
        chaining. '''
        self.__tableSize = self.__getMapSize(size)
        self.__table = []
        for i in range(self.__tableSize):
            self.__table.append(self.__item(None, None))
        if probingType == 0:
            self.__probeIns = self.__separate_chainIns
            self.__probeRem = self.__separate_chainRem
            self.__probeGet = self.__separate_chainGet
        elif probingType == 1:
            self.__probeIns = self.__linear_probeIns
            self.__probeRem = self.__linear_probeRem
            self.__probeGet = self.__linear_probeGet
        elif probingType == 2:
            self.__probeIns = self.__quadratic_probeIns
            self.__probeRem = self.__quadratic_probeRem
            self.__probeGet = self.__quadratic_probeGet
        self.length = 0


    def __getMapSize(self,needed_size):
        ''' finds the next higher prime number to the needed space '''
        def is_prime(n):
            ''' Returns true if a number is a Prime or false if not.'''
            if n == 2:
                return True
            if n%2 == 0 or n <= 1:
                return False
            sqr = int(math.sqrt(n)) + 1
            for divisor in range(3, sqr, 2):
                if n%divisor == 0:
                    return False
            return True
 
        i = needed_size
        if i%2 == 0:
            i+=1 # makes hashmap size uneven, since it needs to be prime
        while not is_prime(i):
            i+=2;
        return i


    def __separate_chainIns(self, item, searchkey):
        ''' insert an item into the given doubly linked
        chain if the given item isn't a linked chain yet
        a new linked chain will be created.'''
        hash = self.__h(searchkey)
        if isinstance(self.__table[hash], self.__item):
            self.__table[hash] = doubly_linked_chain.Doubly_linked_chain()
            self.__table[hash].insert(searchkey,self.__item(item,searchkey))
            return True
        else:
            for i in self.__table[hash].traverse():
                # If the chain already contains an item with that searchkey.
                if i == searchkey:
                    return False
            return self.__table[hash].insert(searchkey,
                                             self.__item(item,searchkey))
        return False
            


    def __separate_chainRem(self, searchkey):
        ''' Removes the item with the given searchkey from a
        linked chain if the chain only contains one item
        afterwards it will be turned into an item again. '''
        if not self.__separate_chainGet(searchkey):
            return False
        if isinstance(self.__table[self.__h(searchkey)], 
                      type(doubly_linked_chain.Doubly_linked_chain())):
            if self.__table[self.__h(searchkey)].length == 1:
                self.__table[self.__h(searchkey)] = self.__item(None, None)
                return True
            self.__table[self.__h(searchkey)].remove(searchkey)
            if self.__table[self.__h(searchkey)].length == 1:
                tmp = self.__table[self.__h(searchkey)].headPtr.next.item
                self.__table[self.__h(searchkey)] = tmp     
        else:
            self.__table[self.__h(searchkey)] = self.__item(None, None)
        return True


    def __separate_chainGet(self, searchkey):
        ''' returns the item with the specified searchkey ''' 
        if isinstance(self.__table[self.__h(searchkey)], 
                      type(doubly_linked_chain.Doubly_linked_chain())):
            tmp = self.__table[self.__h(searchkey)].getItem(searchkey)
            if tmp == False:
                return False
            else:
                return tmp.item
        else:
            return False
        

    def __linear_probeIns(self, item, searchkey):
        ''' Inserts an item in the first free place with index on or after
        the hash of the searchkey. '''
        if self.getTableSize() == self.getLength():
        # Can't insert if table is full
            return False
        i = 0
        while self.__table[self.__h(searchkey)+i].searchkey != None:
            i+=1
            if self.__h(searchkey)+i > self.__tableSize-1:
                i = 0 - self.__h(searchkey)
            if i == 0: 
            # This means we went full circle, so our hashmap is full
                return False
        self.__table[self.__h(searchkey)+i] = self.__item(item,searchkey)
        return True


    def __linear_probeRem(self, searchkey):
        ''' checks the higher positions in the table and removes the first
        item that equals the given searchkey. Rebuild afterwards. '''
        i = 0
        while self.__table[self.__h(searchkey)+i].searchkey != None:
            if self.__table[self.__h(searchkey)+i].searchkey == searchkey:
                self.__table[self.__h(searchkey)+i] = self.__item(None,None)
                self.rebuild()
                return True
            i+=1
            if self.__h(searchkey)+i >= self.__tableSize:
                i = 0 - self.__h(searchkey)
            if i == 0: 
            # This means we went full circle, so our hashmap is full
                return False
        return False
        

    def __linear_probeGet(self, searchkey):
        ''' gets an item that equals the given searchkey '''
        i = 0
        while self.__table[self.__h(searchkey)+i].searchkey != None:
            if self.__table[self.__h(searchkey)+i].searchkey == searchkey:
                return self.__table[self.__h(searchkey)+i].item
            i+=1
            if self.__h(searchkey)+i >= self.__tableSize-1:
                return False
        return False
   

    def __quadratic_probeIns(self, item, searchkey):
        ''' Insert an item to the table if the position
        is already taken the item will be placed to the
        next open place in quadratic steps. '''
        if self.getTableSize() == self.getLength():
        # Can't insert if table is full
            return False
        index = self.__h(searchkey)
        j = 1 # parameter for quadratic probing
        while self.__table[index].searchkey != None:
            index = (self.__h(searchkey) + j*j) % self.__tableSize
            j += 1
            if j > self.__tableSize:
                return False
        self.__table[index] = self.__item(item,searchkey)
        return True


    def __quadratic_probeRem(self, searchkey):
        ''' Removes the item with the given searchkey from the table
        going in square steps. '''
        index = self.__h(searchkey)
        j = 1 # parameter for quadratic probing
        while self.__table[self.__h(index)].searchkey != None:
            if self.__table[self.__h(index)].searchkey == searchkey:
                self.__table[self.__h(index)] = self.__item(None,None)
            i = (self.__h(searchkey) + j*j) % self.__tableSize
            j += 1
            if j > self.__tableSize-1:
                return False
        self.rebuild()
        return True



    def __quadratic_probeGet(self, searchkey):
        ''' Returns the item that equals the given searchkey going in aquare steps. '''
        index = self.__h(searchkey)
        j = 1 # parameter for quadratic probing
        while self.__table[self.__h(index)].searchkey != None:
            if self.__table[self.__h(index)].searchkey == searchkey:
                return self.__table[self.__h(index)].item
            i = (self.__h(searchkey) + j*j) % self.__tableSize
            j += 1
            if j > self.__tableSize-1:
                return False
        return False


    def __h(self, searchkey):
        ''' Calculates the position of the element with the given searchkey
        in the table the searchkey can be string or int.'''
        if type(searchkey) == type(''):
            tmp = 0
            for char in searchkey:
                tmp += ord(char)
            return tmp%self.__tableSize
        else:
            return searchkey%self.__tableSize


    def insert(self, item, searchkey):
        ''' insert an item to the table if the place is
        already occupied the insert method of the chosen
        probe type will be called.'''
        if self.__probeIns(item, searchkey):
            self.length += 1
            return True
        return False

    def getItem(self, searchkey):
        ''' Calls the get method of the given probe type. '''
        return self.__probeGet(searchkey)

    def destroy(self):
        ''' Empties the hashmap '''
        self.__tableSize = None
        self.__table = None
        self.__probeIns = None
        self.__probeRem = None
        self.__probeGet = None
        self.length = 0

    def traverse(self):
        ''' Returns a list of the items in the hashmap '''
        ret_list = []
        i = 0
        j = 0
        while i < self.getTableSize():
            item = self.__table[self.__h(i)]
            if isinstance(item, type(doubly_linked_chain.Doubly_linked_chain())):
                for di in item.traverse():
                    ret_list.append(di.searchkey)
            elif not item.searchkey == None:
                ret_list.append(item.searchkey)
            i+=1
        return ret_list

    def rebuild(self):
        ''' Rebuild the hashmap to fix compromised structure '''
        # redefining traverse: only difference is we return internal item
        # objects instead of the actual items (to have access to the key)
        def traverse(): 
            ''' Returns a list of the items in the hashmap '''
            ret_list = []
            i = 0
            j = 0
            while i < self.getTableSize():
                item = self.__table[self.__h(i)]
                if isinstance(item, type(doubly_linked_chain.Doubly_linked_chain())):
                    for di in item.traverse():
                        ret_list.append(di.searchkey)
                elif not item.searchkey == None:
                    ret_list.append(item)
                i+=1
            return ret_list
        contents = traverse()
        # Dropping table and resetting length
        self.__table = []
        for i in range(self.__tableSize):
            self.__table.append(self.__item(None, None))
        self.length = 0
        # inserting all our items again
        for item in contents:
            self.insert(item, item.searchkey)

    def rec_quadtraverse(self, j):
        ret_list = []
        while j < self.getTableSize():
            if not self.__table[self.__h(j)] == None:
                ret_list.append(self.__table[self.__h(j)].searchkey)   
            j = j**2
        return ret_list    

    def remove(self,searchkey):
        ''' removes the item with the given searchkey.
        If the place is occupied but doesn't equal the searchkey the 
        remove method of the given probe type will be called.'''
        success = False
        if isinstance(self.__table[self.__h(searchkey)], type(doubly_linked_chain.Doubly_linked_chain())):
            success = self.__probeRem(searchkey)
        elif self.__table[self.__h(searchkey)].searchkey == None:
            return False 
        else:
            success = self.__probeRem(searchkey)       
        if success:
            return True
        return False


    def isEmpty(self):
        ''' Returns true if the table is empty or false if not. '''
        if self.length == 0:
            return True
        else:
            return False


    def getTableSize(self):
        ''' Returns the table size. ''' 
        return self.__tableSize


    def getLength(self):
        ''' returns the number of elements in the table '''
        return self.length


    class __item:
        ''' a container for the items in the table'''
        def __init__(self, item, searchkey):
            self.item = item
            self.searchkey = searchkey
