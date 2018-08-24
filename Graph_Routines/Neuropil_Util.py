# # Organizing Files Libs
#import os
#import shutil
#import re

##region Regular Expressions

## Get all the numbers in any format (being float or int)
#numberPattern = "[-+]?[0-9]*\.?[0-9]+(?:e[-+][0-9]+)?"

## Get all dendrites in Synapse Connections
#dendritePattern = "[d(\d)*p_sy(\d)*,]"

## Get all the Synapse Connections
#synapsePattern = re.compile("a\d*-" + dendritePattern + "*\n")

## Compiled version of the Regular Expression above that gets
## all the numbers in the file 
#numberSplitter = re.compile(numberPattern)

## Get all the numbers divided by commas
#allNumbersComma = "(?:" + numberPattern + ",?)"

## Get all the numbers divided by white space
#allNumbersWhiteSpace = "(?:" + numberPattern + " ?)*\n?"

## Get all the numbers divided by white space with the v in the front
#verticesSplitter = re.compile("(v (?:(?:\-?\d*\.\d*)\ ?)*)")

## Get all the numbers divided by white space with the f in the front
#faceSplitter = re.compile("(f (?:(?:\-?\d*)\ ?)*)")

## Splitter to get all the numbers divided by white space
#allNumbersWhiteSpcaceSplitter = re.compile(allNumbersWhiteSpace)

## Compiled version of the Regular Expression above that gets
## all the morphology line in the file
#morphologySplitter = re.compile("(" + numberPattern + "\s*-\s*" + allNumbersComma + "*)\s*\n?")

## Compiled version of the Regular Expression above that gets
## all the connection lines in the file
#connectionSplitter = re.compile(numberPattern + "\(" + numberPattern + "\)\s+?-\s+?" + 
#				numberPattern + "\(" + numberPattern + "\)")

##endregion 

##region Helper Functions
#def ToObj(pLocation):
#    """Converts all off files into obj files in the 
#    pLocation passed and creates the new obj file
#    converted.
    
#    Example of use: 
#    ToObj(".")"""

#    fileDirNames = os.listdir(pLocation)

#    for filDir in fileDirNames:    
#        if filDir.endswith(".off"):
#            tempOff = open(filDir,"r")

#            allNumbers = allNumbersWhiteSpcaceSplitter.findall(tempOff.read())
#            separatedNumbers = [numberSplitter.findall(line) for line in allNumbers] 

#            size = len(separatedNumbers)

#            del separatedNumbers[0]
#            del separatedNumbers[0]
#            del separatedNumbers[0]
#            del separatedNumbers[0]
#            del separatedNumbers[0]
#            del separatedNumbers[-1]

#            numTriangle = 0
#            numVertices = 0

#            for currentLine in range(0, len(separatedNumbers)):
#                if separatedNumbers[currentLine][0] == '3':
#                    separatedNumbers[currentLine][0] = 'f'
#                    separatedNumbers[currentLine][1] += 1
#                    separatedNumbers[currentLine][2] += 1
#                    separatedNumbers[currentLine][3] += 1
#                    numTriangle += 1
#                else:
#                    separatedNumbers[currentLine].insert(0,'v')
#                    numVertices += 1

#            tempObj = open(filDir.replace(".off",".obj"),"w")
#            tempObj.write("# OBJ file exported from NeuroPilGraph Program\n")
#            tempObj.write("# Number of vertices, triangles:" + numVertices + ", " + numTriangle)
        
#            for data in separatedNumbers:
#                tempObj.write(data[0] + " " + data[1] + " " + data[2] + " " + data[3] + "\n")

#        tempObj.close()

#def IterableVersion(pObject):
#    """Return the iterable version of the object passed.
#    If the object was already iterable it returns the original
#    object.
    
#    Example of use: iterObject = IterableVersion(object)"""
#    try:
#        if not isinstance(pObject,str):
#            some_object_iterator = iter(pObject)
#        else:
#            pObject = [pObject] 
#    except TypeError, te:
#        pObject = [pObject] 
    
#    return pObject

