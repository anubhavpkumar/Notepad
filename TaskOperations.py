from ThreadOperations import *

def AddTaskToThread(threadId, TaskJson):
    TaskJson["ThreadId"] = threadId
    TaskJsonList = []
    TaskJsonList.append(TaskJson)
    ConvertJsonToCsv("TaskList.csv", TaskJsonList)

def GetTasksOfAThread(threadId):
    TaskJsonList = ConvertCsvToJson("TaskList.csv") 
    TaskJsonOfThread = []
    for TaskJson in TaskJsonList:
        if (str(TaskJson["ThreadId"]).strip() == str(threadId).strip()):
            TaskJsonOfThread.append(TaskJson)
    return TaskJsonOfThread



