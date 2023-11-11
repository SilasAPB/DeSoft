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
    

# Variáveis globais do jogo    
cabecalho = f'''Bem vindo ao Termo-Insper!!!
Regras:
\t- Escolha uma das dificuldades para jogar
\t- Palavras repetidas não serão contabilizadas como tentativas
\t- Use palavras que tenha o número de letras indicado

Código de cores:
\t{clTxt('Amarelo','parcial')} : a palavra possui essa letra mas em outra posição
\t{clTxt('Verde','correta')} : a letra está na posição correta
\t{clTxt('Cinza','neutra')} : a palavra não possui a letra

Sistema de pontos:\n'''

continuar=True

jogomax=0
jogo=1
pontos=0
recorde=0


# UI de Setup
print(cabecalho)
player=input('\nDigite seu nome: ') # Pede o nome do jogador


while continuar:
    os.system('cls||clear')  # Limpar console
    print(cabecalho)
    nivel=int(input('\nEscolha sua dificuldade (1-7) '))


    # Iniciar configurações da partida do jogo
    letras=nivel+2  # Quantidade de letras corresponde ao nivel de dificuldade + 2

    listaescolhida=filtra(PALAVRAS,letras)

    dicio_inicio=inicializa(listaescolhida)
    resposta=dicio_inicio['sorteada']

    correto = False

    tentativa=0
    historico = []


    while tentativa<dicio_inicio['tentativas'] and not correto:
        # Interface principal do jogo
        print(cabecalho)
        print(crTabela(historico,letras,dicio_inicio['tentativas']))
        chute=input(f'Tente uma palavra com {letras} letras: ')

        os.system('cls||clear')  # Limpar console

        
        # Validação do input
        (res,valid,acs) = validaTentativa(chute)
        
        if valid:
            historico.append(res)
            dicio_inicio['especuladas'].append(chute.lower())
        else:
            print(res)
        
        if acs==letras:  # Checa se todas as letras foram acertadas
            correto = True
        elif valid: # Checa se a especulada é valida
            tentativa+=1


    pontos+=(dicio_inicio['tentativas']-tentativa)*nivel  # Contabilização dos pontos


    # Sequência de finalização da partida
    print(crTabela(dicio_inicio['especuladas'],letras,dicio_inicio['tentativas']))
    
    if correto:  # Caso o usuário tenha descoberto a palavra
        print(clTxt(f'PARABÉNS, VOCÊ DESCOBRIU A PALAVRA','correta'))
    
    elif nivel!=letras and tentativa==dicio_inicio['tentativas']:  # Caso o usuário não tenha conseguido achar a palavra
        print(clTxt(f'Que pena, você não descobriu... A resposta era {resposta}','errada'))
    
        if pontos>recorde:
            recorde=pontos
        if jogomax<jogo:
            jogomax=jogo
    
        print(clTxt(f'Sua pontuação de {pontos} foi zerada','errada'))
        pontos=0
        jogo=1


    pergunta=input('Digite 0 para Sair ou Digite 1 para Jogar Novamente  ')

    while pergunta not in ['0','1']:
        print(f'Digite um valor válido {player}!!')
        pergunta=input('Digite 0 para Sair ou Digite 1 para Jogar Novamente  ')
        
    if int(pergunta)==1:  # Iniciar uma nova partida
        continuar=True
        jogo+=1
    elif int(pergunta)==0: # Finalização do jogo
        continuar=False
        if pontos>recorde:
            recorde=pontos
        print(f'Obrigado por jogar {player}, sua maior pontuação foi {recorde}, invicto por {jogomax} jogos')