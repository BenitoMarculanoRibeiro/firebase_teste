import requests
import json

link = "https://teste-firebase-17f6a-default-rtdb.firebaseio.com/"


def adicionar_venda(url, dado):
    requisicao = requests.post(f'{url}/Vendas/.json', data=json.dumps(dado))
    print(requisicao)
    print(requisicao.text)


# &equalTo=1
def ler_vendas(url):
    requisicao = requests.get(f'{url}/Vendas/.json')
    print(requisicao)
    dic_requisicao = requisicao.json()
    print(dic_requisicao)


def ler_venda(url):
    requisicao = requests.get(f'{url}/Vendas/.json?orderBy="preco"&limitToFirst=1&endAt=3&print=pretty')
    print(requisicao)
    dic_requisicao = requisicao.json()
    print(dic_requisicao)


def editar_venda(url, dado):
    requisicao = requests.patch(f'{url}/Vendas/-Mz6McZuCkCVd1AqlL3e/.json', data=json.dumps(dado))
    print(requisicao)
    print(requisicao.text)


def apagar_venda(url, id_venda):
    requisicao = requests.delete(f'{url}/Vendas/{id_venda}/.json')
    print(requisicao)
    print(requisicao.text)


dados = {'cliente': 'rodolfo'}
# editar_venda(link, dados)
ler_venda(link)