#def CountFiles(pFileExtension, pTuple):
#    if pTuple == None:
#        pTuple = (pFileExtension,1)
#    elif pTuple[0] == pFileExtension: 
#        pTuple = (pFileExtension,pTuple[1]+1)

#    return pTuple

##endregion

##region Print Functions
#def PrintCount(pTuples,pStringTypes,pAction):
#    """Prints to a command-line the total number of files.
#    Uses the filenames (passed through pStringType) to 
#    generate the text. If the tuples are empty then
#    generate the error message accordingly.
    
#    Example of use: 
#    PrintCount(tuple,"Axons","moved")"""

#    pTuples = IterableVersion(pTuples)
#    pStringTypes = IterableVersion(pStringTypes)

#    if len(pTuples) != len(pStringTypes):
#        print "The number of tuples has to be the same then strings"
#    else:
#        for tuple,stringType in zip(pTuples,pStringTypes):
#            if tuple == None:
#                print "No "+stringType+" " + pAction + "."
#            else:
#                print stringType+ " "+pAction+" : " + str(tuple[1])

#    print

#def PrintExtensions(pSets,pStringTypes):
#    """Prints to a command-line the total number of different 
#    extensions. Uses the filenames (passed through pStringType) 
#    to generate the text.
    
#    Example of use: 
#    PrintExtensions(axonExtensions,"Axons")"""

#    pSets = IterableVersion(pSets)
#    pStringTypes = IterableVersion(pStringTypes)
#    separationPattern = ", "

#    if len(pSets) != len(pStringTypes):
#        print "The number of sets has to be the same then strings"
#    else:
#        for set,stringType in zip(pSets,pStringTypes):
#            allExtensions = ""
#            for extension in set:
#                allExtensions += extension + separationPattern
#            allExtensions = allExtensions[0:len(allExtensions) - len(separationPattern)]
#            print stringType+ " has "+str(len(set))+" different extensions. Being: " + str(allExtensions.upper())

#    print

##endregion

##region Data Manipulation Functions
#def GetAllFiles(pLocation,pExtension=None,pFullPathMode=False,pInFolder=False):
#    """
#    Get all files inside a location and 
#    return the list that contains all those
#    files.

#    This function has some optional arguments:
#    pExtension can be defined to filter the
#    files that are returned, and pFullPathMode
#    can be set to True to return the files in 
#    a Full Path Format
    
#    Example of use:
#    files = GetAllFiles(location)
#    files = GetAllFiles(location,extension)
#    files = GetAllFiles(location,extension,pFullPathMode=True)
#    files = GetAllFiles(location,pFullPathMode=True)
#    """
#    list = []

#    if pInFolder:
#        # I probably have an eror here because this method goes inside the folder too
#        # use the os.listdir() that only get all the files and directories
#        # from the current location.
#        for (dirpath, dirnames, filenames) in os.walk(pLocation):
#            dirList = []
#            if pExtension != None:
#                 for file in filenames:
#                    if file.endswith(pExtension.lower()):
#                        dirList.append(file)
#            else:
#                dirList.extend(filenames)
#            if pFullPathMode and len(dirList) != 0:
#                list.extend([dirpath.replace("\\","/") + "/" + file for file in dirList])
#    else:
#        if pExtension != None:
#            for file in os.listdir(pLocation):
#                if file.endswith(pExtension.lower()):
#                    list.append(file)
#        else:
#            for (dirpath, dirnames, filenames) in os.walk(pLocation):
#                list.extend(filenames)
#                break

#        if pFullPathMode:
#            list = [pLocation + "/" + file for file in list]

#    return list

#def GetInfo(pList):
#    """
#    Get all the information from a list of files returning
#    a list containing the Tuple with the number of different
#    files (meaning the number of axons or others) and all
#    the different file extensions.

#    Example of use: [tuple,set] = GetInfo(listOfFiles)
#    """

#    tempTuple = None
#    allExtensions = set()

#    for file in pList:
#        if file[0] != ".": 
#            fileExtension = GetFileExtension(file)
#            allExtensions.add(fileExtension)
#            tempTuple = CountFiles(fileExtension,tempTuple)

#    return [tempTuple,allExtensions]

