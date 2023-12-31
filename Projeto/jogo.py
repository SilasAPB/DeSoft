import os
import json
from palavrasExtendido import PALAVRAS


# Funções em módulo
from dicioApi import retornaSignificado
from crTabela import crTabela
from normalizaPalavra import normalizaPalavra
from clTxt import clTxt
from logo import logo
from inidicaposicao import inidica_posicao
from filtra import filtra
from inicializa import inicializa

# FUNÇÕES
def validaTentativa(chute):
    for l in chute:
        if l in proibidas:
            return (clTxt('Essa palavra contém caracteres especiais proibidos ou números','errada'),False,0)
    if chute not in listaescolhida and len(chute) == letras:  # Verifica se a entrada é uma palavra dentro da lista de palavras
        return (clTxt('Palavra não conhecida, tente outra','errada'),False,0)
    elif chute in dicio_inicio['especuladas']:
        return (clTxt('Essa palavra já foi digitada. Digite novamente!','errada'),False,0)
    else:
        comparar=inidica_posicao(resposta,chute)
        if comparar == []:
            return(clTxt(f'Essa palavra não possui {letras} letras, tente novamente com uma palavra válida','errada'),False,0)
        else:
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
cabecalho = f'''
{logo()}
Bem vindo ao Termo-Insper!!!

Regras:
\t- Escolha uma das dificuldades para jogar
\t- Palavras repetidas não serão contabilizadas como tentativas
\t- Use palavras que tenha o número de letras indicado
\t- Para desistir da partida, digite \"desistir\"
\t- Para pedir uma dica, digite \"definicao\". Cada dica custará 1 tentativa.

Código de cores:
\t{clTxt('Amarelo','parcial')} : a palavra possui essa letra mas em outra posição
\t{clTxt('Verde','correta')} : a letra está na posição correta
\t{clTxt('Cinza','neutra')} : a palavra não possui a letra

Sistema de pontos:
\t - O número de tentativas é dado pelo dificuldade escolhida
\t - Os pontos são dados pelo número de tentativas maximas menos o número de chutes errados multiplicado pelo nível:
\t\t Por exemplo: Dificuldade 1 (4 tentativas):
\t\t\t Correta: rua
\t\t\t Tentativas: sol - lua - rua
\t\t\t Foram 2 tentativas erradas até acertar, logo:
\t\t\t\t Pontos: (4-2) X 1 = 2
\t\t - Os pontos são somados a cada partida até que o jogador perca ou desista
\t\t - No caso de derrota, se o jogador quiser jogar de novo sua pontuação será zerada
\t\t - Pontuações mais altas serão salvas como recordes!!

{clTxt('BOA SORTE!!!!','azul')}'''

continuar=True

jogomax=0
jogo=1
pontos=0
recorde=0

proibidas = '\"\'!@#$%^&*()-+?_=,<>/\\^~0123456789'

# Ler placar de arquivo externo
placar = {}
if os.path.exists('./placar.json'):  # Checando se o arquivo existe
    with open('./placar.json', 'r') as data:
        placar = json.load(data)  # Lendo o arquivo

# UI de Setup
os.system('cls||clear')  # Limpar console
print(cabecalho)
player=input('\nDigite seu nome: ') # Pede o nome do jogador
while player == '':
        print(clTxt("\nNome Invalido!",'errada'))
        player=input('\nDigite seu nome: ')


