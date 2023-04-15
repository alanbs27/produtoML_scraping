import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/miband5'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', class_= 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default')

for produto in produtos:
    titulo = produto.find('h2', class_="ui-search-item__title")
    link = produto.find('a', class_="ui-search-link")
    # real = produto.find('span', class_="price-tag-fraction")
    # centavos = produto.find('span', class_="price-tag-cents")
    preco = produto.find('span', class_="price-tag-amount")

    #print(produto.prettify())
    print('titulo do produto:', titulo.text)
    print('link do prooduto:', link['href'])
    print('preco do produto:', preco.text)


    if (centavos):
         print('preco do produto: R$', real.text + ',' + centavos.text)
     else:
         print('preco do produto: R$', real.text)


    print('\n')




