import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time

# URL base da agenda tributária de 2025
base_url = "https://www.gov.br/receitafederal/pt-br/assuntos/agenda-tributaria/2025"

# Função para obter os links dos meses
def obter_links_meses(url_base):
    response = requests.get(url_base)
    soup = BeautifulSoup(response.content, 'html.parser')
    links_meses = [a['href'] for a in soup.select('a.internal-link') if '/2025/' in a['href']]
    return links_meses

# Função para obter os links das datas com eventos em cada mês
def obter_links_datas(url_mes):
    response = requests.get(url_mes)
    soup = BeautifulSoup(response.content, 'html.parser')
    links_datas = [a['href'] for a in soup.select('a') if '/dia-' in a['href']]
    return links_datas

# Função para extrair tabelas de uma página de data
def extrair_tabelas(url_data):
    response = requests.get(url_data)
    soup = BeautifulSoup(response.content, 'html.parser')
    tabelas_html = soup.find_all('table')
    tabelas = []
    for tabela in tabelas_html:
        df = pd.read_html(str(tabela))[0]
        tabelas.append(df.to_dict(orient='records'))
    return tabelas

# Dicionário para armazenar os dados
dados_agenda = {}

# Obter os links dos meses
links_meses = obter_links_meses(base_url)

# Iterar sobre os meses
for link_mes in links_meses:
    nome_mes = link_mes.split('/')[-1]
    dados_agenda[nome_mes] = {}
    url_mes = link_mes
    links_datas = obter_links_datas(url_mes)
    time.sleep(1)  # Pausa para evitar sobrecarga no servidor

    # Iterar sobre as datas
    for link_data in links_datas:
        nome_data = link_data.split('/')[-1]
        url_data = link_data
        tabelas = extrair_tabelas(url_data)
        dados_agenda[nome_mes][nome_data] = tabelas
        time.sleep(1)

# Salvar os dados em formato JSON
with open("agenda_tributaria_2025.json", "w", encoding="utf-8") as f:
    json.dump(dados_agenda, f, ensure_ascii=False, indent=2)

print("Dados salvos com sucesso em 'agenda_tributaria_2025.json'.")
