import csv
import os.path

def ConvertCsvToJson(filename):
    with open(filename) as csvfile:
        csvrows = csv.reader(csvfile, delimiter=',')
        headerList = csvrows.next()
        jsonList = []
        for rows in csvrows:
            x = {}
            for i in range(0,len(headerList)):
                x[headerList[i]] = rows[i]
            jsonList.append(x)
    return jsonList

def ConvertJsonToCsv(filename, jsonList):
    if os.path.exists(filename):
        if os.path.getsize(filename):
            existingJsonList = ConvertCsvToJson(filename)
            jsonList = existingJsonList + jsonList
    with open(filename, 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvHeader = jsonList[0].keys()
        csvwriter.writerow(csvHeader)
        for jsonObject in jsonList:
            rowList = []
            for item in csvHeader:
                rowList.append(jsonObject[item])
            csvwriter.writerow(rowList)
    return True

def GetNumberOfLinesInCsv(filename):
    with open(filename) as csvfile:
        numberOfLines = len(list(csv.reader(csvfile, delimiter=',')))
        return numberOfLines - 1 if numberOfLines > 0 else 0
