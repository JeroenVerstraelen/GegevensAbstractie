class Tree234:
    ''' Represents a 234 tree '''

    # Node class for the nodes of the tree.
    # items, children and parent can be passed in as arguments. The class will
    # NOT check whether the right amount was passed in, so be careful not to
    # create an invalid node!
    class Node:
        ''' represents a node in a 234 tree '''
        def __init__(self, i1 = None, i2 = None, i3 = None,
                    c1 = None, c2 = None, c3 = None, c4 = None, parent = None):
            self.items = []
            self.children = []
            self.parent = parent
            # loop through items and add them if present
            for i in [i1, i2, i3]:
                if i:
                    self.items.append(i)
            # loop through items and add them if present
            for c in [c1, c2, c3, c4]:
                if c:
                    self.children.append(c)
            self.items.sort() # Put items in order
            self.children.sort() # Put children in order

        def __lt__(self, node):
            ''' Compare nodes -> compare first data item '''
            if self.items[0] < node:
                return True
            return False

        def __gt__(self, node):
            ''' Compare nodes -> compare first data item '''
            if self.items[0] > node:
                return True
            return False

        def __eq__(self, node):
            ''' Compare nodes -> compare first data item '''
            if self.items[0] == node:
                return True
            return False

        def contains(self, item):
            ''' checks whether item is present in this node. returns boolean '''
            for i in self.items:
                if i == item:
                    return True
            return False

        def addi(self, item):
            ''' add an item to the node '''
            self.items.append(item)
            self.items.sort()

        def remi(self, item):
            ''' remove an item from the node '''
            self.items.remove(item)
            self.items.sort()

        def addc(self, child):
            ''' add a child to the node '''
            self.children.append(child)
            child.setParent(self)
            self.children.sort()

        def remc(self, child):
            ''' remove a child from the node '''
            self.children.remove(child)
            self.children.sort()

        def setParent(self, parent):
            ''' set the parent of the node '''
            self.parent = parent

        def isEmpty(self):
            ''' Returns True if no items or children are present. '''
            if len(self.children) == 0 == len(self.items):
                return True
            return False

        def isLeaf(self):
            ''' Returns whether the node is a leaf node or not '''
            if len(self.children) == 0:
                return True
            return False

        def size(self):
            ''' Returns number of items in the node '''
            return len(self.items)

        def path(self, item):
            ''' returns next node on path to item or successor, False if leaf'''
            if self.isLeaf(): return False
            for i in range(self.size()):
                if item < self.items[i]: # return left child if item is smaller
                    return self.children[i]
            return self.children[-1] # end reached: return last child
            


    def __init__(self):
        ''' start with an empty root node '''
        self.node = Tree234.Node()

    def createTree(self):
        ''' method exists for completeness' sake; does nothing '''
        pass

    def destroyTree(self):
        ''' makes tree empty '''
        self.node = Tree234.Node()

    def isEmpty(self):
        ''' returns boolean indicating whether tree is empty '''
        if self.node.isEmpty():
            return True
        return False

    def getHeight(self):
        ''' Calculate and return the current height of the tree '''
        def height(node):
            ''' recursive function that traverses nodes to get height '''
            if node.isEmpty():
                return 0
            tmpheight = 1
            for child in node.children:
                tmpheight = max(tmpheight, height(child) + 1)
            return tmpheight
        return height(self.node)

    def getLength(self):
        list = self.traverse()
        length = len(self.traverse())
        if length == 1 and list[0].items == [None, None, None]:
            return 0
        return length

       
    def insert(self, item):
        ''' Insert an item in the tree at the appropriate place '''
        # first check if an item with same searchkey is present. return False if this is the case.
        if self.retrieve(item):
            return False
        # defining a function to split nodes:
        def split(node):
            ''' Splits a tree-node into two one-nodes '''
            node1 = Tree234.Node(parent = node.parent)
            node2 = Tree234.Node(parent = node.parent)
            node1.addi(node.items[0])
            node.parent.addi(node.items[1])
            node2.addi(node.items[2])
            if not node.isLeaf():
                node1.addc(node.children[0])
                node1.addc(node.children[1])
                node2.addc(node.children[2])
                node2.addc(node.children[3])
            node.parent.remc(node)
            node.parent.addc(node1)
            node.parent.addc(node2)
        # special case: root needs to be split
        if self.node.size() == 3:
            newrootnode = Tree234.Node()
            oldrootnode = self.node
            self.node.setParent(newrootnode)
            self.node = newrootnode
            newrootnode.addc(oldrootnode)
            split(oldrootnode)
        currentnode = self.node
        while not currentnode.isLeaf():
            # find correct child in path
            childnode = currentnode.path(item)
            # split child if needed and find new correct child
            if childnode.size() == 3:
                split(childnode)
                childnode = currentnode.path(item)
            # set current node to child
            currentnode = childnode
        currentnode.addi(item)
        return True
       
    def delete(self, searchKey):
        ''' deletes the node with the given search key from the tree '''
        # The fix function transforms a two-node in a three-node with the
        # help of a rotate or merge
        def fix(node):
            ''' fixes a 2-node to prepare for a deletion '''
            # The merge function is called in the fix function and operates
            # on the variables of that function.
            def merge(node, direction): # left = -1, right = 0
                ''' merges node, sibling and parent item in given 
                    direction '''
                mergednode = Tree234.Node(parent = parent)
                mergednode.addi(node.items[0])
                mergednode.addi(sibling.items[0])
                mergednode.addi(parent.items[index + direction])
                if not node.isLeaf():
                    mergednode.addc(node.children[0])
                    mergednode.addc(node.children[1])
                    mergednode.addc(sibling.children[0])
                    mergednode.addc(sibling.children[1])
                parent.remi(parent.items[index + direction])
                parent.remc(node)
                parent.remc(sibling)
                parent.addc(mergednode)
                return mergednode
            # The rotate function is called in the fix function and operates
            # on the variables of that function.
            def rotate(node, direction): # clockwise = -1, counter = 0
                ''' rotates an element from sibling towards node via parent
                    item in given direction '''
                node.addi(parent.items[index + direction])
                parent.remi(parent.items[index + direction])
                parent.addi(sibling.items[direction])
                sibling.remi(sibling.items[direction])
                if not node.isLeaf():
                    node.addc(sibling.children[direction])
                    sibling.remc(sibling.children[direction])
 
            parent = node.parent
            index = parent.children.index(node)
            sibling = None
            if index > 0:
                sibling = parent.children[index - 1]
                if sibling.size() > 1:
                    # rotate from the left
                    rotate(node, -1)
                    return node
            if index + 1 < parent.size():
                sibling = parent.children[index + 1]
                if sibling.size() > 1:
                    # rotate from the right
                    rotate(node, 0)
                    return node
            # All neighbour siblings are 2-nodes, merge with sibling
            if index > 0:
                # merge with left sibling
                sibling = parent.children[index - 1]
                node = merge(node, -1) # item in parent has index of node -1
                return node
            else:
                # merge with right sibling
                sibling = parent.children[index + 1]
                node = merge(node, 0) # item in parent has same index as node
                return node
            # if somehow none of our cases were true; return false
            return False

        currentnode = self.node
        # first: special case for the root node: if the root and both its
        # siblings are two-nodes we merge them
        if currentnode.size() == 1 and not currentnode.isLeaf():
            child0 = currentnode.children[0]
            child1 = currentnode.children[1]
            if (child0.size() == 1 and child1.size() == 1):
                currentnode.addi(child0.items[0])
                currentnode.addi(child1.items[0])
                currentnode.remc(child0)
                currentnode.remc(child1)
                if not child0.isLeaf():
                    currentnode.addc(child0.children[0])
                    currentnode.addc(child0.children[1])
                    currentnode.addc(child1.children[0])
                    currentnode.addc(child1.children[1])
        # second special case: the root node and its successor are both
        # 2-nodes, but the sibling is not: we rotate.
        if currentnode.size() == 1 and not currentnode.isLeaf():
            childnode = currentnode.path(searchKey)
            if childnode.size() == 1:
                # determine direction
                if childnode < currentnode: # child is to the left
                    sibling = currentnode.children[1]
                    index = 0
                else: # child is to the right
                    sibling = currentnode.children[0]
                    index = -1
                childnode.addi(currentnode.items[0])
                currentnode.items[0] = sibling.items[index]
                sibling.remi(currentnode.items[0])
                if not childnode.isLeaf():
                    childnode.addc(sibling.children[index])
                    sibling.remc(sibling.children[index])
        while not currentnode.isLeaf():
            if currentnode.contains(searchKey):
                itemnode = currentnode
            childnode = currentnode.path(searchKey)
            if childnode.size() == 1:
                childnode = fix(childnode)
            currentnode = childnode
        if currentnode.contains(searchKey):
            currentnode.remi(searchKey)
            return True
        for item in currentnode.items:
            if item > searchKey:
                successor = item
                break
        currentnode.remi(successor)
        itemnode.remi(searchKey)
        itemnode.addi(successor)

    def traverse(self, visit = "inorder"):
        ''' returns a list of the items in the tree traversed in given order
            "inorder", "preorder" or "postorder". default inorder '''
        itemlist = []
        def inorder(node):
            ''' recursively fills itemlist with items inorder '''
            if node.isLeaf():
                itemlist.extend(node.items)
            else:
                for i in range(node.size()):
                    inorder(node.children[i])
                    itemlist.append(node.items[i])
                inorder(node.children[-1])
        def preorder(node):
            ''' recursively fills itemlist with items preorder '''
            itemlist.extend(node.items)
            if not node.isLeaf():
                for child in node.children:
                    preorder(child)
        def postorder(node):
            ''' recursively fills itemlist with items postorder '''
            if not node.isLeaf():
                for child in node.children:
                    postorder(child)
            itemlist.extend(node.items)
        if visit == "preorder":
            preorder(self.node)
        elif visit == "postorder":
            postorder(self.node)
        else:
            inorder(self.node)
        return itemlist

    def retrieve(self, searchKey):
        ''' returns the item with given searchKey, False if not found '''
        currentnode = self.node # start in the root node
        while True:
            if currentnode.contains(searchKey):
                return currentnode.items[currentnode.items.index(searchKey)]
            if currentnode.isLeaf(): # We're at the bottom without result
                return False
            currentnode = currentnode.path(searchKey) # get next node
