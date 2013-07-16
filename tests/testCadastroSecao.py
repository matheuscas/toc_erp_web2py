import unittest
import time
from testSetup import TestSetup

class TestCadastroSecao(TestSetup):
	"""docstring for TestCadastroSecao"""
	def setUp(self):
		super(TestCadastroSecao,self).setUp()
		estoque_url_base = 'http://127.0.0.1:8000/toc_erp_web2py/estoque'
		acao_inserir = '/inserir_secao'
		self.url_inserir_secao = estoque_url_base + acao_inserir
		self.nome = 'Uma secao qualquer'
		self.descricao = 'um descricao qualquer'
		self.situacao = 'INATIVO'
		self.tabela = 'secao_'

	def exclui_secao_de_teste(self):
		self.db_test(self.db_test.secao.nome == self.nome.upper()).delete()
		self.db_test.commit()	

	def test_inserir_campos_obrigatorios_vazios(self):
		self.driver.get(self.url_inserir_secao)
		self.submit_form()
		time.sleep(0.5)

		mensagem_de_erro = 'enter a value'

		assert self.driver.find_element_by_id('nome__error').text == mensagem_de_erro

	def test_inserir_campos_obrigatorios_preenchidos(self):
		self.driver.get(self.url_inserir_secao)
		self.driver.find_element_by_id(self.tabela + 'nome').send_keys(self.nome)
		self.driver.find_element_by_id(self.tabela + 'descricao').send_keys(self.descricao)
		self.driver.find_element_by_id(self.tabela + 'situacao').send_keys(self.situacao)
		self.submit_form()
		time.sleep(0.1)

		assert (len(self.db_test(self.db_test.secao.nome == self.nome.upper()).select()) > 0) == True

		time.sleep(0.1)

		self.exclui_secao_de_teste()

	def test_inserir_secao_com_nome_repetido(self):
		self.db_test.secao.insert(nome=self.nome.upper(),situacao=self.situacao)
		self.db_test.commit()
		time.sleep(0.1)
		self.driver.get(self.url_inserir_secao)
		self.driver.find_element_by_id(self.tabela + 'nome').send_keys(self.nome)
		self.submit_form()
		time.sleep(0.5)
		mensagem_de_erro = 'value already in database or empty'
		assert self.driver.find_element_by_id('nome__error').text == mensagem_de_erro
		self.exclui_secao_de_teste()


	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroSecao('test_inserir_campos_obrigatorios_vazios'))
		suite.addTest(TestCadastroSecao('test_inserir_campos_obrigatorios_preenchidos'))
		suite.addTest(TestCadastroSecao('test_inserir_secao_com_nome_repetido'))
		return suite	