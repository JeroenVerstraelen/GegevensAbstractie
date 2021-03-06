from twothreetree import *

tree1 = TwoThreeTree()
#tree1.create()
tree1.insert(5)
tree1.insert(7)
tree1.insert(4)
tree1.insert(9)
tree1.insert(2)
tree1.insert(25)
tree1.insert(1)
tree1.insert(3)
print("Retrieve 3: ", tree1.retrieveItem(3))
print("Traverse: "+str(tree1.traverse()))

print("Height: " + str(tree1.treeLength()))

tree1.deleteItem(7)
tree1.deleteItem(5)
tree1.deleteItem(9)
tree1.deleteItem(3)
tree1.deleteItem(4)
tree1.deleteItem(2)
tree1.deleteItem(1)
tree1.deleteItem(5)


print("Height: " + str(tree1.treeLength()))
print("Traverse: "+str(tree1.traverse()))


tree1.insert(60)
tree1.insert(72)
tree1.insert(28)
tree1.insert(30)
tree1.insert(42)
tree1.insert(61)
tree1.insert(59)
tree1.insert(22)
print("Height: " + str(tree1.treeLength()))
print("Traverse: "+str(tree1.traverse()))
tree1.deleteItem(42)
tree1.deleteItem(61)
tree1.deleteItem(59)
tree1.deleteItem(22)
tree1.deleteItem(30)
tree1.deleteItem(28)
tree1.deleteItem(72)
tree1.deleteItem(60)

print("Height: " + str(tree1.treeLength()))
print("Traverse: "+str(tree1.traverse()))
