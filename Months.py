def months(n):
    return months[n]

n = int(input("Enter the number of the month: "))
months = {1:"January" , 2:"February" , 3:"March" , 4:"April" , 5:"May" , 6:"June" , 7:"July" , 
          8: "August" , 9:"September" , 10:"October" , 11:"November" , 12:"December" }

print("The month is\n" , months[n])