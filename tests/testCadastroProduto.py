import unittest
import time
from testSetup import TestSetup

class TestCadastroProduto(TestSetup):
	"""docstring for TestCadastroProduto"""
	def setUp(self):
		super(TestCadastroProduto,self).setUp()
		compras_url_base = 'http://localhost:8000/toc_erp_web2py/estoque/'
		controller_inserir = 'inserir_produto'
		self.url_inserir_produto = compras_url_base + controller_inserir
		self.nome = 'Um produto qualquer'
		self.unidade_medida = 'UN'
		self.limpa_dados_tabela('marca')
		self.limpa_dados_tabela('fabricante')
		self.limpa_dados_tabela('secao')
		self.limpa_dados_tabela('produto')


	def test_nao_preenche_campos_obrigatorios(self):
		self.driver.get(self.url_inserir_produto)
		self.submit_form()
		time.sleep(0.5)

		mensagem_de_erro = 'enter a value'
		mensagem_de_erro_2 = 'value not in database'

		assert (self.driver.find_element_by_id('nome__error').text == mensagem_de_erro and
				self.driver.find_element_by_id('unidade_medida__error').text == mensagem_de_erro and
				self.driver.find_element_by_id('secao_id__error').text == mensagem_de_erro_2) == True

	def test_preenche_campos_obrigatorios(self):		
		temp_id = self.db_test.secao.insert(nome="secao teste".upper(),situacao='ATIVO')
		self.db_test.commit()

		time.sleep(0.1)

		self.driver.get(self.url_inserir_produto)
		self.driver.find_element_by_id('produto_nome').send_keys(self.nome)
		self.driver.find_element_by_id('produto_unidade_medida').send_keys(self.unidade_medida)
		self.submit_form()

		time.sleep(0.5)

		rows = self.db_test(self.db_test.produto.nome == self.nome.upper()).select()
		assert (len(rows) > 0) == True

	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroProduto('test_nao_preenche_campos_obrigatorios'))
		suite.addTest(TestCadastroProduto('test_preenche_campos_obrigatorios'))
		return suite							