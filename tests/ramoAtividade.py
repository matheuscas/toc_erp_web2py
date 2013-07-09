import sys
import os
from os import path
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

sys.path.append('../../../') # we need this to use web2py's modules

from gluon.sql import DAL, Field
from gluon.validators import *

compras_url_base = 'http://127.0.0.1:8000/toc_erp_web2py/compras'
driver = webdriver.Firefox()
action = '/inserir_ramo_atividade'
submit_button = "//input[@value='Submit']"
url_inserir_ramoAtividade = compras_url_base + action
nome_ramoAtividade = "ramo qualquer" 

db_username_postgres = 'postgres'
db_password_postgres = '1234'
db_postgres_url = 'postgres://' + db_username_postgres + ':' + db_password_postgres + '@localhost/dev'

path_to_database = path.join(path.curdir, "../databases")
db_test = DAL(db_postgres_url, folder=path_to_database)
db_test.import_table_definitions(path_to_database)


def preenche_campos_obrigatorios():
	nome = driver.find_element_by_id("ramoAtividade_nome_ramo")	
	nome.send_keys(nome_ramoAtividade)

def test_campos_obrigatorios_vazios():

	driver.get(url_inserir_ramoAtividade)

	nome_error = driver.find_elements_by_id("nome_ramo__error")

	mensagem_erro_padrao = 'enter a value'

	driver.find_element_by_xpath(submit_button).click()

	WebDriverWait(driver, 10)

	for element in nome_error:
		assert element.text == mensagem_erro_padrao

	#driver.quit()	

def test_campos_obrigatorios_preenchidos():	
	
	preenche_campos_obrigatorios()

	descricao = driver.find_element_by_id("ramoAtividade_descricao")
	descricao.send_keys("Uma descricao qualquer")

	driver.find_element_by_xpath(submit_button).click()

	WebDriverWait(driver, 10)

	assert (db_test(db_test.ramoAtividade.nome_ramo == nome_ramoAtividade).select() > 0) == True

	driver.quit()

 	
