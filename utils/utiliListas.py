def findDictionaryIndex(dataList, key, value):
    ind = -1
    for i in range(len(dataList)):
        if dataList[i].get("code"key) == value:
            ind = i
            break

    return ind