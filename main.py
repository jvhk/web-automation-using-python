from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

#Automatização web utilizando python

nome = input('Digite um nome do produto: ')
hora = time.strftime('%H:%M:%S', time.localtime())
print(f'[{hora}] Automação iniciada')

print('Automação iniciada')

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.set_window_size(1366,768)
driver.implicitly_wait(5) #await to async pages

driver.get('https://www.google.com/')

busca = driver.find_element(By.NAME, 'q')

busca.send_keys('kabum')

btn_pesquisar = driver.find_element(By.CLASS_NAME, 'gNO89b')

btn_pesquisar.click()

driver.find_element(By.CLASS_NAME,'LC20lb').click()

caixa_texto = driver.find_element(By.ID, 'input-busca')
caixa_texto.send_keys(nome + Keys.ENTER)

nomes = driver.find_elements(By.CLASS_NAME,'nameCard')
precos = driver.find_elements(By.CLASS_NAME,'priceCard')

try:
    l_nomes_produtos = []
    l_precos_produtos = []

    for i in range(len(nomes)):
        l_nomes_produtos.append(nomes[i].text)
        l_precos_produtos.append(precos[i].text)
    
    produtos = {'Produto': l_nomes_produtos, 'Preco': l_precos_produtos}

    dados = pd.DataFrame(data=produtos)
    dados.to_excel(f'{nome}.xlsx', engine='openpyxl', index=False)

    print(f'[{hora}] Planilha criada com sucesso!')
except:
    print('Erro na execução!')