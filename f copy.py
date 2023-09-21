from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CEP = '30530130'
CPF = '28011724649'

driver = webdriver.Chrome()
driver.get('https://siatu-tributario.pbh.gov.br/guias/iptu')

n = 0
while n == 0:
    try:
        driver.find_element(By.CSS_SELECTOR,'[id="cep"]').send_keys(CEP)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,'[id="cpfCnpj"]').send_keys(CPF,Keys.ENTER)
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,'[class="btn ml-3 mr-3 float-right btn-primary"]').click()
        n = 1
        input('wait')
    except:
        time.sleep(1)
