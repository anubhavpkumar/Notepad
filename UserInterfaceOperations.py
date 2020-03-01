import os

screencharwidth = 100
def clearscreen():
    os.system("cls")

def PrintLine():
    print ("#" * screencharwidth)

def PrintInCenter(message):
    lengthOfMessage = len(message)
    numberOfSpaces = (screencharwidth - lengthOfMessage)/2
    print (" "*numberOfSpaces) + message

def PrintNumberOfNewLines(n):
    print("\n" * n)

def PrintOnLeft(line):
    print(line)






