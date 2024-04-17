# funzione numero degli insegnanti con cattedra piena (18)
def cattedrePiena(diz):
    pieni = 0
    for key,value in diz.items():
        if(value==18):
            pieni+=1
    return(str(pieni))

# funzione calcolare il totale delle ore del dizionario
def totaleOre(diz):
    ore = 0
    for key,value in diz.items():
        ore+=value
    return(str(ore))

# scrivere una funzione che modifichi le ore allocate ad un insegnante
def modificaOre(diz, nome, ore):
        if nome in diz:
            diz[nome] = ore

# funzione scala monte ore totale
def scalaOre(diz, nome, ore):
        if nome in diz:
            if(diz[nome]>=ore):
                diz[nome] -= ore

dizionario = {"rossi":18,"bianchi":16,"venarucci":6}
# inserire un elemento dentro il dizionario
dizionario["viola"]=14
print(dizionario)
# modificare una coppia chiave valore
dizionario["bianchi"]=18
print(dizionario)
# iterare sul dizionario
for key,value in dizionario.items():
    print("la chiave è..."+key)
    print("il valore è..."+str(value))

# calcolare il totale delle ore del dizionario
ore = 0
for key,value in dizionario.items():
    ore+=value
print("il totale è..."+str(ore))

# numero degli insegnanti con cattedra piena (18)
pieni = 0
for key,value in dizionario.items():
    if(value==18):
        pieni+=1
print("cattedre piene..."+str(pieni))

# test delle funzioni
print("funzione totale ore..."+totaleOre(dizionario))
print("funzione cattedre piene..."+cattedrePiena(dizionario))
modificaOre(dizionario,"venarucci",10)
print("funzione modifica ore..."+str(dizionario))
scalaOre(dizionario,"venarucci",4)
print("funzione scala ore..."+str(dizionario))
