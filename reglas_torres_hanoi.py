def letrasProposicionales(disco, posicion, torre, ronda):
    letras = []
    primera_ronda = True
    for r in ronda:
        if primera_ronda:
            for d in disco:
                letras.append(d + posicion[disco.index(d)] + torre[0] + r)
                primera_ronda = False
        else:
            for t in torre:
                for p in posicion:
                    if int(r)%2 == 0:
                        letras.append(disco[0] + p + t + r)
                    else:
                        letras.append(disco[1] + p + t + r)
    return letras

def regla_movimiento(letras, ronda):
    inicial = True
    regla = ""
    for i in range(2,len(ronda)+1):
        aux1 = [x for x in letras if int(x[3]) == i]
        for p in aux1:
            regla_ronda = p
            aux2 = [x + "-" for x in aux1 if x != p]
            for q in aux2:
                regla_ronda = q + regla_ronda + "Y"
            if inicial:
                regla = regla_ronda
                inicial = False
            else:
                regla = regla_ronda + regla + "O"
    return regla

def regla_cantidad_posicion(letras, posicion, torre, ronda):
    inicial = True
    regla = ""
    for i in range(1,len(ronda)):
        aux1disco1 = [x for x in letras if int(x[3]) == i]
        aux1disco2 = [x for x in letras if int(x[3]) == i + 1]
        for j in range(len(torre)):
            aux2disco1 = [x for x in aux1disco1 if torre.index(x[2]) == j]
            aux2disco2 = [x for x in aux1disco2 if torre.index(x[2]) == j]
            for p in aux2disco1:
                regla_posicion = p
                aux3 = [x + "-" for x in aux2disco2 if x[1] == p[1]]
                for q in aux3:
                    regla_posicion = q + regla_posicion + ">"
                if inicial:
                    regla = regla_posicion
                    inicial = False
                else:
                    regla = regla_posicion + regla + "Y"
    return regla

def regla_tamano(letras, disco, torre):
    inicial = True
    regla = ""
    for i in range(2, len(ronda)):
        aux1disco1 = [x for x in letras if int(x[3]) == i]
        aux1disco2 = [x for x in letras if int(x[3]) == i + 1]
        for j in range(len(torre)):
            aux2disco1 = [x for x in aux1disco1 if torre.index(x[2]) == j]
            aux2disco2 = [x for x in aux1disco2 if torre.index(x[2]) == j]
            for p in aux2disco1:
                regla_posicion = p
                negaciones = ""
                primera = True
                aux3 = [x + "-" for x in aux2disco2 if (disco.index(p[0]) < disco.index(x[0])) and int(p[1]) > int(x[1])]
                if len(aux3) > 0:
                    for q in aux3:
                        if primera:
                            negaciones = q
                            primera = False
                        else:
                            negaciones = q + negaciones + "Y"
                    regla_posicion = negaciones + regla_posicion + ">"
                    if inicial:
                        regla = regla_posicion
                        inicial = False
                    else:
                        regla = regla_posicion + regla + "Y"
    return regla

def regla_final(letras, disco, ronda):
    inicial = True
    regla = ""
    aux1 = [x for x in letras if x[2] == "c"]
    aux2 = [x for x in aux1 if (int(x[3]) + disco.index(x[0])) == len(ronda)]
    correctas = [x for x in aux2 if (disco.index(x[0]) + 1) == int(x[1])]
    incorrectas = [x + "-" for x in aux2 if x not in correctas]
    for p in correctas:
        if inicial:
            regla = p
            inicial = False
        else:
            regla = p + regla + "Y"
    for q in incorrectas:
        regla = q + regla + "Y"
    return regla


disco = ["a", "b"]
posicion = [str(i) for i in range(1, len(disco)+1)]
torre = ["a", "b", "c"]
ronda = [str(i) for i in range(1,5)]

letras = letrasProposicionales(disco, posicion, torre, ronda)
print(regla_movimiento(letras, ronda))
print("")
print(regla_cantidad_posicion(letras, posicion, torre, ronda))
print("")
print(regla_tamano(letras, disco, torre))
print("")
print(regla_final(letras, disco, ronda))

print(letras)
print(len(letras))
