"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    arch = open('data.csv','r').readlines()
    arch = [int(z.replace("\n","").split()[1]) for z in arch]
    suma = sum(arch)

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    arch = open('data.csv','r').readlines()
    arch = [z.replace("\n", "").split()[0] for z in arch]
    resp = list(set([(x,arch.count(x)) for x in arch]))
    resp.sort(key = lambda x: x[0])

    return resp


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    arch = open('data.csv','r').readlines()
    arch = [z.replace("\n", "").split()[0:2] for z in arch]
    letters = []
    suma = []
    for lista in arch:
        if lista[0] not in letters:
            letters.append(lista[0])
            suma.append(int(lista[1]))
        else:
            suma[letters.index(lista[0])] += int(lista[1])
    resp = list(zip(letters,suma))
    resp.sort(key = lambda x: x[0])
    return resp


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    arch = open('data.csv','r').readlines()
    arch = [renglon.replace("\n", "").split()[2].split("-")[1] for renglon in arch]
    resp = list(set([(x,arch.count(x)) for x in arch]))
    resp.sort(key = lambda x: x[0])
    return resp

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    arch = open('data.csv','r').readlines()
    arch = [renglon.split()[0:2] for renglon in arch]
    for i in range(len(arch)):
        arch[i][1] = int(arch[i][1])
    letters = []
    max = []
    min = []
    for lista in arch:
        if lista[0] not in letters:
            letters.append(lista[0])
            max.append(lista[1])
            min.append(lista[1])
        elif lista[1] > max[letters.index(lista[0])]:
            max[letters.index(lista[0])] = lista[1]
        elif lista[1] < min[letters.index(lista[0])]:
            min[letters.index(lista[0])] = lista[1]
    resp = list(zip(letters,max,min))
    resp.sort(key=lambda x: x[0])
    return resp


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    arch = open('data.csv','r').readlines()
    arch = [renglon.split()[4].split(",") for renglon in arch]
    dic = {}

    for lista in arch:
        for list2 in lista:
            w = list2.split(":")
            if w[0] not in dic.keys():
                dic[w[0]] = [int(w[1]),int(w[1])]
            elif dic[w[0]][0] > int(w[1]):
                dic[w[0]] = [int(w[1]),dic[w[0]][1]]
            elif dic[w[0]][1] < int(w[1]):
                dic[w[0]] = [dic[w[0]][0],int(w[1])]
    valores = [(list(dic.keys())[x],list(dic.values())[x][0],list(dic.values())[x][1]) for x in range(len(dic.keys()))]
    valores.sort(key = lambda x: x[0])
    return valores


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    arch = open('data.csv','r').readlines()
    arch = [renglon.split()[0:2] for renglon in arch]
    for i in range(len(arch)):
        arch[i][1] = int(arch[i][1])
    resp = []
    for j in range(10):
        w = []
        for i in arch:
            if i[1] == j:
                w.append(i[0])
        resp.append((j, w))
    resp.sort(key = lambda x: x[0])
    return resp


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    resp = pregunta_07()
    for tup in range(len(resp)):
        resp[tup] = list(resp[tup])
        resp[tup][1] = list(set(resp[tup][1]))
        resp[tup][1].sort()
        resp[tup] = tuple(resp[tup])

    return resp



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    arch = open('data.csv', 'r').readlines()
    arch = [renglon.replace("\n","").split()[4].split(",") for renglon in arch]
    arch = [clave.split(":")[0] for lista in arch for clave in lista]
    keys = []
    counter = []
    for clave in arch:
        if clave not in keys:
            keys.append(clave)
            counter.append(arch.count(clave))
    resp = list(zip(keys, counter))
    resp.sort(key=lambda x: x[0])
    resp = dict(resp)
    return resp


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    arch = open('data.csv','r')
    arch = [(renglon.split()[0],len(renglon.split()[3].split(",")),len(renglon.split()[4].split(","))) for renglon in arch]
    return arch


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    arch = open("data.csv", "r")
    arch = [[int(renglon.split()[1]), renglon.split()[3].split(",")] for renglon in arch]

    keys = []
    suma = []

    for e in range(len(arch)):
        for i in arch[e][1]:

            if i not in keys:
                keys.append(i)
                suma.append(arch[e][0])
            else:
                suma[keys.index(i)] += arch[e][0]
    resp = list(zip(keys,suma))
    resp.sort(key = lambda x :x[0])
    resp = dict(resp)
    return resp



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    arch = open("data.csv", "r")
    arch = [[renglon.split()[0], renglon.replace("\n","").split()[4].split(",")] for renglon in arch]
    for e in range(len(arch)):
        for i in range(len(arch[e][1])):
            arch[e][1][i] = int(arch[e][1][i].split(":")[1])
        arch[e][1] = sum(arch[e][1])
    suma = []
    keys = []
    for i in range(len(arch)):
        if arch[i][0] not in keys:
            keys.append(arch[i][0])
            suma.append(arch[i][1])
        else:
            suma[keys.index(arch[i][0])] += arch[i][1]
    resp = list(zip(keys,suma))
    resp.sort(key=lambda x: x[0])
    resp = dict(resp)
    return resp
