import math

def convertTxtToDict(graphDict):
    namaFile = input("Masukkan nama txt file yang ingin diolah (dalam folder test) : ")
    pathFile = "../test/" + namaFile
    objectFile = open(pathFile,'r')
    banyakNode = int(objectFile.readline())
    for i in range (banyakNode):
        tempDict = {}
        line = objectFile.readline()
        
        #ekstrak nama node
        namaNode = line.split(' ')[0]

        #ekstrak koordinat x dan y dari masing-masing node
        xCoordinate = float(line.split(' ')[1].split(',')[0])
        yCoordinate = float(line.split(' ')[1].split(',')[1])

        #masukkan koordinat
        tempDict = {}
        tempDict['coordinate'] = (xCoordinate,yCoordinate)

        #ekstrak simpul-simpul tetangga dari suatu node
        tempDictForEdge = {}
        listOfEdge = line.split(' ')[2].split(',')
        for edge in listOfEdge:
            edge = edge.strip('\n')
            tempDictForEdge[edge] = float(0)
        tempDict['edge'] = tempDictForEdge

        #masukkan ke dalam graphDict
        graphDict[namaNode] = tempDict

def haversineDistance(lat1,lon1,lat2,lon2):
    rad = math.pi/180
    radius = 6371
    dLat = rad * (lat2-lat1)
    dLon = rad * (lon2-lon1)

    a =  math.sin(dLat/2) * math.sin(dLat/2) + math.cos(rad*lat1) * math.cos(rad*lat2) *  math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return radius*c     #dalam kilometer

def isiJarakAntarNode(graphDict):
    for key in graphDict:
    
        #ambil latitude and longitude dari nodeSrc
        latSrc = graphDict[key]['coordinate'][0]
        lonSrc = graphDict[key]['coordinate'][1]

        for keyEdge in graphDict[key]['edge']:
            latDst = graphDict[keyEdge]['coordinate'][0]
            lonDst = graphDict[keyEdge]['coordinate'][1]
            
            graphDict[key]['edge'][keyEdge] = haversineDistance(latSrc,lonSrc,latDst,lonDst)

#fungsi untuk menentukan apakah sekumpulan activeNodes masih memiliki tetangga yang belum dikunjungi atau tidak
def isNoOtherWay(graphDict, activeNodes, checkedNodes):
    for key in activeNodes:
        for keyEdge in graphDict[key]['edge']:
            if (keyEdge not in checkedNodes):  
                return False
    return True

def findNearestDistance(activeNodes):
    retVal = ""
    min = 100.0
    for key in activeNodes:
        if (activeNodes[key]['f(n)']<min):
            min = activeNodes[key]['f(n)']
            retVal = key
    return retVal

def AStarAlgorithm(graphDict, nodeSrc, nodeDst):
    checkedNodes = []   #list untuk menyimpan node-node yang telah dilalui
    activeNodes = {}    #dict untuk menyimpan node beserta g(n) yang sedang aktif
    foundSolusi = False

    ''' initial state '''
    checkedNodes.append(nodeSrc)
    initialDistance = haversineDistance(graphDict[nodeSrc]['coordinate'][0],graphDict[nodeSrc]['coordinate'][1],graphDict[nodeDst]['coordinate'][0],graphDict[nodeSrc]['coordinate'][1])
    initialDict = {'f(n)' : initialDistance , 'jalur' : []}
    activeNodes[nodeSrc] = initialDict
    nodeNearest = findNearestDistance(activeNodes)
    
    ''' Looping '''
    while (not isNoOtherWay(graphDict,activeNodes,checkedNodes) and not foundSolusi):
        nodeNearest = findNearestDistance(activeNodes)
        if (nodeNearest==nodeDst):
            activeNodes[nodeNearest]['jalur'] = activeNodes[nodeNearest]['jalur'] + [nodeDst]
            foundSolusi = True
        else:
            for keyEdge in graphDict[nodeNearest]['edge']:
                if (keyEdge not in checkedNodes):
                    #tambahan checkedNodes
                    checkedNodes.append(keyEdge)

                    #hitung g(n)
                    gn = activeNodes[nodeNearest]['f(n)'] - haversineDistance(graphDict[nodeNearest]['coordinate'][0],graphDict[nodeNearest]['coordinate'][1],graphDict[nodeDst]['coordinate'][0],graphDict[nodeDst]['coordinate'][1])

                    #hitung h(n)
                    hn = haversineDistance(graphDict[keyEdge]['coordinate'][0],graphDict[keyEdge]['coordinate'][1],graphDict[nodeDst]['coordinate'][0],graphDict[nodeDst]['coordinate'][1])

                    #hitung f(n)
                    fn = gn + hn

                    updateJalur = activeNodes[nodeNearest]['jalur'] + [nodeNearest]
                    activeNodes[keyEdge] = {'f(n)':fn,'jalur':updateJalur}
            del activeNodes[nodeNearest]    #matikan node yang telah membangkitkan tetangganya
    if (foundSolusi):
        return activeNodes[nodeNearest]['jalur']
    else:
        return []

    # return 
