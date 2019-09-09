
studentfirstname = input ("Enter first name:")
studentlastname = input ("Enter last name:")
books = input ("Enter books:")

if books == "0":
    print("Number of points earned = 0 ")
elif books == "1" or "2" :
    print("Number of points earned = 5")
elif books == "3" or "4" :
    print ("Number of points earned = 10")
elif books == "5" or  "6" :
    print ("Number of points earned = 15")
elif books == "7" or "8" :
    print ("Number of points earned = 20")

else:
    print ("Number of points earned = 25")


