import numpy as np

def FIFO(nquadros, referencias):
    listaFIFO = []
    flag = 0
    for i, elem in enumerate(referencias):
        for j in listaFIFO[(len(listaFIFO)-nquadros):]:
            if (j == elem):
                flag=1
        if(flag != 1):
            listaFIFO.append(elem)
        flag=0
    return len(listaFIFO)

def OTM(nquadros, referencias):
    listaOTM = []
    quadro = 0
    flag = 0
    for elem in referencias:
        if(quadro < nquadros):
            for j in listaOTM:
                if (j == elem):
                    flag=1
            if(flag != 1):
                listaOTM.append(elem)
                quadro = quadro + 1
            flag=0

    arrayMaior = []
    flag = 0
    pagina = 0
    absoluto = -1
    referencias = referencias[nquadros:]
    for i, elem in enumerate(referencias):
        for j in listaOTM:
            if (j == elem):
                flag=1
        if(flag != 1):
            for index, process in enumerate(listaOTM):
               if (process not in referencias[i:]):
                   absoluto = process
                   break
               else:
                arrayMaior.append(referencias[i:].index(process))
            if (absoluto == -1):
                listaOTM[listaOTM.index(referencias[max(arrayMaior)+i])] = elem
            else:
                listaOTM[listaOTM.index(absoluto)] = elem
            pagina=pagina+1
        flag=0
        arrayMaior = []
        absoluto = -1
    return pagina+quadro

def LRU(nquadros, referencias):
    listaLRU = []
    quadro = 0
    flag = 0
    for elem in referencias:
        if(quadro < nquadros):
            for j in listaLRU:
                if (j == elem):
                    flag=1
            if(flag != 1):
                listaLRU.append(elem)
                quadro = quadro + 1
            flag=0

    arrayMenor = []
    flag = 0
    pagina = 0
    counter = 0
    #referencias = referencias[nquadros:]
    for i, elem in enumerate(referencias):
        for j in listaLRU:
            if (j == elem):
                flag=1
        if(flag != 1):
            for index, process in enumerate(listaLRU):
                for(indexref, processref) in enumerate(reversed(referencias[:i])):
                    if(process == processref):   
                        arrayMenor.append((len(referencias[:i]) -1 - counter))
                        break
                    counter=counter+1
                counter = 0

            listaLRU[listaLRU.index(referencias[min(arrayMenor)])] = elem
            pagina = pagina + 1
        flag=0
        arrayMenor = []
    return pagina+quadro

txtfile = open('entry.txt', 'r')
txt = txtfile.readlines()
listEntry = []

for line in txt :
    listEntry.append(int(line))
txtfile.close()

nquadros = listEntry[0]
referencias = []

for i, elem in enumerate(listEntry[1:]):  
    referencias.append(elem)


print("FIFO", FIFO(nquadros, referencias))
print("OTM", OTM(nquadros, referencias))
print("LRU", LRU(nquadros, referencias))
