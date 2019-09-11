# functions is basically a collection of code that performs a particular task
# they allow u to organize ur code
#they allow u to break up ur code


# sayinh hi!

# def - keyword used to say we r giving a functioon

def say_hi(): 
    print("hello user!")
# call the function now 
say_hi()

#naming functions - name them in lower case

# parameter - piece of info that we give to a function

def say_hi(Name): 
    print("hello " + Name)
    
say_hi("Mike")
say_hi("steve")

#including more than one parameter

def say_hi(Name,age): 
    print("Hello " + Name + " You are " + age)
    
say_hi("Mike","35")
say_hi("steve","75")

#*** if u replace age with str(age), then u can remove "" at the number
def say_hi(Name,age): 
    print("Hello " + Name + " You are " + str(age))
    
say_hi("Mike",35)
say_hi("steve",75)
