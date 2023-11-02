import random
from palavras import PALAVRAS

cores = {
    'correta' : '\033[0;32;40m',
    'parcial' : '\033[0;33;40m',
    'neutra' : '\033[0;37;40m',
    'padrao' : '\033[m'
}

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

def inidica_posicao(sort, espe):  # ("Palavra sorteada pelo sistema", "Palavra especulada pelo usuário")
    # 
    lis=[]
    if len(sort)==len(espe):
        return []
    else:
        for i in range(len(sort)):
            if espe[i]==sort[i]:
                lis.append(0)  # Letra está na posição correta
            elif espe[i] in sort:
                lis.append(1)  # Letra existe na palavra sorteada
            else:
                lis.append(2)  # Letra não existe na palavra sorteada
    return lis


def clTxt(cor,texto):
    return cores[cor]+texto+cores['padrao']

def validaTentativa(chute):
    if chute not in listaescolhida:  # Verifica se a entrada é uma palavra
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

def ptTabela(historico,tamanho):
    tabela = '-'*((3*tamanho)-1)
    if len(historico):
        for palavra in historico:
            coluna = '|'
            for l in palavra:
                coluna+= l+'|'
            tabela+=coluna
        
    


a=int(input('Escolha sua dificuldade (1-7) '))

letras=a+2  # Quantidade de letras corresponde ao nivel de dificuldade + 2

listaescolhida=filtra(PALAVRAS,letras)

dicio_inicio=inicializa(listaescolhida)
resposta=dicio_inicio['sorteada']

tentativa=0
while tentativa<dicio_inicio['tentativas']:
    chute=input(f'Tente uma palavra com {letras} letras  ')
    validaTentativa(chute)
    dicio_inicio['especuladas']
    ptTabela(chute,dicio_inicio['especuladas'],dicio_inicio['tentativas'])