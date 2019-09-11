# create a program that converts 3 digit month name to full name
# jan -> january
 # dictionary should be created in {}

monthConversions = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December",
}

print(monthConversions.get("luv", "Not a valid key"))