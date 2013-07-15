import unittest
import time
from testSetup import TestSetUp

class TestCadastroEmbalagem(TestSetUp):
	"""docstring for TestCadastroEmbalagem"""
	def setUp(self):
		super(TestCadastroEmbalagem, self).setUp()
		fiscal_url_base = 'http://127.0.0.1:8000/toc_erp_web2py/estoque'
		acao_inserir = '/inserir_embalagem'
		self.url_inserir_imposto = fiscal_url_base + acao_inserir
		self.nome = 'Mais uma embalagem qualquer'
		self.unidade_medida = 'CX'
		self.quantidade_casas_decimais = 1
		self.tabela = 'embalagem_'

	def test_inserir_campos_obrigatorios_vazios(self):
		self.driver.get(self.url_inserir_imposto)
		self.submit_form()
		time.sleep(0.5)

		nome_error = self.driver.find_element_by_id('nome__error')
		unidade_medida_error = self.driver.find_element_by_id('unidade_medida__error')

		mensagem_error = 'enter a value'

		assert (nome_error.text == mensagem_error and unidade_medida_error.text == mensagem_error) == True


	def test_inserir_campos_obrigatorios_preenchidos(self):
		pass

	def test_inserir_nome_da_embalagem_repetido(self):
		pass

	def test_inserir_unidade_medida_e_quantidade_casas_decimais_repetidos(self):
		pass

	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroEmbalagem('test_inserir_campos_obrigatorios_vazios'))
		return suite	

						
			
