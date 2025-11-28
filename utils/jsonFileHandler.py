from json import load, dumps, decoder

def readFile(fileName):
    try:
        fileData = None
        with open(fileName) as file:
            fileData = load(file)
            file.close()
        return fileData    
    except FileNotFoundError:
        return []
    except decoder.JSONDecodeError:
        return []
    
def saveFile(fileName, data):
    jsonFile = open(fileName, "w")
    jsonFile.write(dumps(data))
    jsonFile.close()     
    print("--> Cambios guardados correctamente .....")