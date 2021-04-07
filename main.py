import header 

if __name__ == "__main__":
    '''membuat graph dengan pendekatan listOfDict dengan key1,value1 merupakan nama dan koordinat node, 
    dan key2,value2 merupakan edge beserta bobotnya'''
    graphDict = {}
    header.convertTxtToDict(graphDict)
    header.isiJarakAntarNode(graphDict)
    # print(graphDict)
    # for key in graphDict:
    #     print(graphDict[key])
    # listVal = header.AStarAlgorithm(graphDict,"A7","A36")
    # print(listVal)

    ''' meminta masukan node asal dan node tujuan '''
    print("Buka folder image of maps dan pilih file CaptureFixv1.0.png untuk melihat peta!")
    print()
    print()
    nodeSrc = input("Masukkan node terdekat dengan posisi anda: ")
    nodeDst = input("Masukkan node terdekat dengan tujuan anda: ")

    # ''' olah masukan '''
    # nodesOfSolution = header.AStarAlgorithm(graphDict,nodeSrc,nodeDst)
    # if (len(nodesOfSolution)!=0):


    