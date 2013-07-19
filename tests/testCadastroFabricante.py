import unittest
import time
from testSetup import TestSetup

class TestCadastroFabricante(TestSetup):
	"""docstring for TestCadastroFornecedor"""
	def setUp(self):
		super(TestCadastroFabricante, self).setUp()
		compras_url_base = 'http://localhost:8000/toc_erp_web2py/estoque/'
		controller_inserir_fabricante = 'inserir_fabricante'
		self.url_inserir_fabricante = compras_url_base + controller_inserir_fabricante 
		self.nome = 'um fabricante qualquer'
		self.cpf_cnpj = '02441251554'
		#self.situacao = 'ATIVO'
		self.limpa_dados_tabela('fabricante')

	def insere_endereco_de_teste(self):
		endereco_id = self.db_test.endereco.insert(rua='e',cidade='fsa',bairro='mda',estado='ba')
		self.db_test.commit()
		return endereco_id

	def exclui_endereco_de_teste(self, endereco_id):
		self.db_test(self.db_test.endereco.id == endereco_id).delete()
		self.db_test.commit()

	def insere_fabricante_de_teste(self):
		self.db_test.fabricante.insert(nome=self.nome,cpf_cnpj=self.cpf_cnpj)
		self.db_test.commit()

	def exclui_fabricante_de_teste(self):
		self.db_test(self.db_test.fabricante.cpf_cnpj == self.cpf_cnpj).delete()
		self.db_test.commit()		

	def preenche_campos_obrigatorios_e_submit(self):
		
		self.driver.find_element_by_id('fabricante_nome').send_keys(self.nome)
		self.driver.find_element_by_id('fabricante_cpf_cnpj').send_keys(self.cpf_cnpj)
		self.submit_form()		

	def test_inserir_campos_obrigatorios_vazios(self):	
		self.driver.get(self.url_inserir_fabricante)
		self.submit_form()
		time.sleep(0.5)
		mensagem_de_erro = 'enter a value'

		assert (self.driver.find_element_by_id('nome__error').text == mensagem_de_erro and
			self.driver.find_element_by_id('cpf_cnpj__error').text == mensagem_de_erro) == True

	def test_inserir_campos_obrigatorios_preenchidos(self):
		self.driver.get(self.url_inserir_fabricante)
		endereco_id = self.insere_endereco_de_teste()
		self.preenche_campos_obrigatorios_e_submit()
		time.sleep(0.5)
		assert (len(self.db_test(self.db_test.fabricante.cpf_cnpj == self.cpf_cnpj).select()) > 0) == True
		self.exclui_fabricante_de_teste()
		self.exclui_endereco_de_teste(endereco_id)

	def test_inserir_fabricante_com_cpf_cnpj_repetido(self):
		self.insere_fabricante_de_teste()
		self.driver.get(self.url_inserir_fabricante)
		self.preenche_campos_obrigatorios_e_submit()
		time.sleep(0.5)
		mensagem_de_erro = 'value already in database or empty'

		assert self.driver.find_element_by_id('cpf_cnpj__error').text == mensagem_de_erro

		self.exclui_fabricante_de_teste()			

	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroFabricante('test_inserir_campos_obrigatorios_vazios'))
		suite.addTest(TestCadastroFabricante('test_inserir_campos_obrigatorios_preenchidos'))
		suite.addTest(TestCadastroFabricante('test_inserir_fabricante_com_cpf_cnpj_repetido'))
		return suite	
