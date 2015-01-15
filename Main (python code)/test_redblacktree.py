# Some basic tests to verify the functionality of the 234-tree

import time
import redblack_tree 

# collection of some generic checks
def checks(tree):
    print("traversing. first inorder, then preorder, then postorder.")
    print(tree.inOrderTraversal())
    print(tree.preOrderTraversal())
    print(tree.postOrderTraversal())
    print("Is the tree empty? ",tree.isEmpty())

print("creating tree")
tree = redblack_tree.Redblacktree()

print("running checks on empty tree:")
checks(tree)
print("trying to retrieve 'nul': ",tree.search("nul"))
print("trying to retrieve 'zeven': ",tree.search("zeven"))


tree.createTree() # no effect
tree.destroyTree() # makes the tree empty. since it is empty, should have no effect

print("\ninserting items 'een' to 'eenentwintig'")
tree.insert(1,"een")
tree.insert(2,"twee")
tree.insert(3,"drie")
tree.insert(4,"vier")
tree.insert(5,"vijf")
tree.insert(6,"zes")
tree.insert(7,"zeven")
tree.insert(8,"acht")
tree.insert(9,"negen")
tree.insert(10,"tien")
tree.insert(11,"elf")
tree.insert(12,"twaalf")
tree.insert(13,"dertien")
tree.insert(14,"veertien")
tree.insert(15,"vijftien")
tree.insert(16,"zestien")
tree.insert(17,"zeventien")
tree.insert(18,"achttien")
tree.insert(19,"negentien")
tree.insert(20,"twintig")
tree.insert(21,"eenentwintig")

print("running checks on tree with items 'een' to 'eenentwintig':")
checks(tree)
print("trying to retrieve 0: ",tree.search(0))
print("trying to retrieve 7: ",tree.search(7))


print("\ndeleting items 1 to 21")
tree.delete(1)
tree.delete(2)
tree.delete(3)
tree.delete(4)
tree.delete(5)
tree.delete(6)
tree.delete(7)
tree.delete(8)
tree.delete(9)
tree.delete(10)
tree.delete(11)
tree.delete(12)
tree.delete(13)
tree.delete(14)
tree.delete(15)
tree.delete(16)
tree.delete(17)
tree.delete(18)
tree.delete(19)
tree.delete(20)
tree.delete(21)

print("running checks on tree with all the items deleted from it:")
checks(tree)
print("trying to retrieve 0: ",tree.search(0))
print("trying to retrieve 7: ",tree.search(7))


input("we're going to load a large amount of data now... Press enter to continue")

start_time = time.time()
for i in range(100000):
    tree.insert(i,i)
print("running checks on tree with 100.000 items:")
checks(tree)
print("adding items took ", time.time() - start_time, " seconds.")
print("trying to retrieve 0: ",tree.search(0))
print("trying to retrieve 55555: ",tree.search(55555))










