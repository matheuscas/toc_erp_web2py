import unittest
import time
from testSetup import TestSetup

class TestCadastroSubsecao(TestSetup):
	"""docstring for TestCadastroSubsecao"""
	def setUp(self):
		super(TestCadastroSubsecao,self).setUp()
		estoque_url_base = 'http://127.0.0.1:8000/toc_erp_web2py/estoque'
		acao_inserir = '/inserir_subsecao'
		self.url_inserir_subsecao = estoque_url_base + acao_inserir
		self.nome = 'uma subsecao qualquer'
		self.descricao = 'uma descricao qualquer'
		self.situacao = 'INATIVO'

	def exclui_subsecao_de_teste(self):
		self.db_test(self.db_test.subsecao.nome == self.nome.upper()).delete()
		self.db_test.commit()

	def insere_secao_de_teste(self):
		temp_id = self.db_test.secao.insert(nome="secao teste".upper(),situacao='ATIVO')
		self.db_test.commit()
		return temp_id	

	def exclui_secao_de_teste(self, _id):
		self.db_test(self.db_test.secao.id == _id).delete()
		self.db_test.commit()	

	def test_inserir_campos_obrigatorios_vazios(self):
		self.driver.get(self.url_inserir_subsecao)
		self.submit_form()
		time.sleep(0.5)

		mensagem_de_erro = 'enter a value'
		mensagem_de_erro_2 = 'value not in database'

		assert (self.driver.find_element_by_id('nome__error').text == mensagem_de_erro
			and self.driver.find_element_by_id('secao_id__error').text == mensagem_de_erro_2) == True

	def test_inserir_campos_obrigatorios_preenchidos(self):
		temp_id = self.insere_secao_de_teste()

		time.sleep(0.1)

		temp_secao = self.db_test(self.db_test.secao.id == temp_id).select()

		self.driver.get(self.url_inserir_subsecao)
		self.driver.find_element_by_id('subsecao_nome').send_keys(self.nome)
		self.driver.find_element_by_id('subsecao_situacao').send_keys(self.situacao)
		self.driver.find_element_by_id('subsecao_secao_id').send_keys(temp_secao[0].nome)

		self.submit_form()

		time.sleep(0.5)

		rows = self.db_test(self.db_test.subsecao.nome == self.nome.upper()).select()
		assert (len(rows) > 0) == True

		self.exclui_secao_de_teste(temp_id)


	def test_inserir_subsecao_com_nome_repetido(self):
		temp_id = self.insere_secao_de_teste()
		self.db_test.subsecao.insert(nome=self.nome.upper(),situacao=self.situacao,
			secao_id=temp_id)
		self.db_test.commit()
		time.sleep(0.1)

		temp_secao = self.db_test(self.db_test.secao.id == temp_id).select()

		self.driver.get(self.url_inserir_subsecao)
		self.driver.find_element_by_id('subsecao_nome').send_keys(self.nome)
		self.driver.find_element_by_id('subsecao_situacao').send_keys(self.situacao)
		self.driver.find_element_by_id('subsecao_secao_id').send_keys(temp_secao[0].nome)

		self.submit_form()

		time.sleep(0.5)

		mensagem_de_erro = 'value already in database or empty'

		assert self.driver.find_element_by_id('nome__error').text == mensagem_de_erro

		self.exclui_secao_de_teste(temp_id)
		self.exclui_subsecao_de_teste()


	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroSubsecao('test_inserir_campos_obrigatorios_vazios'))
		suite.addTest(TestCadastroSubsecao('test_inserir_campos_obrigatorios_preenchidos'))
		suite.addTest(TestCadastroSubsecao('test_inserir_subsecao_com_nome_repetido'))
		return suite	
