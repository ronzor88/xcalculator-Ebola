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
