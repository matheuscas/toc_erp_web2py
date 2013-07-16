import unittest
import time
from testSetup import TestSetup

class TestCadastroEmbalagem(TestSetup):
	"""docstring for TestCadastroEmbalagem"""
	def setUp(self):
		super(TestCadastroEmbalagem, self).setUp()
		estoque_url_base = 'http://127.0.0.1:8000/toc_erp_web2py/estoque'
		acao_inserir = '/inserir_embalagem'
		self.url_inserir_imposto = estoque_url_base + acao_inserir
		self.nome = 'Mais uma embalagem qualquer'
		self.unidade_medida = 'CX'
		self.quantidade_casas_decimais = 1
		self.tabela = 'embalagem_'

	def preenche_campos_obrigatorios_e_submit(self):
		self.driver.get(self.url_inserir_imposto)

		self.driver.find_element_by_id(self.tabela + 'nome').send_keys(self.nome)
		self.driver.find_element_by_id(self.tabela + 'unidade_medida').send_keys(self.unidade_medida)
		self.driver.find_element_by_id(self.tabela + 'quantidade_casas_decimais').send_keys(self.quantidade_casas_decimais)

		self.submit_form()

	def exclui_embalagem_de_teste(self):
		self.db_test(self.db_test.embalagem.unidade_medida == self.unidade_medida and
			self.db_test.embalagem.quantidade_casas_decimais == self.quantidade_casas_decimais).delete()

		self.db_test.commit()		

	def insere_embalagem_de_teste(self,nome='Mais uma embalagem qualquer',
		unidade_medida='CX',quantidade_casas_decimais=1,situacao='ATIVA'):
		
		self.db_test.embalagem.insert(nome=nome.upper(),unidade_medida=unidade_medida,
			quantidade_casas_decimais=quantidade_casas_decimais,situacao=situacao)

		self.db_test.commit()		

	def test_inserir_campos_obrigatorios_vazios(self):
		self.driver.get(self.url_inserir_imposto)
		self.submit_form()
		time.sleep(0.5)

		nome_error = self.driver.find_element_by_id('nome__error')
		unidade_medida_error = self.driver.find_element_by_id('unidade_medida__error')

		mensagem_error = 'enter a value'

		assert (nome_error.text == mensagem_error and unidade_medida_error.text == mensagem_error) == True

	def test_inserir_campos_obrigatorios_preenchidos(self):
		self.driver.get(self.url_inserir_imposto)
		self.preenche_campos_obrigatorios_e_submit()
		time.sleep(0.5)
		rows = self.db_test(self.db_test.embalagem.unidade_medida == self.unidade_medida and
			self.db_test.embalagem.quantidade_casas_decimais == self.quantidade_casas_decimais).select()

		assert (len(rows) > 0) == True

		self.exclui_embalagem_de_teste()

	def test_inserir_nome_da_embalagem_repetido(self):
		self.insere_embalagem_de_teste()
		self.driver.get(self.url_inserir_imposto)
		self.preenche_campos_obrigatorios_e_submit()
		time.sleep(0.5)

		mensagem_erro_padrao = 'value already in database or empty'
		nome_error = self.driver.find_element_by_id('nome__error')
		assert nome_error.text == mensagem_erro_padrao

		self.exclui_embalagem_de_teste()

	def test_inserir_unidade_medida_e_quantidade_casas_decimais_repetidos(self):
		self.insere_embalagem_de_teste(nome="Uma outra embalagem")
		self.driver.get(self.url_inserir_imposto)
		self.preenche_campos_obrigatorios_e_submit()

		time.sleep(0.5)

		unidade_medida_error = self.driver.find_element_by_id('unidade_medida__error')
		quantidade_casas_decimais_error = self.driver.find_element_by_id('quantidade_casas_decimais__error')

		mensagem_erro_padrao = 'value already in database'

		assert (unidade_medida_error.text == mensagem_erro_padrao 
			and quantidade_casas_decimais_error.text == mensagem_erro_padrao) == True

		self.exclui_embalagem_de_teste()


	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroEmbalagem('test_inserir_campos_obrigatorios_vazios'))
		suite.addTest(TestCadastroEmbalagem('test_inserir_campos_obrigatorios_preenchidos'))
		suite.addTest(TestCadastroEmbalagem('test_inserir_nome_da_embalagem_repetido'))
		suite.addTest(TestCadastroEmbalagem('test_inserir_unidade_medida_e_quantidade_casas_decimais_repetidos'))
		return suite	

						
			
