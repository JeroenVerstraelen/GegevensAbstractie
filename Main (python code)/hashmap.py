import math
import doubly_linked_chain

class Hashmap:
    
    def __init__(self,size,probingType=0):
        '''This class is a hashtable, size is the
        wished size of the table it will be set to
        the next higher prime number. The probing type
        can be set to the following: 0 = seperate chaining,
        1  = linear probing, 2 = quadratic probing.
        If not specified otherwise the hashtable is set to seperate chaining.
        '''
        self.__tableSize = self.__getMapSize(size)
        self.__table = [self.__item(0, None)]
        for i in range(self.__tableSize-1):
            self.__table.append(self.__item(0, None))
        
        if probingType == 0:
            self.__probeIns = self.__seperate_chainIns
            self.__probeRem = self.__seperate_chainRem
            self.__probeGet = self.__seperate_chainGet
        elif probingType == 1:
            self.__probeIns = self.__linear_probeIns
            self.__probeRem = self.__linear_probeRem
            self.__probeGet = self.__linear_probeGet
        elif probingType == 2:
            self.__probeIns = self.__quadratic_probeIns
            self.__probeRem = self.__quadratic_probeRem
            self.__probeGet = self.__quadratic_probeGet

        self.__length = 0


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
            i+=1
        
        while not is_prime(i):
            i+=2;

        return i


    def __seperate_chainIns(self, item, searchkey):
        ''' insert an item into the given doubly linked
        chain if the given item isn't a linked chain yet
        a new linked chain will be created.'''
        if isinstance(self.__table[self.__h(searchkey)], type(doubly_linked_chain.Doubly_linked_chain())):
            self.__table[self.__h(searchkey)].insert(self.__item(item, searchkey), searchkey)
        else:
            
            temp = self.__table[self.__h(searchkey)]
            
            self.__table[self.__h(searchkey)] = doubly_linked_chain.Doubly_linked_chain()
            self.__table[self.__h(searchkey)].insert(temp, temp.searchkey)
            self.__table[self.__h(searchkey)].insert(self.__item(item, searchkey), searchkey)


    def __seperate_chainRem(self, searchkey):
        ''' Removes the item with the given searchkey from a
        linked chain if the chain only contains one item
        afterwards it will be turned into an item again. '''
        if isinstance(self.__table[self.__h(searchkey)], type(doubly_linked_chain.Doubly_linked_chain())):
            if self.__table[self.__h(searchkey)].length == 1:
                self.__table[self.__h(searchkey)] = 0
                return
            self.__table[self.__h(searchkey)].remove(searchkey)
            if self.__table[self.__h(searchkey)].length == 1:
                tmp = self.__table[self.__h(searchkey)].headPtr.next.item
                self.__table[self.__h(searchkey)] = tmp     
        else:
            self.__table[self.__h(searchkey)] = self.__item(0, None)


    def __seperate_chainGet(self, searchkey):
        ''' returns the item with the specified searchkey ''' 
        if isinstance(self.__table[self.__h(searchkey)], type(doubly_linked_chain.Doubly_linked_chain())):
            tmp = self.__table[self.__h(searchkey)].getNode(searchkey)
            if tmp == None:
                return -1
            else:
                return tmp.item.item
        else:
            return self.__table[self.__h(searchkey)].item
        

    def __linear_probeIns(self, item, searchkey):
        ''' Inserts an item in the next free place higher in the table. '''
        i = 1
        while self.__table[self.__h(searchkey)+i].searchkey != None:
            i+=1
            if self.__h(searchkey)+i > self.__tableSize-1:
                return -1
        self.__table[self.__h(searchkey)+i] = self.__item(item,searchkey)


    def __linear_probeRem(self, searchkey):
        ''' checks the higher positions in the table and removes the first
        item that equals the given searchkey. Closes the gap in the line aftwerwards. '''
        def getNext(self, searchkey, i):
            ''' get the next item in line that should be at the position hashed by the searchkey '''
            while self.__table[self.__h(searchkey)+i].searchkey != None:
                
                if self.__table[self.__h(searchkey)+i].searchkey == searchkey and self.__h(self.__table[self.__h(searchkey)+i].searchkey) == self.__h(searchkey):
                    i+=1
                    continue
                if self.__h(self.__table[self.__h(searchkey)+i].searchkey) == self.__h(searchkey):
                    return self.__table[self.__h(searchkey)+i]
                i+=1
                
            return -1


        i = 0
        while self.__table[self.__h(searchkey)+i].searchkey != None:
            if self.__table[self.__h(searchkey)+i].searchkey == searchkey:
                tmp = getNext(self,searchkey, i)
                if tmp == -1:
                    self.__table[self.__h(searchkey)+i] = self.__item(0,None)
                    return
                while tmp != -1:
                    self.__table[self.__h(searchkey)+i] = tmp
                    tmp = getNext(self, self.__table[self.__h(searchkey)+i].searchkey, i)
                    i+=1
                    if self.__h(searchkey)+i > self.__tableSize-1:
                        return -1
                self.__table[self.__h(searchkey)+i] = self.__item(0, None)
            i+=1


    def __linear_probeGet(self, searchkey):
        ''' gets an item that equals the given searchkey '''
        i = 0
        while self.__table[self.__h(searchkey)+i].searchkey != None:
            
            if self.__table[self.__h(searchkey)+i].searchkey == searchkey:
                return self.__table[self.__h(searchkey)+i].item
            i+=1
            if self.__h(searchkey)+i >= self.__tableSize-1:
                return -1
            
        return -1
   

    def __quadratic_probeIns(self, item, searchkey):
        ''' Insert an item to the table if the position
        is already taken the item will be placed to the
        next open place in quadratic steps. '''
        i = self.__h(searchkey)
        while self.__table[self.__h(i)].searchkey != None:
            i= i**2
            if self.__h(i) > self.__tableSize-1:
                return -1
        self.__table[self.__h(i)] = self.__item(item,searchkey)


    def __quadratic_probeRem(self, searchkey):
        ''' Removes the item with the given searchkey from the table
        going in square steps. '''
        def getNext(self, searchkey, i):
            while self.__table[self.__h(i)].searchkey != None:
                
                if self.__table[self.__h(i)].searchkey == searchkey and self.__h(self.__table[self.__h(i)].searchkey) == self.__h(searchkey):
                    i = i**2
                    continue
                if self.__h(self.__table[self.__h(i)].searchkey) == self.__h(searchkey):
                    return self.__table[self.__h(i)]
                i = i**2
                
            return -1

        
        i = self.__h(searchkey)
        while self.__table[self.__h(i)].searchkey != None:
            
            if self.__table[self.__h(i)].searchkey == searchkey:
                tmp = getNext(self,searchkey, i)
                if tmp == -1:
                    self.__table[self.__h(i)] = self.__item(0,None)
                    return
                while tmp != -1:
                    self.__table[self.__h(i)] = tmp
                    tmp = getNext(self, self.__table[self.__h(i)].searchkey, i)
                    i = i**2
                    if self.__h(i) > self.__tableSize-1:
                        return -1
                self.__table[self.__h(i)] = self.__item(0, None)
            i = i**2


    def __quadratic_probeGet(self, searchkey):
        ''' Returns the item that equals the given searchkey going in aquare steps. '''
        i = self.__h(searchkey)
        while self.__table[self.__h(i)].searchkey != None:
            
            if self.__table[self.__h(i)].searchkey == searchkey:
                return self.__table[self.__h(i)].item
            i = i**2
            if self.__h(i) >= self.__tableSize-1:
                return -1
        return -1


    def __h(self, searchkey):
        ''' Calculates the position of the element with the given searchkey in the
        table the searchkey can be string or int.'''
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
        if isinstance(self.__table[self.__h(searchkey)], type(doubly_linked_chain.Doubly_linked_chain())):
            self.__probeIns(item, searchkey)
        elif self.__table[self.__h(searchkey)].searchkey == None:
            self.__table[self.__h(searchkey)] = self.__item(item, searchkey)
        else:
            self.__probeIns(item, searchkey)
        self.__length += 1


    def getItem(self, searchkey):
        ''' Calls the get method of the given probe type. '''
        return self.__probeGet(searchkey)

    def destroy(self):
        self.__tableSize = None
        self.__table = None
        self.__probeIns = None
        self.__probeRem = None
        self.__probeGet = None
        self.__length = 0

    def traverse(self):
        ret_list = []
        i = 0
        j = 0
        while i < self.getTableSize():
            if not self.__table[self.__h(i)] == None:
                ret_list.append(self.__table[self.__h(i)].searchKey)
            ret_list.append(self.rec_quadtraverse(i**2))
        return ret_list

    def rec_quadtraverse(self, j):
        ret_list = []
        while j < self.getTableSize():
            if not self.__table[self.__h(j)] == None:
                ret_list.append(self.__table[self.__h(j)].searchKey)   
            j = j**2
        return ret_list    

    def remove(self,searchkey):
        ''' removes the item with the given searchkey.
        If the place is occupied but doesn't equal the
        searchkey the remove method of the given probe type will be called.'''
        if isinstance(self.__table[self.__h(searchkey)], type(doubly_linked_chain.Doubly_linked_chain())):
            self.__probeRem(searchkey)
        elif self.__table[self.__h(searchkey)].searchkey == None:
            return -1 
        elif self.__table[self.__h(searchkey)].searchkey == searchkey:
            self.__probeRem(searchkey)    
        else:
            self.__probeRem(searchkey)       
        self.__length -= 1


    def isEmpty(self):
        ''' Returns true if the table is empty or false if not. '''
        if self.__length == 0:
            return True
        else:
            return False


    def getTableSize(self):
        ''' Returns the table size. ''' 
        return self.__tableSize


    def getLength(self):
        ''' returns the number of elements in the table '''
        return self.__length


    class __item:
        ''' a container for the items in the table'''
        def __init__(self, item, searchkey):
            self.item = item
            self.searchkey = searchkey
