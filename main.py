
from attr import attrs
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep, time

# DECLARANDO NOSSO NAVEGADOR E O TAMANHO DA JANELA
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
'''window-size = 1000,1000'''

# ENTRANDO NO SITE DA NOTICIARIO 
driver.get("https://g1.globo.com/")
sleep(2)
x = driver.find_element_by_tag_name('input')
x.send_keys('rio de janeiro')
x.submit()
sleep(0.5)

# NOVAS
recente = driver.find_element_by_xpath('//*[@id="content"]/div/div/ul/li[1]/ul/li[1]/a')
y = recente.click()
sleep(2)

page_content = driver.page_source
site = BeautifulSoup(page_content, 'html.parser')

dados_noticiario = []

materias = site.findAll('div', 'feed-post bstn-item-shape type-materia')


for materia in materias:

    
    
    materia_url = materia.find('a', href=True)

    materia_titulo = materia.find('a',attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
    materia_titulo = materia_titulo.text

    materia_detalhe = materia.find('div', attrs={'class':'feed-post-body-resumo'})
    materia_detalhe = materia_detalhe.text

    # materia_data = materia.findAll('span'[-1])
    # materia_data = materia_data.text

    print('link da matéria:', materia_url['href'])
    print('titulo da matéria:', materia_titulo)
    print('mais detalhes:', materia_detalhe)
    # print('tempo:',materia_data)
    print()
    dados_noticiario.append([materia_url, materia_titulo, materia_detalhe])
import pandas as pd
dados = (pd.DataFrame(dados_noticiario, columns=('link matéria', 'titulo matéria', 'detalhes matéria')))
dados.to_csv('NoticiasRecentes.csv', index=False)
    