while continuar:
    os.system('cls||clear')  # Limpar console
    
    nivel=int(input('\nEscolha sua dificuldade (1-7) '))
    while nivel < 1 or nivel > 7:
        print(clTxt("\nValor Invalido!",'errada'))
        nivel=int(input('\nEscolha sua dificuldade (1-7) '))

    # Iniciar configurações da partida do jogo
    letras=nivel+2  # Quantidade de letras corresponde ao nivel de dificuldade + 2

    # Cria lista de palavras
    listaescolhida=filtra(PALAVRAS,letras)

    # Inicializa configurações da partida
    dicio_inicio=inicializa(listaescolhida)

    # Salva palavra sorteada sem normalização
    original = dicio_inicio['sorteada']
    
    # Normalização da lista e da palavra sorteada
    for i in range(len(listaescolhida)):
        listaescolhida[i] = normalizaPalavra(listaescolhida[i])
    resposta=normalizaPalavra(original)

    correto = False

    tentativa=0
    historico = []
    dica = 0

    os.system('cls||clear')  # Limpar console


    # Loop principal de jogo
    while tentativa<dicio_inicio['tentativas'] and not correto:
        # Interface principal do jogo
        if dica:
            print('Dicas:')
            for i in range(abs(dica)):
                print(f'\t{definicao[i]}')
        
        
        print(crTabela(historico,letras,dicio_inicio['tentativas']))
        chute = normalizaPalavra(input(f'Tente uma palavra com {letras} letras: ').strip())
        
        if chute == 'desistir': # Caso o usuário desista
            tentativa = dicio_inicio['tentativas'] #cria a condição para fim da rodada
            os.system('cls||clear')  # Limpar console
            continue #retorna no começo do while 

        if chute == 'definicao':
            os.system('cls||clear')  # Limpar console
            
            if dica == 0:  # Só é solicidada a api de dicionário da primeira vez
                print(clTxt('\nPesquisando...','parcial'))
                definicao = retornaSignificado(original)
                os.system('cls||clear')  # Limpar console

                if not definicao:  # Caso a api não tenha achado uma definição, o valor retornado pela função é falso
                    definicao = ["Eita! não achamos uma definição para essa palavra..."]
                    dica = -1

            if dica < len(definicao) and dica >= 0:  # Caso ainda tenham dicas disponíveis
                dica+=1
                tentativa+=1
                historico.append('-'*letras)
            elif dica > 0 and dica == len(definicao): 
                print(clTxt('Todas as dicas disponíveis foram utilizadas','errada'))
            continue


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
    print(crTabela(historico,letras,dicio_inicio['tentativas']))
    
    if correto:  # Caso o usuário tenha descoberto a palavra
        print(clTxt(f'PARABÉNS, VOCÊ DESCOBRIU A PALAVRA','correta'))
        if pontos>recorde:
            recorde=pontos

    elif nivel!=letras and tentativa==dicio_inicio['tentativas'] and chute=='desistir':  # Caso o usuário tenha desistido da rodada
        print(clTxt(f'Que pena, você não descobriu... A resposta era {resposta}','errada'))
        jogo=0
        if pontos>recorde:
            recorde=pontos


        print(clTxt(f'Sua pontuação foi diminuida em {nivel} pontos','errada'))
        pontos-=nivel

    
    elif nivel!=letras and tentativa==dicio_inicio['tentativas'] :  # Caso o usuário não tenha conseguido achar a palavra
        print(clTxt(f'Que pena, você não descobriu... A resposta era {resposta}','errada'))
        jogo=0
        if pontos>recorde:
            recorde=pontos

        
        if pontos>0:
            print(clTxt(f'Sua pontuação de {pontos} foi zerada','errada'))#Zera a pontuação em caso de derrota e saldo positivo
            pontos=0


    pergunta=input('Digite 0 para Sair ou Digite 1 para Jogar Novamente  ')

    while pergunta not in ['0','1']:
        print(clTxt(f'\nDigite um valor válido {player}!!\n','errada'))
        pergunta=input('Digite 0 para Sair ou Digite 1 para Jogar Novamente  ')
        
    if int(pergunta)==1:  # Iniciar uma nova partida
        continuar=True
        if correto:
            jogomax=jogo
        jogo+=1

    elif int(pergunta)==0: # Finalização do jogo
        continuar=False
        if pontos>recorde:
            recorde=pontos
        if correto:
            jogomax=jogo
        
        placar[player] = [recorde,jogomax]

        jsonObject = json.dumps(placar,indent=4)
        with open('placar.json', 'w') as data:
            data.write(jsonObject)
        

        print(f'\nObrigado por jogar, {player}. Sua maior pontuação foi {recorde}, e conseguiu ficar invicto por {jogomax} jogos!!')
        print('\nO placar final foi:')
        for nome,dados in placar.items():
            print(f'\t[{nome}] {dados[0]} pontos | {dados[1]} partidas concecutivas')
        