import os
# Reading data from the file
import sys

try:
    fileDir = os.path.dirname(os.path.abspath(__file__))
    print("File Directory is "+fileDir)
    parentDir = os.path.dirname(fileDir)
    print("Root Directory is "+parentDir)
    readFileObj = open(parentDir+"\\Readfile.txt", 'r')

    # Read all the lines
    # print(readFileObj.read())

    # Read one line
    # print(readFileObj.readline())

    # Read only some characters
    # print(readFileObj.read(10))

    # Read the file and display character by character
    # for i in readFileObj.read():
    #  print(i)

    # Read and display line by line
    readline = readFileObj.readline()
    print("The cursor position is " + str(readFileObj.tell()))
    while readline:
        print(readline)
        readline = readFileObj.readline()
except FileNotFoundError as e:
    print("The file does not exist : " + str(e))
except:
    print("Failed due to unknown reason")
