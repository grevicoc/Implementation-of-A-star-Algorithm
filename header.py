def convertTxtToDict(listOfDict):
    namaFile = input("Masukkan nama file yang ingin diolah: ")
    objectFile = open(namaFile,'r')
    banyakNode = int(objectFile.readline())
    for i in range (banyakNode):
        tempDict ={}
        line = objectFile.readline()
        
        #ekstrak nama node
        namaNode = line.split(' ')[0]

        #ekstrak koordinat x dan y dari masing-masing node
        xCoordinate = float(line.split(' ')[1].split(',')[0])
        yCoordinate = float(line.split(' ')[1].split(',')[1])

        #masukkan key: node, value: koordinat
        tempDict[namaNode] = (xCoordinate,yCoordinate)

        #ekstrak simpul-simpul tetangga dari suatu node
        listOfEdge = line.split(' ')[2].split(',')
        for edge in listOfEdge:
            edge = edge.strip('\n')
            tempDict[edge] = float(0)
        
        #masukkan ke dalam listOfDict
        listOfDict.append(tempDict)
    
    return