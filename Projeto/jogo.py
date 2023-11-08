import random
import os
from palavras import PALAVRAS


# Funções em módulo
from crTabela import crTabela

cores = {
    'correta' : '\033[0;32;40m',
    'parcial' : '\033[0;33;40m',
    'neutra' : '\033[0;37;40m',
    'padrao' : '\033[m',
    'errada' : '\033[1;31;40m'
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

    lis=[]
    if len(sort)!=len(espe):
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


def clTxt(texto,cor):  # Adicionar caracteres coloridos
    return cores[cor]+texto+cores['padrao']

def validaTentativa(chute):
    if chute not in listaescolhida:  # Verifica se a entrada é uma palavra dentro da lista de palavras
        return ('Palavra não conhecida, tente outra',False,0)
    elif chute in dicio_inicio['especuladas']:
        return ('Essa palavra já foi digitada. Digite novamente!',False,0)
    else:
        comparar=inidica_posicao(dicio_inicio['sorteada'],chute)
        if comparar == []:
            return(f'essa palavra não possui {letras} letras, tente novamente com uma palavra válida ',False,0)
        else:
            global tentativa
            
            parcial=[]
            for pos in range(len(comparar)):
                if comparar[pos]==0:
                    parcial.append(clTxt(chute[pos],'correta'))
                elif comparar[pos]==1:
                    parcial.append(clTxt(chute[pos],'parcial'))
                elif comparar[pos]==2:
                    parcial.append(clTxt(chute[pos],'neutra'))

            return (parcial,True,comparar.count(0))
    
    

os.system('cls||clear')  # Limpar console

print('Bem vindo ao Termo Insper!!!\n\n\n\n')

player=input('Digite seu nome: ') #pede o nome do jogador

continuar=True

jogo=1 
pontos=0
pontosfinais=0

while continuar:

    nivel=int(input('Escolha sua dificuldade (1-7) '))

    letras=nivel+2  # Quantidade de letras corresponde ao nivel de dificuldade + 2

    listaescolhida=filtra(PALAVRAS,letras)

    dicio_inicio=inicializa(listaescolhida)
    resposta=dicio_inicio['sorteada']

    correto = False

    tentativa=0
    historico = []
    while tentativa<dicio_inicio['tentativas'] and not correto:

        print(crTabela(historico,letras,dicio_inicio['tentativas']))
        
        chute=input(f'Tente uma palavra com {letras} letras: ')

        os.system('cls||clear')  # Limpar console

        (res,valid,acs) = validaTentativa(chute)
        if valid:
            historico.append(res)
            dicio_inicio['especuladas'].append(chute.lower())
        else:
            print(res)
        

        if acs==letras:  # Checa se todas as letras foram acertadas
            correto = True
        elif valid: #checa se a especulada é valida
            tentativa+=1

    pontos+=(dicio_inicio['tentativas']-tentativa)*nivel
    # Sequência fora do loop de jogo
    print(crTabela(dicio_inicio['especuladas'],letras,dicio_inicio['tentativas']))
    if correto:  # Caso o usuário tenha descoberto a palavra
        print(f'{cores["correta"]} PARABÉNS, VOCÊ DESCOBRIU A PALAVRA {cores["neutra"]}')
    elif nivel!=letras and tentativa==dicio_inicio['tentativas']:  # Caso o usuário não tenha conseguido achar a palavra
        print(f'{cores["errada"]} Que pena, você não descobriu... A resposta era {resposta}{cores["neutra"]}')

    pergunta=input('Digite 0 para Sair ou Digite 1 para Jogar Novamente  ')

    validos=[0,1]

    while int(pergunta) not in validos:
        print(f'Digite um valor válido {player}!!')
        pergunta=input('Digite 0 para Sair ou Digite 1 para Jogar Novamente  ')
        
    if int(pergunta)==1:
        continuar=True
        jogo+=1
    elif int(pergunta)==0: #finalização do jogo
        continuar=False
        pontosfinais=pontos/jogo
        print(f'Obrigado por jogar {player}, sua pontuação final foi {pontosfinais}')