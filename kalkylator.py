# -*- coding: cp1252 -*-
print "Välkommen till vår grymma kalkylator!"

def plus (a, b):
    return a+b
def minus (a, b):
    return a-b
def multi (a, b):
    return a*b
def div (a, b):
    return a/b


def medeltal (a):
    sum =0
    for i in a:
        sum = plus(sum, i);

    return div(sum, len(a))

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0
def summa (a):
    sum =0
    for i in a:
        sum = plus(sum, i);

    return sum

def upp (a,b):
    return a**b
print "Välj vilken funktion du vill använda:"
print "\n (1) Plus \n (2) Minus \n (3) Multiplicera \n (4) Dividera"
print "\n (5) Medeltal \n (6) Median \n (7) Summa flera tal \n (8) Upphöjning"
operation = input("Välj funktion (1-8): ")
if operation == 1:
    a = input("Tal 1: ")
    b = input("Tal 2: ")
    print plus(a, b)
if operation == 2:
    a = input("Tal 1: ")
    b = input("Tal 2: ")
    print minus (a, b)
if operation == 3:
    a = input("Tal 1: ")
    b = input("Tal 2: ")
    print multi(a, b)
if operation == 4:
    a = input("Tal 1: ")
    b = input("Tal 2: ")
    print div(a, b)
if operation == 5:
    inputLista = []
    inputting = True
    while inputting:
        inputtal = raw_input("Lägg till ett tal, X när du är klar: ")
        if inputtal == "x" or inputtal == "X":
            inputting = False
            continue
        inputLista.append(int(inputtal))
        print "Just nu har du: "
        print inputLista
    
    print medeltal(inputLista)
if operation == 6:
    inputLista = []
    inputting = True
    while inputting:
        inputtal = raw_input("Lägg till ett tal, X när du är klar: ")
        if inputtal == "x" or inputtal == "X":
            inputting = False
            continue
        inputLista.append(int(inputtal))
        print "Just nu har du: "
        print inputLista
    
    print median(inputLista)

        

    

