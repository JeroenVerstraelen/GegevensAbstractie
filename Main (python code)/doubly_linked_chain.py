class Doubly_linked_chain:
    ''' A chain of containers linked together by pointers without order. '''

        
    class node:
        ''' A container with two pointers one pointing to the previous one pointing to the next element.
            A new node is created by giving it an an item and the two links.
            Example: node(previous Node, item, next node)
            The searchkey for a node is its item if its a single value or its first object if it's a list.'''
        def __init__(self, prevNode, nextNode, searchKey = None, item = None):
            self.next = nextNode
            self.prev = prevNode
            if item == None:
                item = searchKey
            self.item = item
            self.searchKey = searchKey
                
    
    def __init__(self):
        dummy_head_node = self.node(None,None) #a dummy head Node to prevent the special case of inserting at the head.
        dummy_head_node.next = dummy_head_node
        dummy_head_node.prev = dummy_head_node
        self.headPtr = dummy_head_node
        self.length = 0

    def insert(self, searchkey, item = None):
        ''' Adds an item to the front of the chain after the dummy head node.'''
        dummyHeadNode = self.headPtr
        nextNode = dummyHeadNode.next
        if searchkey == None:
            return False
        newNode = self.node(dummyHeadNode, dummyHeadNode.next, searchkey, item)
        dummyHeadNode.next = newNode
        nextNode.prev = newNode
        self.length +=1
        return True


    def remove(self,searchKey):
        ''' Removes the first node with the given searchkey from the chain.
            The method returns True if it was successfull or False if not.
        '''
        node = self.getNode(searchKey)
        if not node:
            return False
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.length -=1
        return True


    def clear(self):
        ''' Removes all the nodes from the chain except for the dummy head node. '''
        dummyHeadNode = self.headPtr
        dummyHeadNode.next = dummyHeadNode
        dummyHeadNode.prev = dummyHeadNode
        

    def getNode(self,searchKey):
        ''' Returns the first node found with the given searchkey.'''
        if searchKey == None:
            return False
        tmpNode = self.headPtr.next
        while tmpNode.searchKey != None:
            if tmpNode.searchKey == searchKey:
                return tmpNode
            tmpNode = tmpNode.next
        return False

    def getItem(self, searchKey):
        ''' Returns the first item found with the given searchkey. '''
        node = self.getNode(searchKey)
        if node:
            return node.item
        return False

    def getLength(self):
        return self.length

    def isEmpty(self):
        ''' Returns True if the chain is empty or false if not. '''
        if self.headPtr == self.headPtr.next:
            return True
        return False

    def traverse(self):
        ''' returns a list of all the items in the chain '''
        tmpList = []
        tmpNode = self.headPtr.next
        while tmpNode.searchKey != None:
            tmpList.append(tmpNode.searchKey)
            tmpNode = tmpNode.next
        return tmpList[::-1]

