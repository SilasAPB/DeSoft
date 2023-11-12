import requests

def retornaSignificado(palavra):
    response = requests.get(f"https://api.dicionario-aberto.net/word/{palavra}").json()
    
    if response == []:
        return False
    
    significados = []

    for sig in response:
        significados.extend(sig['xml'].split('def>')[1][:-2].split('\n')[1:-1])  # Faz o recorte apenas com os significados do json retornado pela API
    return significados

# while True:
#     palavra = input("\nDigite uma palavra: ").lower()

#     print(retornaSignificado(palavra))
