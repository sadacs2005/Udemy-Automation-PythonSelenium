# Write to file
writeToFile = open("C:\\Users\Sadashiva Ashok\\PycharmProjects\\AutomationProjectDCI\\Writefile.txt", 'w')
writeToFile.write("This is the content written to file")
writeToFile.close()

# Appending to the existing file
writeToFile = open("C:\\Users\Sadashiva Ashok\\PycharmProjects\\AutomationProjectDCI\\Writefile.txt", 'a')
writeToFile.write("\nThis is the 2nd content written to file")
writeToFile.close()


