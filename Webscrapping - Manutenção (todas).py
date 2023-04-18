from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

options = Options()
options.headless = False
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
driver.get('https://uliving-admin.elabs.xyz/unit/Santos/maintenance/request')
time.sleep(5)
# Filtrando manutenções por abertas
driver.find_element('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[1]/div[1]/div[1]/button').click()
driver.find_element('xpath', '/html/body/ngb-modal-window/div/div/div[2]/div[4]/div/select/option[1]').click()
driver.find_element('xpath', '/html/body/ngb-modal-window/div/div/div[3]/button').click()
time.sleep(5)

# Buscando e iterando sobre os headers
th = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/thead/tr/th')
headers = []
for i in th:
    texto = i.text.strip()
    headers.append(texto)

print(headers)

# Declarando as colunas onde queremos os dados

tr = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr')
nome = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[2]')
quarto = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[3]')
tipo_manutencao = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[4]')
problema = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[5]')
data_criacao = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[6]')
status = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[7]')
tempo_aberto = driver.find_elements('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[8]')

tabela_manutencao = []

for n in range(83):
    print(n)
    for i in range(len(nome)):
        temporary_data = {'Nome': nome[i].text.strip(),
                          'Quarto': quarto[i].text.strip(),
                          'Tipo Manutenção': tipo_manutencao[i].text.strip(),
                          'Problema': problema[i].text.strip(),
                          'Data de Criação': data_criacao[i].text.strip(),
                          'Status': status[i].text.strip(),
                          'Tempo aberto': tempo_aberto[i].text.strip()}
        tabela_manutencao.append(temporary_data)
    if n < 5:
        driver.find_element('xpath',
                            '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/ngb-pagination/ul/li[9]/a').click()
    elif n < 80:
        driver.find_element('xpath',
                            '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/ngb-pagination/ul/li[11]/a').click()
    elif n >= 80:
        driver.find_element('xpath',
                            '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/ngb-pagination/ul/li[6]/a').click()
    else:
        pass
    time.sleep(5)
    tr = driver.find_elements('xpath',
                              '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr')
    nome = driver.find_elements('xpath',
                                '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[2]')
    quarto = driver.find_elements('xpath',
                                  '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[3]')
    tipo_manutencao = driver.find_elements('xpath',
                                           '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[4]')
    problema = driver.find_elements('xpath',
                                    '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[5]')
    data_criacao = driver.find_elements('xpath',
                                        '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[6]')
    status = driver.find_elements('xpath',
                                  '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[7]')
    tempo_aberto = driver.find_elements('xpath',
                                        '/html/body/app-root/app-content/div/div/div[2]/app-list-maintenances/div[2]/div/div/div/div[2]/table/tbody/tr/td[8]')

tabela_manutencao = pd.DataFrame(tabela_manutencao)
tabela_manutencao.to_excel('Manutencao.xlsx')

driver.close()


