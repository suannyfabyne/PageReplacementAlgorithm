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
    for i in referencias[:nquadros]:
        listaOTM.append(i)
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
    return pagina+nquadros

def LRU(nquadros, referencias):
    listaLRU = []
    for i in referencias[:nquadros]:
        listaLRU.append(i)
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
    return pagina+nquadros

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
