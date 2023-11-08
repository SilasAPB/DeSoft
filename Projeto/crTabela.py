# @param Função para imprimir uma tabela com as tentativas do usuário
def crTabela(historico,tamanho,tmax):
    divisa = '-'*((4*tamanho)+1) + '\n'  # Estrutura para dividir as linhas da tabela
    tabela = divisa  # Inicializando uma tabela vazia
    for palavra in historico:
            coluna = '|'
            for l in palavra:
                coluna+= f' {l} |'  # Adicionando todas as colunas de uma linha
            tabela+=coluna+'\n'+divisa  # Adicionando a linha à tabela
    if len(historico)<tmax:  # Caso a quantidade de jogadas do usuário seja menor que a quantidade máxima de tentativas
        tabela+=f'{"|   "*tamanho+"|"}\n{divisa}'*(tmax-len(historico))  # Criar linhas vazias na tabela
    return(tabela)