import unittest
import time
from testSetup import TestSetUp

class TestCadastroImposto(TestSetUp):
	"""docstring for TestCadastroImposto"""
	def setUp(self):
		super(TestCadastroImposto,self).setUp()
		fiscal_url_base = 'http://127.0.0.1:8000/toc_erp_web2py/fiscal'
		acao_inserir = '/inserir_imposto'
		self.url_inserir_imposto = fiscal_url_base + acao_inserir
		self.nome_imposto = 'Imposto x'
		self.tipo_imposto = 'IPI'
		self.tipo_aliquota_imposto = 'Tributado'
		self.percentual_imposto = 7
		self.situacao_imposto = 'ATIVO'
		self.tabela = 'imposto_'

	def submmit_form(self):
		self.driver.find_element_by_xpath(self.submit_button).click()

	def preenche_campos_obrigatorios_e_submit(self):

		campo_nome_imposto = self.driver.find_element_by_id(self.tabela + 'nome_imposto')
		campo_tipo_imposto = self.driver.find_element_by_id(self.tabela + 'tipo_imposto')
		campo_tipo_aliquota_imposto = self.driver.find_element_by_id(self.tabela + 'tipo_aliquota_imposto')
		campo_percentual_imposto = self.driver.find_element_by_id(self.tabela + 'percentual_imposto')
		campo_situacao_imposto = self.driver.find_element_by_id(self.tabela + 'situacao_imposto')

		campo_nome_imposto.send_keys(self.nome_imposto)
		campo_tipo_imposto.send_keys(self.tipo_imposto)
		campo_tipo_aliquota_imposto.send_keys(self.tipo_aliquota_imposto)
		campo_percentual_imposto.send_keys(self.percentual_imposto)
		campo_situacao_imposto.send_keys(self.situacao_imposto)

		self.submmit_form()

	def exclui_imposto_de_teste(self):
		self.db_test(self.db_test.imposto.tipo_aliquota_imposto == self.tipo_aliquota_imposto and
			self.db_test.imposto.tipo_imposto == self.tipo_imposto and 
			self.db_test.imposto.percentual_imposto == self.percentual_imposto).delete()

		self.db_test.commit()		

	def test_inserir_campos_obrigatorios_vazios(self):
		self.driver.get(self.url_inserir_imposto)
		self.submmit_form()
		time.sleep(0.5)

		nome_imposto_erro = self.driver.find_element_by_id('nome_imposto__error')
		tipo_imposto_erro = self.driver.find_element_by_id('tipo_imposto__error')
		tipo_aliquota_erro = self.driver.find_element_by_id('tipo_aliquota_imposto__error')
		percentual_erro = self.driver.find_element_by_id('percentual_imposto__error')
		situacao_erro = self.driver.find_element_by_id('situacao_imposto__error')

		mensagem_erro = 'enter a value'
		mensagem_erro_2 = 'value not allowed'
		mensagem_erro_3 = 'enter a number between -1e+10 and 1e+10'

		assert_nome = (nome_imposto_erro.text == mensagem_erro)
		assert_tipo = (tipo_imposto_erro.text == mensagem_erro_2)
		assert_aliquota = (tipo_aliquota_erro.text == mensagem_erro_2)
		assert_percentual = (percentual_erro.text == mensagem_erro_3)
		assert_situacao = (situacao_erro.text == mensagem_erro_2)

		assert (assert_nome and assert_tipo and assert_aliquota and assert_percentual) == True

	def test_inserir_campos_obrigatorios_preenchidos(self):		
		self.driver.get(self.url_inserir_imposto)
		self.preenche_campos_obrigatorios_e_submit()
		time.sleep(0.1)
		rows = self.db_test(self.db_test.imposto.tipo_aliquota_imposto == self.tipo_aliquota_imposto and
			self.db_test.imposto.tipo_imposto == self.tipo_imposto and 
			self.db_test.imposto.percentual_imposto == self.percentual_imposto).select()

		assert (len(rows) > 0) == True
		self.exclui_imposto_de_teste()

	def test_inserir_nome_do_imposto_repetido(self):
		
		self.db_test.imposto.insert(nome_imposto=self.nome_imposto.upper(), tipo_imposto=self.tipo_imposto,
			tipo_aliquota_imposto=self.tipo_aliquota_imposto, situacao_imposto=self.situacao_imposto,
			percentual_imposto=self.percentual_imposto)
		self.db_test.commit()

		time.sleep(0.1)

		self.driver.get(self.url_inserir_imposto)
		self.preenche_campos_obrigatorios_e_submit()

		time.sleep(0.5)

		mensagem_erro_padrao = 'value already in database or empty'
		nome_imposto_erro = self.driver.find_element_by_id('nome_imposto__error')
		assert nome_imposto_erro.text == mensagem_erro_padrao

		self.exclui_imposto_de_teste()
	
	def test_inserir_tipo_imposto_e_tipo_aliquota_e_percentual_repetidos(self):
		pass

	def test_inserir_percentual_abaixo_de_zero(self):
		pass

	def test_inserir_percentual_acima_de_cem(self):
		pass

	def test_inserir_percentual_entre_zero_e_cem(self):
		pass			

	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroImposto('test_inserir_campos_obrigatorios_vazios'))
		suite.addTest(TestCadastroImposto('test_inserir_campos_obrigatorios_preenchidos'))
		suite.addTest(TestCadastroImposto('test_inserir_nome_do_imposto_repetido'))
		return suite				