import random
from palavras import PALAVRAS
def filtra(lista,num):
    lisn=[]
    for palavra in lista:
        som=0
        for letra in palavra:
            som+=1
        if som==num:
            if palavra.lower() not in lisn:
                lisn.append(palavra.lower())
    return lisn


def inicializa(lis):
    a=random.choice(lis)
    soma=0
    for letra in a:
        soma+=1
    dicio={}
    dicio['n']=soma
    dicio['sorteada']=a
    dicio['especuladas']=[]
    dicio['tentativas']=soma+1
    return dicio

def inidica_posicao(sort, espe):
    conts=0
    conte=0
    lis=[]
    for letra in sort:
        conts+=1
    for letra in espe:
        conte+=1
    if conts!=conte:
        return []
    else:
        i=0
        while i<conts:
            if espe[i]==sort[i]:
                lis.append(0)
            elif espe[i] in sort:
                lis.append(1)
            else:
                lis.append(2)
            i+=1

    return lis

a=int(input('Escolha sua dificuldade (1-7)'))
letras=a+2
listaescolhida=filtra(PALAVRAS,letras)

dicio_inicio=inicializa(listaescolhida)

tentativa=0
while tentativa<dicio_inicio['tentativas']:
    chute=input(f'Tente uma palavra com {letras} letras')