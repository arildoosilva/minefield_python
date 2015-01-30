# -*- coding: utf-8 -*-
import random
opcao = raw_input("Opcoes:\n 1 = 10x10\n 2 = 20x20\n 3 = 30x30\nEscolha a dificuldade: ")
tmn = 0
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
    exit    
print "\nO tamanho do campo sera de %d de altura por %d de largura\n" % (tmn, tmn)
campo = [[0 for x in xrange(tmn)] for x in xrange(tmn)]
def criacampo():

    for i in range(0, tmn):
        for j in range(0, tmn):
            campo[i][j]=0
def populavetor():
    for x in range(0, bm):
        rA=random.randint(1, tmn-2)
        rL=random.randint(1, tmn-2)
        campo[rA][rL]=9
def pontos():
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
                campo[i][j]='-'
    for i in range(0, tmn):
        for j in range(0, tmn):
            if (campo[i][j]=='M') or (campo[i][j]=='-'):
                x = x + "%s "  % campo[i][j]
            else:
                x = x + "%d "  % campo[i][j]
        x = x + "\n"
    print "Campo:"
    print x
criacampo()
populavetor()
pontos()
raw_input("Pressione qualquer tecla para fechar a janela")