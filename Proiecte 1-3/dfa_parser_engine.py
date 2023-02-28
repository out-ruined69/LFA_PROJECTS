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
                stari.append(lines[i].strip())
            else:
                l=lines[i].strip().split(',')
                stari.append(l[0])
                if 'S' in l:
                    start.append(l[0])
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
matriceAdiacenta=[[[] for x in range(len(alfabet))] for y in range(len(stari))]
for i in listaTranzitii:
    if i[1] not in alfabet or i[0] not in stari or i[2] not in stari:
        print("NU E AFD")
        exit()
for i in listaTranzitii:
    matriceAdiacenta[int(i[0])][alfabet.index(i[1])].append(i[2])
if len(start)!=1:
    print("NU E AFD")
    exit()
if len(final)==0:
    print("NU E AFD")
    exit()
for i in matriceAdiacenta:
    for j in i:
        if(len(j)>1):
            print("NU E AFD")
            exit()
print("E AFD")


