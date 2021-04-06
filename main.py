import header 

if __name__ == "__main__":
    listOfdict = []
    header.convertTxtToDict(listOfdict)
    header.isiJarakAntarNode(listOfdict)
    for dictVal in listOfdict:
        print(dictVal)
    #listOfDict telah terisi namun jarak antar 2 node masih kosong