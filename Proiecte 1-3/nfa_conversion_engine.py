f=open("fisier1.in")
lines=f.readlines()
i=0
alfabet=[]
stari=[]

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
                stari.append(lines[i].strip())
            else:
                l=lines[i].strip().split(',')
                stari.append(l[0])
                if 'S' in l:
                    start=int(l[0])
                if 'F' in l:
                    final.append(l[0])
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
    matriceAdiacentaAFN[int(i[0])][alfabet.index(i[1])].append(i[2])
QPrim=[]
l=[]
#print(matriceAdiacentaAFN)
matriceAdiacentaAFD=[]
#print(QPrim)
for simbol in range(len(alfabet)):
        if matriceAdiacentaAFN[start][simbol] not in QPrim and len(matriceAdiacentaAFN[start][simbol]) !=0:
            QPrim.append(matriceAdiacentaAFN[start][simbol])
a=[]
for i in QPrim:
    if(QPrim.index(i)!=0):
        a=[]
        for el in i:
            l=[]
            for simbol in range(len(alfabet)):
                print(matriceAdiacentaAFN[int(el)][simbol])
                if matriceAdiacentaAFN[int(el)][simbol] not in l:
                    l.append(matriceAdiacentaAFN[int(el)][simbol])
                    print(l)
            if l not in QPrim and len(l)!=0:
                QPrim.append(l)
            a.append(l)
    matriceAdiacentaAFD.append(a)




        # if matriceAdiacentaAFN[i.index(el)][simbol] not in QPrim and len(matriceAdiacentaAFN[i.index(el)][simbol]) !=0:
        #             QPrim.append(matriceAdiacentaAFN[QPrim.index(i)][simbol])
        #         l.append(matriceAdiacentaAFN[QPrim.index(i)][simbol])
        # #print(l)
        # a=[]
        # for lista in l:
        #     for el in lista:
        #         a.append(el)
        # matriceAdiacentaAFD.append(a)

