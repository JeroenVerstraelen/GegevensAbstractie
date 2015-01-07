class Redblacktree:            
    '''
    class for the red-black tree
    '''

    class redblacknode:            
        '''
        class for the node of a red-black tree
        '''
        def __init__(self,key):
            self.key = key
            self.red = False    #self.red holds the color of the connectino between the node and it's parent, and is initialized as black
            self.leftchild = None
            self.rightchild = None
            self.parent = None
        
        def __str__(self):        #returns a string representation for a node
            return str(self.key)
        
        def __repr__(self):
            return str(self.key)
    
        def create(self, key):        #initializes a node
            self.__init__(key)
    
        def destroy(self):        #destroys the node
            del(self)
    
        def isLeaf(self):        #returns True if the node is a leaf, otherwise returns False
            if self.rightchild == None and self.leftchild == None:
                return True
            else:
                return False
     
        def getParent(self):        #returns the parent of the node
            return self.parent
     
        def getRightChild(self):    #returns the right child of the node
            return self.rightchild
            
        def getLeftChild(self):        #returns the left child of the node
            return self.leftchild
            
        def preOrderTraversal(self, node=None):    #traverses and prints the tree in preorder
            ret_list = []
            if None != node.key and node != None:
                ret_list.append(node)
            if node.leftchild != None:
                ret_list.extend(node.leftchild.postOrderTraversal(node.leftchild))
            if node.rightchild != None:
                ret_list.extend(node.rightchild.postOrderTraversal(node.rightchild))
            return ret_list
        
        def postOrderTraversal(self, node=None):    #traverses and prints the tree in postorder
            ret_list = []
            if node.leftchild != None:
                ret_list.extend(node.leftchild.postOrderTraversal(node.leftchild))
            if node.rightchild != None:
                ret_list.extend(node.rightchild.postOrderTraversal(node.rightchild))
            if None != node.key and node != None:
                ret_list.append(node)
            return ret_list
           
        def inOrderTraversal(self, node=None):    #traverses and prints the tree in inorder
            ret_list = []
            if node.leftchild != None:
                ret_list.extend(node.leftchild.inOrderTraversal(node.leftchild))
            if None != node.key and node != None:
                ret_list.append(node)
            if node.rightchild != None:
                ret_list.extend(node.rightchild.inOrderTraversal(node.rightchild))
            return ret_list
     

    def __init__(self):
        self.dummy = redblacknode(None)#dummy node
        self.root = self.dummy    #upon initialisation of a tree, the dummy serves as the root
    
    def search(self,key,node=None):    
        '''
        searches for a value in the tree and returns the node if it's included in the tree, otherwise returns None
        can be called with a node to search only the subtrees of that node
        if no node is entered the default node is the root of the tree
        '''
        if None == node:
            node = self.root
        while node != self.dummy and key != node.key:    #search until the end of the tree or until the key is found
            if key < node.key:
                node = node.leftchild
            else:
                node = node.rightchild
        if node.key == key: return node    #only return the node if the keys match
        else: return None
    
    def insert(self,key,item):
        '''
        inserts an item in the tree and restores the properties of a red-black tree after
        '''
        the_node = redblacknode(key)    #initialize a node with the entered key
        helpingnode = self.dummy
        node = self.root
        while node != self.dummy:    #search for the node's place in the tree
            helpingnode = node    #helpingnode tracks the last visited node
            if the_node.key < node.key:
                node = node.leftchild
            else:
                node = node.rightchild
        the_node.parent = helpingnode    #the last visited node becomes the new node's parent
        if helpingnode == self.dummy:    #if the tree holds no nodes, the new node becomes the root
            self.root = the_node    
        elif the_node.key < helpingnode.key:    #otherwise, find out if the new node is the parents' left or right child
            helpingnode.leftchild = the_node
        else:
            helpingnode.rightchild = the_node
        the_node.leftchild = self.dummy    #the new node becomes a leaf
        the_node.rightchild = self.dummy
        the_node.red = True        #the new connection is initialized as red for convenience in the restoreproperties procedure
        self.restoreproperties(the_node)

    def delete(self,key):
        '''
        deletes a node from the tree
        if the entered key doesn't exist in the red-black tree, returns an error
        '''
        the_node = self.search(key)    #search for the node that matches the key
        if the_node == None:        #error if the node doesn't exist
            print("error: the node to delete doesn't exist")
            return
        helpingnode = self.dummy
        node = the_node
        if node.rightchild == self.dummy:#if the node does not have an inOrder succesor it can easily be deleted by connecting the left child to the parent, if the node doesn't have a left child self.dummy will be linked, so there are no special cases for this
            if node == node.parent.rightchild:    #find out if the node is its' parent's left or right child, link the left child, and delete the node
                node.parent.rightchild = node.leftchild
                del(the_node)
            elif node == node.parent.leftchild:
                node.parent.leftchild = node.leftchild
                del(the_node)
        else:
            while node.rightchild != self.dummy:    #if the node has an inOrder succesor, find it
                node = node.rightchild
            if node == node.parent.rightchild:    #find out if the succesor is its' parent's left or right child and link the left child
                node.parent.rightchild = node.leftchild
            elif node == node.parent.leftchild:
                node.parent.leftchild = node.leftchild
            if the_node == the_node.parent.rightchild:#replace the_node with it's successor in the parent
                the_node.parent.rightchild = node
            elif the_node == the_node.parent.leftchild:
                the_node.parent.leftchild = node
            node.leftchild = the_node.leftchild    #replace the_node with it's successor
            node.rightchild = the_node.rightchild
            node.parent = the_node.parent
            del(the_node)            #destroy the_node

    def restoreproperties(self,the_node):    
        '''
        restores the properties of a red-black tree through rotations
        '''
        while the_node.parent.red:    #if the parent's connection is red, changes should be made.
            if the_node.parent == the_node.parent.parent.leftchild: #find out what side of the parent's parent the parent is linked to.*
                helpingnode = the_node.parent.parent.rightchild
                if helpingnode.red:    #if this connection is also red, execute the appropriate changes in the connections**
                    the_node.parent.red = False
                    helpingnode.red = False
                    the_node.parent.parent.red = True
                    the_node = the_node.parent.parent
                else:            #if this connection is not red, a rotation should be executed***
                    if the_node == the_node.parent.rightchild:
                        the_node = the_node.parent
                        self.left_rotate(the_node.parent.parent)
                    the_node.parent.red = False
                    the_node.parent.parent.red = True
                    self.right_rotate(the_node.parent.parent)
            else:                            #*
                helpingnode = the_node.parent.parent.leftchild
                if helpingnode.red:    #**
                    the_node.parent.red = False
                    helpingnode.red = False
                    the_node.parent.parent.red = True
                    the_node = the_node.parent.parent
                else:            #***
                    if the_node == the_node.parent.leftchild:
                        the_node = the_node.parent
                        self.right_rotate(the_node)
                    the_node.parent.red = False
                    the_node.parent.parent.red = True
                    self.left_rotate(the_node.parent.parent)
        self.root.red = False
    
    def left_rotate(self, the_node):    
        '''
        subprocedure for restoreproperties
        '''
        helpingnode = the_node.rightchild
        the_node.rightchild = helpingnode.leftchild
        if helpingnode.leftchild != self.dummy and helpingnode.leftchild != None:
            helpingnode.leftchild.parent = the_node
        helpingnode.parent = the_node.parent
        if the_node.parent == self.dummy:
            self.root = helpingnode
        elif the_node == the_node.parent.leftchild:
            the_node.parent.leftchild = helpingnode
        else:
            the_node.parent.rightchild = helpingnode
        helpingnode.leftchild = the_node
        the_node.parent = helpingnode

    def right_rotate(self, the_node):    
        '''
        subprocedure for restoreproperties
        '''
        helpingnode = the_node.leftchild
        the_node.leftchild = helpingnode.rightchild
        if helpingnode.rightchild != self.dummy:
            helpingnode.rightchild.parent = the_node
        helpingnode.parent = the_node.parent
        if the_node.parent == self.dummy:
            self.root = helpingnode
        elif the_node == the_node.parent.rightchild:
            the_node.parent.rightchild = helpingnode
        else:
            the_node.parent.leftchild = helpingnode        
        helpingnode.rightchild = the_node
        the_node.parent = helpingnode
                
    def createTree(self):         #creates a red-black tree
        pass

    def destroyTree(self):            #destroys the tree
        del(self)

    def getLength(self):
        list = self.inOrderTraversal()
        length = len(list)
        if length == 1 and list[0].key == None:
            return 0
        return length

    def isEmpty(self):
        if self.getLength() == 0:
            return True
        return False
    
    def preOrderTraversal(self, node=None):    #traverses and prints the tree in preorder
        ret_list = []
        if None == node:
            node = self.root
        ret_list.append(node)
        if node.leftchild != None:
            ret_list.extend(node.leftchild.preOrderTraversal(node.leftchild))
        if node.rightchild != None:
            ret_list.extend(node.rightchild.preOrderTraversal(node.rightchild))
        return ret_list

    def postOrderTraversal(self, node=None):    #traverses and prints the tree in postorder
        ret_list = []
        if None == node:
            node = self.root
        if node.leftchild != None:
            ret_list.extend(node.leftchild.postOrderTraversal(node.leftchild))
        if node.rightchild != None:
            ret_list.extend(node.rightchild.postOrderTraversal(node.rightchild))
        ret_list.append(node)
        return ret_list
    
    def inOrderTraversal(self, node=None):    #traverses and prints the tree in inorder
        ret_list = []
        if None == node:
            node = self.root
        if node.leftchild != None:
            ret_list.extend(node.leftchild.inOrderTraversal(node.leftchild))
        ret_list.append(node)
        if node.rightchild != None:
            ret_list.extend(node.rightchild.inOrderTraversal(node.rightchild))
        return ret_list
