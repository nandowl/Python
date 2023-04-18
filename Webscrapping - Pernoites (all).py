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
                    '/html/body/app-root/app-login/div/div/div/div[2]/div/div/div/form/div[1]/input').send_keys(
    'xxxxxxxxxxxxx')
driver.find_element('xpath',
                    '/html/body/app-root/app-login/div/div/div/div[2]/div/div/div/form/div[2]/input').send_keys(
    'xxxxxxxxxxxxx')
driver.find_element('xpath',
                    '/html/body/app-root/app-login/div/div/div/div[2]/div/div/div/form/div[3]/div/button').click()
time.sleep(5)
# Acessando a página alvo
driver.get('https://uliving-admin.elabs.xyz/unit/Santos/visits')
time.sleep(5)

# Filtrando todas as manutenções por data
driver.find_element('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[1]/div[2]/div/input').send_keys('01/01/2021')
driver.find_element('xpath', '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[1]/div[4]/button').click()
time.sleep(5)
# Buscando e iterando sobre os headers
th = driver.find_elements('xpath',
                          '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/thead/tr/th')

headers = []
for i in th:
    texto = i.text.strip()
    headers.append(texto)

print(headers)

# Declarando as colunas onde queremos os dados

nome = driver.find_elements('xpath',
                            '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[2]')
quarto = driver.find_elements('xpath',
                              '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[3]')
visitante = driver.find_elements('xpath',
                                       '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[4]')
documento = driver.find_elements('xpath',
                                '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[5]')
data_entrada = driver.find_elements('xpath',
                                    '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[6]')
data_saida = driver.find_elements('xpath',
                              '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[7]')
data_saida_real = driver.find_elements('xpath',
                                    '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[8]')
status = driver.find_elements('xpath',
                                    '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[9]')

pernoites = []
pagination = driver.find_elements('xpath',
                                  '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/ngb-pagination/ul/li')
qtd_pag = driver.find_element('xpath',
                              f'/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/ngb-pagination/ul/li[{len(pagination) - 1}]').text.strip()

print(len(pagination))
print(len(qtd_pag))
for n in range(int(qtd_pag)):
    for i in range(len(nome)):
        temporary_data = {'Nome': nome[i].text.strip(),
                          'Quarto': quarto[i].text.strip(),
                          'Visitante': visitante[i].text.strip(),
                          'Documento': documento[i].text.strip(),
                          'Data de Entrada': data_entrada[i].text.strip(),
                          'Data de Saída': data_saida[i].text.strip(),
                          'Data saída real': data_saida_real[i].text.strip(),
                          'Status': status[i].text.strip()}
        pernoites.append(temporary_data)
    if True:
        driver.find_element('xpath',
                            f'/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/ngb-pagination/ul/li[{len(pagination)}]').click()
    else:
        pass
    time.sleep(5)
    nome = driver.find_elements('xpath',
                                '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[2]')
    quarto = driver.find_elements('xpath',
                                  '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[3]')
    visitante = driver.find_elements('xpath',
                                     '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[4]')
    documento = driver.find_elements('xpath',
                                     '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[5]')
    data_entrada = driver.find_elements('xpath',
                                        '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[6]')
    data_saida = driver.find_elements('xpath',
                                      '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[7]')
    data_saida_real = driver.find_elements('xpath',
                                           '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[8]')
    status = driver.find_elements('xpath',
                                  '/html/body/app-root/app-content/div/div/div[2]/app-list-visitor/div[2]/div[2]/div[6]/div/div[2]/table/tbody/tr/td[9]')

pernoites = pd.DataFrame(pernoites)
pernoites.to_excel('Pernoites.xlsx')

driver.close()
