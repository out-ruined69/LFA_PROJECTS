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
matriceAdiacenta=[[[] for x in range(len(alfabet))] for y in range(len(stari))]
for i in listaTranzitii:
    matriceAdiacenta[int(i[0])][alfabet.index(i[1])]=(int(i[2]))

matrice=[[-1 for i in range(len(stari))] for j in range(len(stari))]

for i in range(len(stari)):
    for j in range(i):
        if i in final and j not in final or i not in final and j in final:
            matrice[i][j]=1
        else:
            matrice[i][j]=0

ok=1
while ok==1:
    ok=0
    for i in range(len(stari)):
        for j in range(i):
            if matrice[i][j] == 0:
                for k in range(len(alfabet)):
                    if matrice[matriceAdiacenta[j][k]][matriceAdiacenta[i][k]] == 1 or matrice[matriceAdiacenta[i][k]][matriceAdiacenta[j][k]]==1:
                        matrice[i][j]=1
                        ok = 1


l=[]
for i in range(len(stari)):
        for j in range(i):
            if matrice[i][j] == 0:
                l.append([i,j])

for i in range(len(l)):
    for k in range(2):
        for j in range(i+1,len(l)):
            if l[i][k] in l[j] and l[i][1-k] not in l[j]:
                l[j].append(l[i][1-k])
            if l[i][k] in l[j] and l[i][1-k] in l[j]:
                del l[i]

    i=i-1
d={}
n = len(stari)
for i in  range(len(l)):
    d[n] = l[i]
    n=n+1
for i in range(len(matriceAdiacenta)):
    for j in range(len(alfabet)):
        for key in d:
            if matriceAdiacenta[i][j] in d[key]:
                matriceAdiacenta[i][j] = key

for i in matriceAdiacenta:
    if matriceAdiacenta.count(i) > 1:
        matriceAdiacenta.remove(i)
print(matriceAdiacenta)
for i in range(len(final)):
    for key in d:
        if final[i] in d[key]:
            final[i]=key
final=list(set(final))
for key in d:
    if start[0] in d[key]:
        start[0]=key
final=list(set(final))
print(final,start)
