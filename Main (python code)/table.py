from binarytree import *
from doubly_linked_chain import *

from hashmap import *
from redblack_tree import *
from tree_234 import *
from twothreetree import * 


class Table:

    def __init__(self):
        self.implementation = "binaryTree"
        self.pointer = None
        
    def setImplementation(self, implementation):
        self.implementation = implementation

    def createTable(self):
        if self.implementation == "binaryTree":
            self.pointer = BinTree()
        elif self.implementation == "doublylinkedchain":
            self.pointer = Doubly_linked_chain()
        elif self.implementation == "hashmap":
            self.pointer = Hashmap(10000)
        elif self.implementation == "redBlackTree":
            self.pointer = Redblacktree()
        elif self.implementation == "234Tree":
            self.pointer = Tree234()
        elif self.implementation == "23Tree":
            self.pointer = TwoThreeTree()

    def destroyTable(self):
        if (self.implementation == "binaryTree" or
           self.implementation == "doublylinkedchain"):
            self.pointer.clear()
        elif self.implementation == "hashmap":
            self.pointer.destroy()
        elif (self.implementation == "redBlackTree" or
              self.implementation == "234Tree" or
              self.implementation == "23Tree"):
            self.pointer.destroyTree()

    def tableIsEmpty(self):
        return self.pointer.isEmpty()  

    def tableLength(self):
        if self.implementation == "binaryTree":
            return len(self.pointer.inorder())
        elif self.implementation == "doublylinkedchain":
            return self.pointer.getLength()
        elif self.implementation == "hashmap":
            return self.pointer.getLength()
        elif self.implementation == "redBlackTree":
            return self.pointer.getLength()
        elif self.implementation == "234Tree":
            return self.pointer.getLength()
        elif self.implementation == "23Tree":
            return self.pointer.treeLength()

    def tableInsert(self, newItem):
        if self.implementation == "23Tree" or self.implementation == "234Tree":
            return self.pointer.insert(newItem)
        return self.pointer.insert(newItem, newItem)

    def tableDelete(self, searchKey):
        if self.implementation == "binaryTree":
            return self.pointer.remove(searchKey)
        elif self.implementation == "doublylinkedchain":
            return self.pointer.remove(searchKey)
        elif self.implementation == "hashmap":
            return self.pointer.remove(searchKey)
        elif self.implementation == "redBlackTree":
            return self.pointer.delete(searchKey)
        elif self.implementation == "234Tree":
            return self.pointer.delete(searchKey)
        elif self.implementation == "23Tree":
            return self.pointer.deleteItem(searchKey)

    def tableRetrieve(self, searchKey):
        if self.implementation == "binaryTree":
            return self.pointer.getData(searchKey)
        elif self.implementation == "doublylinkedchain":
            return self.pointer.getItem(searchKey)
        elif self.implementation == "hashmap":
            return self.pointer.getItem(searchKey)
        elif self.implementation == "redBlackTree":
            return self.pointer.search(searchKey)
        elif self.implementation == "234Tree":
            return self.pointer.retrieve(searchKey)
        elif self.implementation == "23Tree":
            return self.pointer.retrieveItem(searchKey)

    def traverseTable(self):
        if self.implementation == "binaryTree":
            return self.pointer.inorder()
        elif self.implementation == "redBlackTree":
            return self.pointer.inOrderTraversal()
        else:
            return self.pointer.traverse()

    def sortObjectList(self, olist, getter):
        ''' this function takes lists of objects and getter methodes to sort the
            objects by different properties '''
        def quicksort(lst):
            if len(lst) < 2:
                return lst
            pivotindex = int((len(lst) - 1)/2)
            newpivotindex = int((len(lst) - 1)/2)
            pivot = lst[pivotindex]
            for i in range(pivotindex - 1, -1, -1):
                if lst[i] >= pivot:
                    lst.insert(newpivotindex, lst.pop(i))
                    newpivotindex -= 1
            for i in range(pivotindex + 1, len(lst)):
                if lst[i] <= pivot:
                    lst.insert(newpivotindex, lst.pop(i))
                    newpivotindex += 1
            leftlist = quicksort(lst[0:newpivotindex])
            leftlist.append(pivot)
            rightlist = quicksort(lst[newpivotindex + 1:len(lst)])
            lst = leftlist + rightlist
            return lst
        templist = []
        for obj in olist:
            templist.append((getter(obj), obj))
        sortedlist = quicksort(templist)
        resultlist = []
        for item in sortedlist:
            resultlist.append(item[1])
        return resultlist
    
        

