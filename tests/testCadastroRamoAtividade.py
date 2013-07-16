import unittest
import time
from random import randint
from testSetup import TestSetup

class TestCadastroRamoAtividade(TestSetup):
	"""docstring for TestCadastroRamoAtividade"""
	def setUp(self):
		super(TestCadastroRamoAtividade,self).setUp()
		self.compras_url_base = 'http://127.0.0.1:8000/toc_erp_web2py/compras'
		self.acao_inserir = '/inserir_ramo_atividade'
		self.acao_atualizar = '/atualizar_ramo_atividade'
		self.url_inserir_ramoAtividade = self.compras_url_base + self.acao_inserir
		self.url_atualizar_ramoAtividade = self.compras_url_base + self.acao_atualizar
		self.nome_ramoAtividade = "ramo qualquer_test" 

	def preenche_campos_obrigatorios(self):
		nome = self.driver.find_element_by_id("ramoAtividade_nome_ramo")	
		nome.send_keys(self.nome_ramoAtividade)	

	def exclui_ramo_ativdade_de_teste(self):
		self.db_test(self.db_test.ramoAtividade.nome_ramo == self.nome_ramoAtividade).delete()
		self.db_test.commit()	

	def test_inserir_campos_obrigatorios_vazios(self):
		self.driver.get(self.url_inserir_ramoAtividade)
		self.driver.find_element_by_xpath(self.submit_button).click()
		time.sleep(0.5)
		nome_error = self.driver.find_element_by_id("nome_ramo__error")
		mensagem_erro_padrao = 'enter a value'
		assert nome_error.text == mensagem_erro_padrao
	
	def test_inserir_campos_obrigatorios_preenchidos(self):
		self.driver.get(self.url_inserir_ramoAtividade)
		rand = randint(1,1000)
		self.nome_ramoAtividade = self.nome_ramoAtividade + str(rand)
		self.preenche_campos_obrigatorios()
		self.driver.find_element_by_xpath(self.submit_button).click()
		time.sleep(0.1)
		rows = self.db_test(self.db_test.ramoAtividade.nome_ramo == self.nome_ramoAtividade).select()
		assert rows[0].nome_ramo == self.nome_ramoAtividade
		self.exclui_ramo_ativdade_de_teste()

	@classmethod	
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroRamoAtividade('test_inserir_campos_obrigatorios_vazios'))
		suite.addTest(TestCadastroRamoAtividade('test_inserir_campos_obrigatorios_preenchidos'))
		return suite	
		