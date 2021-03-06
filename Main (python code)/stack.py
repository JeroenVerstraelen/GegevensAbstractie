class Stack:
    '''
     Represents a Stack.
 
    Instance variables:
        self.stack = 0/[]

    Instance methods:
        createStack(self)
        destroyStack(self)
        isEmpty(self)
        push(self, newItem)
        pop(self)
        pop_r(self)
        getTop(self)
    '''

    class Node:
        ''' Represents a node in the stack.

        Used for linking and as a container.

        Instance variables:
            self.value    The data contained by this Node.
            self.links    Array with static size 2, represents
                          respectively the lower and upper linked
                          Nodes of self.
        '''
   
        def __init__(self, val=None, links=[None, None]):
            self.value = val
            self.links = links

        def push(self, value):
            ''' Pushes a node with 'value' on top of this Node. '''
            self.links[1] = Stack.Node(value, [self, None])      # Set the new Node as upper link of self.
            return self.links[1]                                 # Return the new Node.

        def pop(self):
            ''' Removes the Node above this Node and returns its value. '''
            prevNode = self.links[0]   
            if prevNode:                     
                prevNode.links[1] = None
            return prevNode

        def getLinks(self):
            ''' Returns an array linking to the lower and upper Node. '''
            return self.links

        def getValue(self):
            ''' Returns the value contained by this Node. '''
            return self.value

    def __init__(self):
        self.top = None

    def createStack(self):
        ''' Empty function to follow contract. '''
        pass

    def destroyStack(self):
        '''Destroys the Stack.'''
        self.top = None

    def isEmpty(self):
        '''Checks if the Stack is Empty.'''
        if self.top:
            return False
        return True

    def push(self, newItem):
        '''Pushes newItem on top of the Stack.'''
        if self.top:        
            self.top = self.top.push(newItem)
        else:
            self.top = Stack.Node(newItem)
        return True

    def pop(self):
        '''Deletes the item on the top of the Stack.'''
        if self.isEmpty() == False:
            self.top = self.top.pop() 
            return True
        return False

    def pop_r(self):
        '''Deletes the item on the top of the Stack and returns it.'''
        if self.top:
            value = self.top.getValue()
            self.top.pop().getValue()
            return value
        return None

    def getTop(self):
        '''Gets the top of the stack and returns it.'''
        return self.top.getValue()