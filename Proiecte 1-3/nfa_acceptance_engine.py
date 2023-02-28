f=open("fisier1.in")
lines=f.readlines()
i=0
alfabet=[]
stari=[]
start=[]
final=[]
while i< len(lines):
    while lines[i][0] == '#':
        i+=1
      #  print("#")

    if "Sigma" in lines[i]:
        i+=1
        while "End" not in lines[i]:
            alfabet.append(lines[i].strip())
            i+=1
           # print("sigma")

    if "States" in lines[i]:
        i+=1
        while "End" not in lines[i]:
            if "," not in lines[i]:
                stari.append(int(lines[i].strip()))
            else:
                l=lines[i].strip().split(',')
                stari.append(int(l[0]))
                if 'S' in l:
                    start.append(int(l[0]))
                if 'F' in l:
                    final.append(int(l[0]))
            i+=1

    listaTranzitii=[]
    if "Transitions" in lines[i]:
        i+=1
        while "End" not in lines[i]:
            l=lines[i].strip().split(',')
            listaTranzitii.append(l)
            i+=1
    i+=1
matriceAdiacentaAFN=[[[] for x in range(len(alfabet))] for y in range(len(stari))]
for i in listaTranzitii:
    matriceAdiacentaAFN[int(i[0])][alfabet.index(i[1])].append(int(i[2]))
coada = []
cuvant="aababb"
coada.append(start)
for litera in cuvant:
    n = len(coada)
    for i in range(n):
        lista=[x for x in coada[i]]
        y=matriceAdiacentaAFN[lista[len(lista)-1]][alfabet.index(litera)]
        for ob in y:
            lista.append(ob)
            l = [x for x in lista]
            coada.append(l)
            del lista[len(lista)-1]
    for i in range(n):
        del coada[0]
print(coada)
for lista in coada:
    if lista[len(lista)-1] in final:
        print("Acceptat")
        exit()
print("Respins")