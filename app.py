# from modelos.restaurante import Restaurante
# from modelos.cardapio.bebida import Bebida
# from modelos.cardapio.prato import Prato

# restaurante_praca = Restaurante('praça', 'Gourmet')
# bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
# bebida_suco.aplicar_desconto()
# prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
# prato_paozinho.aplicar_desconto()

# restaurante_praca.adicionar_no_cardapio(bebida_suco)
# restaurante_praca.adicionar_no_cardapio(prato_paozinho)

# def main():
#     # print(bebida_suco)
#     # print(prato_paozinho)
#     restaurante_praca.exibir_cardapio

# if __name__ == '__main__':
#     main()

import json
import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
else:
    print(f'O erro foi {response.status_code}')


for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)