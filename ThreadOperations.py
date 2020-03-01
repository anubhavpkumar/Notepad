from CsvOperations import *
import datetime

def AddNewThread(threadJson):
    if (ValidateThreadJson(threadJson)):
        numberOfLines = GetNumberOfLinesInCsv("ThreadList.csv")
        threadJson = AddIdToThreadJson(threadJson, numberOfLines)
        threadJsonList = []
        threadJsonList.append(threadJson)
        return (str(ConvertJsonToCsv("ThreadList.csv", threadJsonList)))

def AddNewThreadList(threadJsonList):
    for threadJson in threadJsonList:
        AddNewThread(threadJson)

def GetAllThreads():
    ThreadsJsonList = ConvertCsvToJson("ThreadList.csv")
    return ThreadsJsonList

## Private Items
def ValidateThreadJson(threadJson):
    KeysList = threadJson.keys()
    return (("Title" in KeysList) and ("DateTime" in KeysList))

def AddIdToThreadJson(threadJson, numberOfLines):
    threadJson["Id"] = numberOfLines + 1
    return threadJson
