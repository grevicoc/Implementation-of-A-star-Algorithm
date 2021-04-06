import math

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
        tempDictForEdge = {}
        listOfEdge = line.split(' ')[2].split(',')
        for edge in listOfEdge:
            edge = edge.strip('\n')
            tempDictForEdge[edge] = float(0)
        tempDict['edge'] = tempDictForEdge

        #masukkan ke dalam listOfDict
        listOfDict.append(tempDict)

def haversineDistance(lat1,lon1,lat2,lon2):
    rad = math.pi/180
    radius = 6371
    dLat = rad * (lat2-lat1)
    dLon = rad * (lon2-lon1)

    a =  math.sin(dLat/2) * math.sin(dLat/2) + math.cos(rad*lat1) * math.cos(rad*lat2) *  math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return radius*c

def isiJarakAntarNode(listOfDict):
    for i in range (len(listOfDict)):
        
        #ambil node source
        nodeSrc = list(listOfDict[i].keys())[0]
        for key in listOfDict[i]['edge']:

            #ambil latitude and longitude dari nodeSrc
            latSrc = listOfDict[i][nodeSrc][0]
            lonSrc = listOfDict[i][nodeSrc][1]
            
            #ambil node destination
            for dictVal in listOfDict:
                if key in dictVal:
                    #ambil latitude and longitude dari nodeDst
                    latDst = dictVal[key][0]
                    lonDst = dictVal[key][1]
                    listOfDict[i]['edge'][key] = haversineDistance(latSrc,lonSrc,latDst,lonDst)
                    break
            