#C1615033

import numpy as np
import math

def makeDict (file):#counts how many different words in a file
    file_object = open(file,"r")
    wordDict = {}
    for line in file_object:
        wordslist = line.split()
        # print(line)
        for word in wordslist:
            if word not in wordDict:
                wordDict[word] = 1
    file_object.close()
    print("Words in dictionary:", len(wordDict))
    printQuery(queryFile)
    file_object.close()



def printQuery(file):
    queryFile = open(file, "r")
    for q in queryFile:
        print("Query: ", q.strip())
        printRelDocs(q.strip())
    queryFile.close()


def printRelDocs(query):

    document = open(documentFile,"r")
    relevantDocs = []
    for index, lines in enumerate(document, start=1):
        if set(query.split()).issubset(lines.split()):
                relevantDocs.append(index)



    print("Related Documents:", str(relevantDocs)[1:-1].replace(", ", " "))
    findAngles(relevantDocs,query)
    document.close()


def findAngles(relevantDocs, query):


    docfile = open(documentFile, "r")
    angles_dict = {}
    index = 0
    finalDict = {}
    for index, line in enumerate(docfile,start=1):
        if index in relevantDocs:
            queryVec = []
            lineDict = dictline(line)
            lineVec = getVector(lineDict)
            tempList = templateList(line)
            for word in tempList:
                if word in query.split():
                    queryVec.append(1)
                else:
                    queryVec.append(0)

            lineArray = np.array(lineVec)
            queryArray = np.array(queryVec)

            angles_dict[index] =  round(calc_angle(lineVec,queryVec),5)
    sorted_Angles = sorted(angles_dict.items(), key=lambda x: x[1])
    for i in sorted_Angles:
        print(i[0],i[1])
    docfile.close()








def dictline(text):
    wordDict = {}


    for i in text.split():
        #print(i)
        if i in wordDict:
            wordDict[i] += 1
        else:
            wordDict[i] = 1
    return  wordDict


def templateList(line):
    wordDictionary = {}
    tempList = []

    for i in line.split():

        if i not in wordDictionary:
            wordDictionary[i]=1
            tempList.append(i)

    return tempList



def getVector(dict): #converts the dictionary to a vector
    vec = []
    for values in dict.values():
        vec.append(values)
    return vec



def calc_angle(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta



print("Please enter the files in the same directory of the python file.")
documentFile = "docs.txt"

#makeDict("docs.txt")
queryFile = "queries.txt"
makeDict(documentFile)


