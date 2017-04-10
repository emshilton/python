# This exercise creates a program that easily allows you to move files from the command line
# Be sure you have the correct file paths when moving important files

# Imports necessary libraries
import os
import os.path

# Prompts user to enter the current path to the file
print "Enter the current path to your file including file name: "
initFilePath = raw_input()


#Checks for valid input and if not prompts user to re-enter
while not os.path.isfile(initFilePath):
	print "Invalid Path - Enter the initial path to your file: "
	initFilePath = raw_input()


# Prompts the user to enter the final file location
print "Enter the location you want the file moved to: "
finalPath = raw_input()

# Extracts the file name from the file path
pathList = initFilePath.split('/')
fileName = pathList[-1]

# Creates destination file path
finalFilePath = finalPath + '/' + fileName

# Moves the file to the final file path
os.rename(initFilePath, finalFilePath)

#Checks for succesful move
if os.path.isfile(finalFilePath):
	print "Your file has been moved successfuly" 
else:
	print "There has been an error moving your file!!"
