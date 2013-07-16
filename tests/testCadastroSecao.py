import unittest
import time
from testSetup import TestSetUp

class TestCadastroSecao(TestSetUp):
	"""docstring for TestCadastroSecao"""
	def setUp(self):
		super(TestCadastroSecao,self).setUp()
		estoque_url_base = 'http://127.0.0.1:8000/toc_erp_web2py/estoque'
		acao_inserir = '/inserir_secao'
		self.url_inserir_secao = estoque_url_base + acao_inserir
		self.nome = 'Uma secao qualquer'
		self.descricao = 'um descricao qualquer'
		self.tabela = 'secao_'

	def test_inserir_campos_obrigatorios_vazios(self):
		self.driver.get(self.url_inserir_secao)
		self.submit_form()
		time.sleep(0.5)

		mensagem_de_erro = 'enter a value'

		assert self.driver.find_element_by_id('nome__error').text == mensagem_de_erro

	def test_inserir_campos_obrigatorios_preenchidos(self):
		pass

	def test_inserir_secao_com_nome_repetido(self):
		pass			

	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroSecao('test_inserir_campos_obrigatorios_vazios'))
		return suite	