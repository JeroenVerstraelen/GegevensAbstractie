class Node:
    """ represents a node in a tree """
    
    def __init__(self, key, data=None):
        self.key = key
        self.data = data

    def __str__(self):
        """ Returns the search key of the node. """
        return str(self.key)

    def __gt__(self, node):
        """ Compares the value of search keys. """
        if self.key > node:
            return True
        else:
            return False

    def __lt__(self, node):
        """ Compares the value of search keys. """
        if self.key < node:
            return True
        else:
            return False

    def getData(self):
        """ Returns the data in the node. """
        return self.data

    def setData(self, data):
        """ Sets the data """
        self.data = data

    def getKey(self):
        """ Returns the search key of the node. """
        return self.key

class BinTree:
    """ Represents the ADT binary tree """

    def __init__(self, root=None):
        """ Creates a binary tree. """
        self.root = root
        self.lefttree = None
        self.righttree = None

    def __str__(self):
        """ Returns a string with an ASCII image of the tree """
        if self.isEmpty():
            return "empty"
        structure = self.getstructure()
        item = structure.pop(0)
        height = self.getHeight()
        image = ""
        for i in range(height):
            spacing = 2 ** (height - i + 1)
            for j in range(2**i):
                if (item[0], item[1]) == (i + 1, j + 1):
                    image += str(item[2]).center(spacing)
                    if len(structure) == 0:
                        break
                    item = structure.pop(0)
                else:
                    image += "".center(spacing)
            image += "\n"
        return image

    def getRootData(self):
        """ Returns the data from the root. """
        if self.root:
            return self.root.getData()
        else:
            return False

    def setRootData(self, data):
        """ Sets the data in the root. """
        self.root.setData(data)

    def getstructure(self, level = 1, rank = 1):
        """ Returns a list of all the nodes with their level and rank within the tree. """
        if self.isEmpty():
            return []
        structure = [(level, rank, self.root.getKey())]
        level += 1
        rank = rank * 2
        if self.righttree != None:
            structure += self.righttree.getstructure(level, rank)
        rank -= 1
        if self.lefttree != None:
            structure += self.lefttree.getstructure(level, rank)
        structure.sort()
        return structure

    def search(self, searchkey):
        """ returns the subtree where the item with searchkey is in the root """
        if self.isEmpty():
            return False
        if self.root.getKey() == searchkey:
            return self
        if self.root > searchkey and self.lefttree != None:
            return self.lefttree.search(searchkey)
        if self.root < searchkey and self.righttree != None:
            return self.righttree.search(searchkey)
        return False

    def getData(self, searchkey):
        """ searches for a node with the given search key and returns its data """
        subtree = self.search(searchkey)
        if subtree:
            return subtree.root.getData()
        return False

    def getLeftSubtree(self):
        """ Returns the left subtree """
        return self.lefttree

    def getRightSubtree(self):
        """ Returns the right subtree """
        return self.righttree

    def attachLeftSubtree(self, subtree):
        """ attach the given subtree as out left subtree """
        self.lefttree = subtree

    def attachRightSubtree(self, subtree):
        """ attach the given subtree as out right subtree """
        self.righttree = subtree


    def contains(self, searchkey):
        """ Returns whether the tree contains an item with the given search key """
        if self.search(searchkey):
            return True
        return False

    def insert(self, searchkey, data=None):
        """ Inserts the given node. """
        node = Node(searchkey, data)
        if self.isEmpty():
            self.root = node 
        elif self.root.getKey() == searchkey:
            return False
        elif self.root > searchkey:
            if self.lefttree == None:
                self.lefttree = BinTree(node)
            else:
                self.lefttree.insert(searchkey, data)
        elif self.root < searchkey:
            if self.righttree == None:
                self.righttree = BinTree(node)
            else:
                self.righttree.insert(searchkey, data)
        return True

    def remove(self, searchkey):
        """ Removes the node with the given searchkey. """
        subtree = self.search(searchkey)
        if not subtree:
            return False
        # Three cases: we have no children, 1 child or 2 children
        # case with no children: clear subtree:
        if subtree.getHeight() == 1:
            subtree.clear()
            return True
        leftsubtree = subtree.getLeftSubtree()
        rightsubtree = subtree.getRightSubtree()
        # case with one child: overwrite self with child:       
        if leftsubtree and not rightsubtree:
            subtree.root = leftsubtree.root
            subtree.attachRightSubtree(leftsubtree.getRightSubtree())
            subtree.attachLeftSubtree(leftsubtree.getLeftSubtree())
            return True
        elif not leftsubtree:
            subtree.root = rightsubtree.root
            subtree.attachLeftSubtree(rightsubtree.getLeftSubtree())
            subtree.attachRightSubtree(rightsubtree.getRightSubtree())
            return True
        # case with two children: copy root from inorder successor and delete that node.
        successor = subtree.getSuccessor()
        subtree.root = successor.root
        successor.remove(successor.root.getKey()) #recursively deletes successor
        return True


    def getSuccessor(self):
        """ Returns the inorder successor of the root of the tree """
        if not self.getRightSubtree():
            return self
        subtree = self.getRightSubtree()
        while subtree.getLeftSubtree(): 
            subtree = subtree.getLeftSubtree()
        return subtree
        

    def clear(self):
        """ Removes all nodes, leaving the tree empty. """
        self.__init__()

    def inorder(self):
        if self.isEmpty():
            return []
        keylist = []
        if self.lefttree != None:
            keylist.extend((self.lefttree.inorder()))
        keylist.append(self.root.getKey())
        if self.righttree != None:
            keylist.extend((self.righttree.inorder()))
        return keylist

    def preorder(self):
        if self.isEmpty():
            return []
        keylist = []
        keylist.append(self.root.getKey())
        if self.lefttree != None:
            keylist.extend((self.lefttree.preorder()))
        if self.righttree != None:
            keylist.extend((self.righttree.preorder()))
        return keylist

    def postorder(self):
        if self.isEmpty():
            return []
        keylist = []
        if self.lefttree != None:
            keylist.extend((self.lefttree.postorder()))
        if self.righttree != None:
            keylist.extend((self.righttree.postorder()))
        keylist.append(self.root.getKey())
        return keylist


    def getHeight(self):
        """ Returns the height of the tree. """
        if self.isEmpty():
            return 0
        height = 1
        if self.lefttree != None:
            height += self.lefttree.getHeight()
        if self.righttree != None:
            height = max(height, self.righttree.getHeight() + 1)
        return height

    def isEmpty(self):
        """ Returns whether the tree is empty. """
        if self.root == None:
            return True
        return False

