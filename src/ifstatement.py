#specifying conditions
#create a boolean variable

is_male = False

if is_male:
    print("You are a male")

else:
    print("You are not a male")


# adding another variable into the booelan
#OR operator
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are male or tall or both") 

else:
    print("You are neither male nor tall")

#AND operator

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male") 

else:
    print("You are either not male or not tall or both")

# adding in more conditions (ELIF)

is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male") 

elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")