#def GetLocation(pObjType=None):
#    """
#    Returns the location where the files of the type 
#    pObjType are located.

#    If nothing is passed returns the location 
#    where all the folders are stored, meaning
#    the Axons, Dendrites and Synapses folders.
#    This can be used to later get all files 
#    that are organized.

#    Example of use: 
#    location = GetLocation("Axons")
#    location = GetLocation()
#    """

#    if pObjType == None:
#        return os.curdir + "/InputFiles"
#    else:
#        return os.curdir + "/InputFiles/" + pObjType.lower().capitalize()

#def GetFileExtension(pFile):
#    """
#    Get the file extension of pFile.

#    Example of use: extension = GetFileExtension(file)
#    """

#    return os.path.basename(pFile).split(".")[1]

#def GetFileName(pFile):
#    """
#    Get only the file name of pFile.

#    Example of use: fileName = GetFileName(file)
#    """

#    return os.path.basename(pFile).split(".")[0]

#def GetCompartmentType(pFile):

#    fileName = GetFileName(pFile)

#    if fileName.find("sy") != -1:
#        return "Synapse"
#    elif fileName[0] == "a":
#        return "Axon"
#    elif fileName[0] == "d":
#        return "Dendrite"
    
#def OrganizeData(debugMode=False):
#    """
#    Check if there are files in the InputFiles Folder. 
#    If there is none, displays the error accordingly. 
#    If there are files check the names to determine
#    on wich folder to put them and prints the 
#    summary of the operations.

#    All the prints are only done if the user
#    activated the debugMode. Also it calls
#    the CheckOrganizedData method to display
#    all the files currently organized.

#    Example of use: OrganizeData() - debugMode Off
#    by default.
#    OrganizeData(debugMode = True) - debugMode On.
#    """
#    currentLocation = os.curdir + "/InputFiles" 
#    unorganizedFiles = GetAllFiles(currentLocation)

#    if len(unorganizedFiles) == 0:
#        if debugMode:
#            print "No files were added to the program.\n If you want to "+ \
#                   "add new Axon,Dendrite or Synapse files add then to "+\
#                    "the InputFiles folder."
#            print
#    else:
#        axons = None
#        dendrites = None
#        synapses = None

#        for file in unorganizedFiles:
#            tempFileLocation = currentLocation + "/" + file
#            fileExtension = os.path.splitext(file)[1][1:]
#            if file[0] == "a":   
#                axons = CountFiles(fileExtension,axons)
#                shutil.move(tempFileLocation,currentLocation + "/Axons/" + file)
#            elif file[0] == "d":
#                if file.find("sy") != -1:
#                    synapses = CountFiles(fileExtension,synapses)
#                    shutil.move(tempFileLocation,currentLocation + "/Synapses/" + file)
#                else: 
#                    dendrites = CountFiles(fileExtension,dendrites)
#                    shutil.move(tempFileLocation,currentLocation + "/Dendrites/" + file)

#        if debugMode:
#            PrintCount([axons,dendrites,synapses],["Axons","Dendrites","Synapses"],"moved")
        
#    if debugMode:
#        CheckOrganizedData()

#def CheckOrganizedData():
#    """
#    Check the folders of Axons, Dendrites and 
#    Synapses and prints the number os files 
#    and all the extensions found.

#    Example of use: CheckOrganizedData()
#    """
#    currentLocation = os.curdir + "/InputFiles" 

#    axonFiles = GetAllFiles(currentLocation + "/Axons")
#    dendriteFiles = GetAllFiles(currentLocation + "/Dendrites")
#    synapseFiles = GetAllFiles(currentLocation + "/Synapses")

#    [axons,axonExtensions] = GetInfo(axonFiles)
#    [dendrites,dendriteExtensions] = GetInfo(dendriteFiles)
#    [synapses,synapsesExtensions] = GetInfo(synapseFiles)

#    PrintCount([axons,dendrites,synapses],["Axons","Dendrites","Synapses"],"already organized")
#    PrintExtensions([axonExtensions,dendriteExtensions,synapsesExtensions],["Axons","Dendrites","Synapses"])

#    #endregion 