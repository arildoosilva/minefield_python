# -*- coding: utf-8 -*-
import random
import re

#global vars
tmn=0
campo=[]
bm=0

def choose():
    opcao = input("Options:\n 1 = 10x10\n 2 = 20x20\n 3 = 30x30\nChoose the size: ")
    global tmn
    global campo
    global bm
    if opcao == "1":
        tmn=10
        bm=random.randint(1, 10)
    elif opcao == "2":
        tmn=20
        bm=random.randint(10, 30)
    elif opcao == "3":
        tmn=30
        bm=random.randint(30, 70)
    else:
        print ("Wrong value")
        exit()
    campo = [[0 for x in range(tmn)] for x in range(tmn)]

def createField(): #fills the field with 0s
    for i in range(0, tmn):
        for j in range(0, tmn):
            campo[i][j]=0
    for x in range(0, bm):
        rA=random.randint(1, tmn-2)
        rL=random.randint(1, tmn-2)
        campo[rA][rL]=9

def points():
    x = ""
    for i in range(0, tmn-1):
        for j in range(0, tmn-1):
            if campo[i][j]>=9:            
                campo[i-1][j-1]+=1; campo[i-1][j]+=1; campo[i-1][j+1]+=1
                campo[i][j-1]+=1;                       campo[i][j+1]+=1
                campo[i+1][j-1]+=1; campo[i+1][j]+=1; campo[i+1][j+1]+=1
    for i in range(0, tmn):
        for j in range(0, tmn):
            if campo[i][j]>=9:
                campo[i][j]='M'
            if campo[i][j]==0:
                campo[i][j]='0'
    for i in range(0, tmn):
        for j in range(0, tmn):
            if (campo[i][j]=='M'):
                x = str(x) + "%s "  % str(campo[i][j])
            else:
                x = str(x) + "%s "  % str(campo[i][j])
                x = x + "\n"
    print ("Field:")
    for x in range(0, tmn):
        line=(''.join(str(campo[x])))
        line=re.sub(r'\W+', " ", line)
        print (line)