from UserInterfaceOperations import *
from ThreadOperations import *
from TaskOperations import *
import sys
import datetime

def ScreenControl(screenNumber, metaData = {}):
    clearscreen()
    if screenNumber == 0:
        WelcomeScreen()
    if screenNumber == 1:
        AddNewMessages(metaData["ThreadId"])
    if screenNumber == 2:
        ViewThreadScreen()
    if screenNumber == 4:
        ThankYouScreen()
    if screenNumber == 3:
        ViewMessagesScreen(metaData["Id"])
    if screenNumber == 5:
        AddThreadScreen()
    ErrorScreen()

def ErrorScreen():
    PrintLine()
    PrintInCenter("You Ran Into an Error. Kindly press Enter to Restart")
    PrintLine()
    raw_input("")
    ScreenControl(0)

def WelcomeScreen():
    clearscreen()
    PrintLine()
    PrintInCenter("Welcome To Anubhav's Notepad")
    PrintInCenter("I Really hope you like my work")
    PrintInCenter("If You do, remember to share a word of encouragement")
    PrintInCenter("If Not, you can just share tips on how I can improve")
    PrintInCenter("Message me on anubhav.p.kumar@gmail.com")
    PrintNumberOfNewLines(2)
    PrintInCenter("Please keep your console on Maximum width for a better user Experience")
    PrintLine()
    PrintOnLeft("1. View Active Threads")
    PrintOnLeft("2. Exit")
    while(True):
        choice = input("Enter Your Choice Here >>")
        if choice == 1:
            ScreenControl(2)

def ViewThreadScreen():
    clearscreen()
    ThreadJsonList = GetAllThreads()
    PrintLine()
    PrintInCenter("These are the Active Threads")
    PrintLine()
    PrintNumberOfNewLines(3)
    ValidThreadIds = []
    for ThreadJson in ThreadJsonList:
        ValidThreadIds.append(int(ThreadJson["Id"]))
        PrintInCenter(ThreadJson["Id"]+"."+ThreadJson["Title"])
    PrintOnLeft("Enter choice 100 to start a new thread")
    choice = input("Enter the Thread Number to view the Messages>> ")
    while(True):
        if choice in ValidThreadIds:
            metadata = {}
            metadata["Id"] = choice
            ScreenControl(3, metadata)
        elif (choice == 100):
            ScreenControl(5)
        else:
            ScreenControl(4)

def AddNewMessages(ThreadId):
    PrintLine()
    PrintInCenter("Adding Messages to Thread Number "+ str(ThreadId))
    PrintLine()
    PrintNumberOfNewLines(1)
    message = raw_input("Enter Your Message >> ")
    TaskJson = {}
    TaskJson["ThreadId"] = ThreadId
    TaskJson["Message"] = message
    AddTaskToThread(ThreadId, TaskJson)
    metaData = {}
    metaData["Id"] = ThreadId
    ScreenControl(3, metaData)

def ViewMessagesScreen(ThreadId):
    TaskJsonList = GetTasksOfAThread(ThreadId)
    TaskJsonList = [] if TaskJsonList == None else TaskJsonList
    PrintLine()
    PrintInCenter("There are " + str(len(TaskJsonList)) + " messages in this thread")
    PrintLine()
    PrintNumberOfNewLines(1)
    for TaskJson in TaskJsonList:
        PrintInCenter(TaskJson["Message"])
    PrintNumberOfNewLines(2)
    PrintOnLeft("1. Add New Message")
    PrintOnLeft("2. Exit")
    choice = input("Enter Your Choice")
    metaData = {}
    metaData["ThreadId"] = ThreadId
    while True:
        if choice == 1:
            ScreenControl(1, metaData)
        if choice == 2:
            ScreenControl(4)

def AddThreadScreen():
    PrintLine()
    PrintInCenter("Start a New Thread")
    PrintLine()
    PrintNumberOfNewLines(1)
    threadTitle = raw_input("Enter the title of the New Thread >> ")
    threadJson = {}
    threadJson["Title"] = threadTitle
    threadJson["DateTime"] = datetime.datetime.now()
    AddNewThread(threadJson)
    ScreenControl(2)

def ThankYouScreen():
    PrintLine()
    PrintInCenter("Thank you for Using this. Hope you liked it")
    PrintInCenter("Please Give me a feedback on anubhav.p.kumar@gmail.com")
    PrintInCenter("Hit Enter to Exit")
    PrintLine()
    raw_input("")
    clearscreen()
    sys.exit(0)

ScreenControl(0)