#---------------------------------------------------
#------Created  : 19/11/2024 - Khurram Asif
#------Modified : 27/11/2024 - Khurram Asif
#------Description : Python file handling tutorial
#----------------------------------------------------

# Open a text file
#f = open("timesheet.txt")

# Read contents and input out to screen 
#print(f.read())


# Read first character only
#print(f.read(1))

# Read first line only
#print(f.readline())



# Read first two lines 
#print(f.readline())
#print(f.readline())


# Read all lines 
"""
for x in f:
  print(x)
"""

# close file
#f.close()

#Open empty file 
#f2 = open("Output_File_1.txt", "w")

# Write text into empty file
#f2.write("Hello World!")


# Write first line of paycheck.txt into empty file
#f2.write(f.readline())

# Write all data from paycheck.txt into empty file
#f2.write(f.read())


# Open a text file
f = open("timesheet.txt")

# Read contents and input out to screen 
hours = f.readline()

# Open a text file
f3 = open("paycheck.txt")

earnings = f3.readline()

#Open empty file 
f2 = open("Output_File_1.txt", "w")

earnings_per_hour = float(earnings) / float(hours)

f2.write("hours : " + hours) 
f2.write("earnings : " + earnings) 
f2.write("earnings_per_hour : " + str(earnings_per_hour)) 








