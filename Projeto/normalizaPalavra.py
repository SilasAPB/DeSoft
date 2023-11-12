regras = [
    'âãáàäa',
    'êéèëa',
    'îíìïi',
    'ôõóòöo',
    'ûúùüu',
    'çc'
    ]  # As regras compõem uma lista de caracteres proibidos e, no final, o caractere a ser substituido

# Função para substituir caracteres proibidos da palavra
def normalizaPalavra(palavra,regras = regras):
    normalizada = ''
    for l in palavra:
        regular = True
        for r in regras:
            if l in r[:-1]:
                normalizada+=r[-1]
                regular = False
        if regular:
            normalizada+=l
    return normalizada