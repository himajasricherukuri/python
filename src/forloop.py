# for loop can be used to loop through any collection
# for loop is used to define a variable 
friends = ["jim", "karen", "kevin"]

for friend in friends:
    print (friend)

# any word can be used in place of friend
friends = ["jim", "karen", "kevin"]
for index in range(10):
    print(index)


#specifying range of numbers
friends = ["jim", "karen", "kevin"]
for index in range(3, 10):
    print(index)

# figuring out how many letters 

friends = ["jim", "karen", "kevin"]

for index in range(len(friends)):
    print(friends[index])
    friends[2]
