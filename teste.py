import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

navegador.get("https:google.com.br")
navegador.maximize_window()
time.sleep(3)
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("teste")
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

navegador.close()



def teste1():
    vendas=1000

    if vendas >= 1000:
        print("Ganhou")
    else:
        print("Não Ganhou")