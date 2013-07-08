from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

compras_url_base = 'http://127.0.0.1:8000/toc_erp_web2py/compras'
driver = webdriver.Firefox()
action = '/inserir_ramo_atividade'
submit_button = "//input[@value='Submit']"
url_inserir_fornecedor = compras_url_base + action


def preenche_campos_obrigatorios_e_submit():
	nome = driver.find_element_by_id("ramoAtividade_nome_ramo")	
	nome.send_keys("ramo qualquer")

	driver.find_element_by_xpath(submit_button).click()

def test_campos_obrigatorios_vazios():

	driver.get(url_inserir_fornecedor)

	nome_error = driver.find_elements_by_id("nome_ramo__error")

	mensagem_erro_padrao = 'enter a value'

	driver.find_element_by_xpath(submit_button).click()

	WebDriverWait(driver, 10)

	for element in nome_error:
		assert element.text == mensagem_erro_padrao

	driver.quit()	

def test_campos_obrigatorios_preenchidos():
	pass	

 	
