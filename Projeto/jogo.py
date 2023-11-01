import random
from palavras import PALAVRAS


# FUNÇÕES

def filtra(lista,num): # Filtra as palavras com a quantidade de letras desejadas
    lisn=[]
    for palavra in lista:
        if len(palavra)==num:
            lisn.append(palavra.lower())
    return lisn


def inicializa(lis):  # Define as configuraões do jogo
    a=random.choice(lis)
    dicio={
        'n': len(a),
        'sorteada' : a,
        'especuladas' : [],
        'tentativas': len(a) + 1  # Usuário pode tentar uma vez para cada letra com um bonus de 1 tentativa
    }
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

a=int(input('Escolha sua dificuldade (1-7) '))
letras=a+2
listaescolhida=filtra(PALAVRAS,letras)

dicio_inicio=inicializa(listaescolhida)
resposta=dicio_inicio['sorteada']

tentativa=0
while tentativa<dicio_inicio['tentativas']:
    chute=input(f'Tente uma palavra com {letras} letras  ')
    if chute not in listaescolhida:
        print('Palavra não conhecida, tente outra')
    else:
        comparar=inidica_posicao(dicio_inicio['sorteada'],chute)
        if comparar == []:
            print(f'essa palavra não possui {letras} letras, tente novamente com uma palavra válida ')
            tentativa=tentativa
        else:
            parcial=''
            for pos in range(len(comparar)):
                if comparar[pos]==0:
                    parcial+=(f'\033[0;32;40m {chute[pos]} \033[m')
                elif comparar[pos]==1:
                    parcial+=(f'\033[0;33;40m {chute[pos]} \033[m')
                elif comparar[pos]==2:
                    parcial+=(f'\033[0;37;40m {chute[pos]} \033[m')
            print(parcial)
            a=comparar.count(0)
            if a==letras:
                tentativa=dicio_inicio['tentativas']
            else:
                tentativa+=1
        if a==letras and tentativa<=dicio_inicio['tentativas']:
            print('\033[1;30;43m PARABÉNS, VOCÊ DESCOBRIU A PALAVRA \033[m')
        elif a!=letras and tentativa==dicio_inicio['tentativas']:
            print(f'\033[1;31;40m que pena, você não descobriu... A resposta era {resposta} \033[m')