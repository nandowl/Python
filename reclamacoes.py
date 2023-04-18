from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options, service=servico)

# Acessar o site alvo
driver.get('https://uliving-admin.elabs.xyz/login')

# Autenticar no site com o Selenium
driver.find_element('xpath',
                       '/html/body/app-root/app-login/div/div/div/div[2]/div/div/div/form/div[1]/input').clear()
driver.find_element('xpath',
                       '/html/body/app-root/app-login/div/div/div/div[2]/div/div/div/form/div[1]/input').send_keys('xxxxxxxxxxxxx')
driver.find_element('xpath',
                       '/html/body/app-root/app-login/div/div/div/div[2]/div/div/div/form/div[2]/input').send_keys('xxxxxxxxxxxxx')
driver.find_element('xpath',
                       '/html/body/app-root/app-login/div/div/div/div[2]/div/div/div/form/div[3]/div/button').click()
time.sleep(5)
# Acessando a página alvo
driver.get('https://uliving-admin.elabs.xyz/unit/Santos/feedback/complainings')
time.sleep(5)

# Buscando e iterando sobre os headers
th = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/thead/tr/th')
headers = []
for i in th:
    texto = i.text.strip()
    headers.append(texto)

# Declarando as colunas onde queremos os dados

tipo = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[1]')
data = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[2]')
usuario = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[3]')
mensagem = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[4]')
resposta = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[5]')
estado = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[6]')

reclamacoes = []
pagination = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/ngb-pagination/ul/li')

for n in range(len(pagination) - 2):
    for i in range(len(usuario)):
        temporary_data = {'Tipo': tipo[i].text.strip(),
                          'Data': data[i].text.strip(),
                          'Usuário': usuario[i].text.strip(),
                          'Mensagem': mensagem[i].text.strip(),
                          'Resposta': resposta[i].text.strip(),
                          'Estado': estado[i].text.strip()}
        reclamacoes.append(temporary_data)
    if True:
        driver.find_element('xpath', f'/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/ngb-pagination/ul/li[{len(pagination)}]').click()
    else:
        break
    time.sleep(3)
    tipo = driver.find_elements('xpath',
                                '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[1]')
    data = driver.find_elements('xpath',
                                '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[2]')
    usuario = driver.find_elements('xpath',
                                   '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[3]')
    mensagem = driver.find_elements('xpath',
                                    '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[4]')
    resposta = driver.find_elements('xpath',
                                    '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[5]')
    estado = driver.find_elements('xpath',
                                  '/html/body/app-root/app-content/div/div/div[2]/app-list-suggestions/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[6]')

reclamacoes = pd.DataFrame(reclamacoes)
reclamacoes.to_excel('reclamacoes.xlsx')

driver.close()

