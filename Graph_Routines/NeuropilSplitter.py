import Neuropil_Util
import os

def ReadObj(pLocation):
    """"""

    fileDirNames = os.listdir(pLocation)

    for filDir in fileDirNames:    
        if filDir.endswith(".obj"):
            tempOff = open(pLocation +"/"+ filDir,"r")

            all_lines = tempOff.read()

            allVerticesNumbers = Neuropil_Util.verticesSplitter.findall(all_lines)
            allFacesNumbers = Neuropil_Util.faceSplitter.findall(all_lines)

            separatedVerticesNumbers = [Neuropil_Util.numberSplitter.findall(line) for line in allVerticesNumbers] 
            separatedFacesNumbers = [Neuropil_Util.numberSplitter.findall(line) for line in allFacesNumbers] 

            size = len(separatedNumbers) 

            numTriangle = 0
            numVertices = 0

            for currentLine in range(0, len(separatedNumbers)):
                if separatedNumbers[currentLine][0] == '3':
                    separatedNumbers[currentLine][0] = 'f'
                    separatedNumbers[currentLine][1] += 1
                    separatedNumbers[currentLine][2] += 1
                    separatedNumbers[currentLine][3] += 1
                    numTriangle += 1
                else:
                    separatedNumbers[currentLine].insert(0,'v')
                    numVertices += 1

            tempObj = open(filDir.replace(".off",".obj"),"w")
            tempObj.write("# OBJ file exported from NeuroPilGraph Program\n")
            tempObj.write("# Number of vertices, triangles:" + numVertices + ", " + numTriangle)
        
            for data in separatedNumbers:
                tempObj.write(data[0] + " " + data[1] + " " + data[2] + " " + data[3] + "\n")

        tempObj.close()


if __name__ == '__main__':
    ReadObj(Neuropil_Util.GetLocation())