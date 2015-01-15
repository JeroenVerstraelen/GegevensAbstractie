# Tests for the hashmap implementation according to the contract by Nico Beyer

# import the classes to test
import hashmap # change if needed

# function to add a collection of items to a hashmap
def additems(map0):
    print("Adding items 1 through 20, 1000 and 99999999999999999999")
    map0.insert("one",1)
    map0.insert("two",2)
    map0.insert("three",3)
    map0.insert("four",4)
    map0.insert("five",5)
    map0.insert("six",6)
    map0.insert("seven",7)
    map0.insert("eight",8)
    map0.insert("nine",9)
    map0.insert("ten",10)
    map0.insert("eleven",11)
    map0.insert("twelve",12)
    map0.insert("thirteen",13)
    map0.insert("fourteen",14)
    map0.insert("fifteen",15)
    map0.insert("sixteen",16)
    map0.insert("seventeen",17)
    map0.insert("eightteen",18)
    map0.insert("nineteen",19)
    map0.insert("twenty",20)
    map0.insert("one thousand",1000)
    map0.insert("a lot", 99999999999999999999) # twenty 9's

# a function to remove all of the previously added items
def removeitems(map0):
    print("Removing items 1 through 20, 1000 and 99999999999999999999")
    map0.remove(1)
    map0.remove(2)
    map0.remove(3)
    map0.remove(4)
    map0.remove(5)
    map0.remove(6)
    map0.remove(7)
    map0.remove(8)
    map0.remove(9)
    map0.remove(10)
    map0.remove(11)
    map0.remove(12)
    map0.remove(13)
    map0.remove(14)
    map0.remove(15)
    map0.remove(16)
    map0.remove(17)
    map0.remove(18)
    map0.remove(19)
    map0.remove(20)
    map0.remove(1000)
    map0.remove(9999999999999999999) # twenty 9's

# run some basic checks; printing out everything that is being done so the results can be verified
def runchecks(map0):
    print("getting item 0 (should never exist):")
    print(map0.getItem(0))
    print("getting item 10:")
    print(map0.getItem(10))
    print("getting item 99999999999999999999:")
    print(map0.getItem(99999999999999999999))
    print("Is the map empty? ",map0.isEmpty())
    print("current size = ",map0.getTableSize())
    print("current length = ",map0.getLength())


# create a hashmap with seperate chaining
print("\ntesting map with seperate chaining")
map1 = hashmap.Hashmap(100, 0)
runchecks(map1)
additems(map1)
runchecks(map1)
removeitems(map1)
runchecks(map1)


# create a hashmap with linear probing
print("\ntesting map with linear probing")
map2 = hashmap.Hashmap(100, 1)
runchecks(map2)
additems(map2)
runchecks(map2)
removeitems(map2)
runchecks(map2)



# create a hashmap with quadratic probing
print("\ntesting map with quadratic probing")
map3 = hashmap.Hashmap(100, 2)
runchecks(map3)
additems(map3)
runchecks(map3)
removeitems(map3)
runchecks(map3)


