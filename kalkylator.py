# -*- coding: cp1252 -*-
print "V�lkommen till v�r grymma kalkylator!"
running = True
while running:
    def plus (a, b):
        return a+b
    def minus (a, b):
        return a-b
    def multi (a, b):
        return a*b
    def div (a, b):
        if a==0 or b==0:
            print "Input invalid!"
            return 0
        return a/b
    def medeltal (a):
        summa = sum(a)
        return div(summa, len(a))
    def median(lst):
        sortedLst = sorted(lst)
        lstLen = len(lst)
        index = (lstLen - 1) // 2
        if (lstLen % 2):
            return sortedLst[index]
        else:
            return (sortedLst[index] + sortedLst[index + 1])/2.0
    def summa (a):
        summa = sum(a)
        return summa
    def upp (a,b):
        return a**b

    print "V�lj vilken funktion du vill anv�nda:"
    print "\n (1) Plus \n (2) Minus \n (3) Multiplicera \n (4) Dividera"
    print "\n (5) Medeltal \n (6) Median \n (7) Summa flera tal \n (8) Upph�jning"
    operation = input("V�lj funktion (1-8): ")

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
            inputtal = raw_input("L�gg till ett tal, X n�r du �r klar: ")
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
            inputtal = raw_input("L�gg till ett tal, X n�r du �r klar: ")
            if inputtal == "x" or inputtal == "X":
                inputting = False
                continue
            inputLista.append(int(inputtal))
            print "Just nu har du: "
            print inputLista
        print median(inputLista)

    if operation == 7:
        inputLista = []
        inputting = True
        while inputting:
            inputtal = raw_input("L�gg till ett tal, X n�r du �r klar: ")
            if inputtal == "x" or inputtal == "X":
                inputting = False
                continue
            inputLista.append(int(inputtal))
            print "Just nu har du: "
            print inputLista
        
        print summa(inputLista)

    if operation == 8:
        a = input("Tal 1: ")
        b = input("Upph�jt till: ")
        print upp(a, b)
    runAgain = raw_input("Vill du r�kna igen?(y/n): ")
    if runAgain == "n":
        running = False
    continue
