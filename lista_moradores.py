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
driver.get('https://uliving-admin.elabs.xyz/unit/Santos/residents')
time.sleep(5)

# Buscando e iterando sobre os headers
th = driver.find_elements('xpath',
                          '/html/body/app-root/app-content/div/div/div[2]/app-list-residents/div[2]/div/div[9]/div/div[2]/table/thead/tr/th')

headers = []
for i in th:
    texto = i.text.strip()
    headers.append(texto)

print(headers)

# Declarando as colunas onde queremos os dados

uh = driver.find_elements('xpath',
                            '/html/body/app-root/app-content/div/div/div[2]/app-list-residents/div[2]/div/div[9]/div/div[2]/table/tbody/tr/td[2]')
nome = driver.find_elements('xpath',
                              '/html/body/app-root/app-content/div/div/div[2]/app-list-residents/div[2]/div/div[9]/div/div[2]/table/tbody/tr/td[3]')
email = driver.find_elements('xpath',
                               '/html/body/app-root/app-content/div/div/div[2]/app-list-residents/div[2]/div/div[9]/div/div[2]/table/tbody/tr/td[4]')

moradores = []
pagination = driver.find_elements('xpath',
                                  '/html/body/app-root/app-content/div/div/div[2]/app-list-residents/div[2]/div/div[9]/ngb-pagination[2]/ul/li')
qtd_pag = driver.find_element('xpath',
                              f'/html/body/app-root/app-content/div/div/div[2]/app-list-residents/div[2]/div/div[9]/ngb-pagination[2]/ul/li[{len(pagination) - 1}]').text.strip()

print(len(pagination))
print(len(qtd_pag))
for n in range(int(qtd_pag)):
    for i in range(len(nome)):
        temporary_data = {'UH': uh[i].text.strip(),
                          'Nome': nome[i].text.strip(),
                          'Email': email[i].text.strip()}
        moradores.append(temporary_data)
    if True:
        driver.find_element('xpath',
                            f'/html/body/app-root/app-content/div/div/div[2]/app-list-residents/div[2]/div/div[9]/ngb-pagination[2]/ul/li[{len(pagination)}]').click()
    else:
        pass
    time.sleep(5)
    uh = driver.find_elements('xpath',
                              '/html/body/app-root/app-content/div/div/div[2]/app-list-residents/div[2]/div/div[9]/div/div[2]/table/tbody/tr/td[2]')
    nome = driver.find_elements('xpath',
                                '/html/body/app-root/app-content/div/div/div[2]/app-list-residents/div[2]/div/div[9]/div/div[2]/table/tbody/tr/td[3]')
    email = driver.find_elements('xpath',
                                 '/html/body/app-root/app-content/div/div/div[2]/app-list-residents/div[2]/div/div[9]/div/div[2]/table/tbody/tr/td[4]')


moradores = pd.DataFrame(moradores)
moradores.to_excel('lista_moradores.xlsx')

driver.close()
