# Some basic tests to verify the functionality of the 234-tree

import time
import tree_234

# collection of some generic checks
def checks(tree):
    print("traversing. first inorder, then preorder, then postorder.")
    print(tree.traverse())
    print(tree.traverse("preorder"))
    print(tree.traverse("postorder"))
    print("Is the tree empty? ",tree.isEmpty())

print("creating tree")
tree = tree_234.Tree234()

print("running checks on empty tree:")
checks(tree)
print("trying to retrieve 'nul': ",tree.retrieve("nul"))
print("trying to retrieve 'zeven': ",tree.retrieve("zeven"))


tree.createTree() # no effect
tree.destroyTree() # makes the tree empty. since it is empty, should have no effect

print("\ninserting items 'een' to 'eenentwintig'")
tree.insert("een")
tree.insert("twee")
tree.insert("drie")
tree.insert("vier")
tree.insert("vijf")
tree.insert("zes")
tree.insert("zeven")
tree.insert("acht")
tree.insert("negen")
tree.insert("tien")
tree.insert("elf")
tree.insert("twaalf")
tree.insert("dertien")
tree.insert("veertien")
tree.insert("vijftien")
tree.insert("zestien")
tree.insert("zeventien")
tree.insert("achttien")
tree.insert("negentien")
tree.insert("twintig")
tree.insert("eenentwintig")

print("running checks on tree with items 'een' to 'eenentwintig':")
checks(tree)
print("trying to retrieve 'nul': ",tree.retrieve("nul"))
print("trying to retrieve 'zeven': ",tree.retrieve("zeven"))


print("\ndeleting items 'een' to 'eenentwintig'")
tree.delete("een")
tree.delete("twee")
tree.delete("drie")
tree.delete("vier")
tree.delete("vijf")
tree.delete("zes")
tree.delete("zeven")
tree.delete("acht")
tree.delete("negen")
tree.delete("tien")
tree.delete("elf")
tree.delete("twaalf")
tree.delete("dertien")
tree.delete("veertien")
tree.delete("vijftien")
tree.delete("zestien")
tree.delete("zeventien")
tree.delete("achttien")
tree.delete("negentien")
tree.delete("twintig")
tree.delete("eenentwintig")

print("running checks on tree with all the items deleted from it:")
checks(tree)
print("trying to retrieve 'nul': ",tree.retrieve("nul"))
print("trying to retrieve 'zeven': ",tree.retrieve("zeven"))


input("we're going to load a large amount of data now... Press enter to continue")

start_time = time.time()
for i in range(100000):
    tree.insert(i)
print("running checks on tree with 100.000 items:")
checks(tree)
print("adding items took ", time.time() - start_time, " seconds.")
print("trying to retrieve 0: ",tree.retrieve(0))
print("trying to retrieve 55555: ",tree.retrieve(55555))










