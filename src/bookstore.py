
studentfirstname = input ("Enter first name:")
studentlastname = input ("Enter last name:")
books = input ("Enter books:")

if books == "0":
    print("Number of points earned = 0 ")
elif books == "1" or books == "2" :
    print("Number of points earned = 5")
elif books == "3" or books == "4" :
    print ("Number of points earned = 10")
elif books == "5" or books == "6" :
    print ("number of points earned = 15")
elif books == "7" or books == "8" :
    print ("number of points earned = 20")
else :
    print ("number of points earned = 25")


