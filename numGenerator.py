import random
lista = []
loop = True
for i in range(14):
    if i == 0:
        input()
        nota = round(random.uniform(0, 10), 2)
        lista.append(nota)
        print(nota, end = " ")
    else:
        maxmin = lista[0]
        if maxmin - 2 < 0:
            nota = round(random.uniform(0, maxmin + 3), 2)
            lista.append(nota)
            print(nota, end = " ")
        elif maxmin + 3 > 10: 
            nota = round(random.uniform(maxmin - 1, 10), 2)
            lista.append(nota)
            print(nota, end = " ")
        else:
            nota = round(random.uniform(maxmin - 1, maxmin + 3), 2)
            lista.append(nota)
            print(nota, end = " ")
                
