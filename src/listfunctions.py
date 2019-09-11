lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby"]
friends.extend(lucky_numbers)
print(friends)
# extend function allows you take a list and append it on another list

#append- adding individual elements
lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby"]
friends.append("creed")
print(friends)


#insert - inserts the element at the given index, shifting elements to the right.

lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby"]
friends.insert(1,"kelly")
print(friends)

#remove - searches for the first instance of the given element and removes it
lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby"]
friends.remove("jim")
print(friends)

#clear - gives an empty list
lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby"]
friends.clear()
print(friends)

#pop- pops /remobves last element in the list
lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby"]
friends.pop()
print(friends)

#index- searches for the given element from the start of the list and returns its index. 

lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby"]
print(friends.index("kevin"))

#count the number of similar elements
lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby","kevin"]
print(friends.count("kevin"))

#sort - sort the list in ascending order

lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby"]
friends.sort()  
lucky_numbers.sort()
print(lucky_numbers)
print(friends)

# reverse a list

lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby"]
friends.reverse()
print(friends)

# copy -used to copy attributes from another list

lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","karen","jim","oscar","toby"]
friends2 = friends.copy()
print(friends2)



