import unittest
import time
from testSetup import TestSetup

class TestCadastroMarca(TestSetup):
	"""docstring for TestCadastroMarca"""
	def setUp(self):
		super(TestCadastroMarca,self).setUp()
		compras_url_base = 'http://localhost:8000/toc_erp_web2py/estoque/'
		controller_inserir = 'inserir_marca'
		self.url_inserir_marca = compras_url_base + controller_inserir
		self.nome = 'mais uma marca fajuta'
		self.limpa_dados_tabela('marca')
		self.limpa_dados_tabela('fabricante')

	def test_inserir_campos_obrigatorios_vazios(self):
		self.driver.get(self.url_inserir_marca)
		self.submit_form()
		time.sleep(0.5)

		mensagem_de_erro = 'enter a value'
		#so estou testanto o nome , pois a imagem eh opcional
		#e a situacao sempre vem um valor padrao e a lista de fabricantes
		#fica inativa quando n tem nenhum.  
		assert (self.driver.find_element_by_id('nome__error').text == mensagem_de_erro) == True

	def test_inserir_campos_obrigatorios_preenchidos(self):
		self.driver.get(self.url_inserir_marca)
		self.driver.find_element_by_id('marca_nome').send_keys(self.nome)
		self.submit_form()
		time.sleep(0.5)

		rows = self.db_test(self.db_test.marca.nome == self.nome.upper()).select()
		assert (len(rows) > 0) == True

	def test_validar_nome_marca_repetido(self):
		fabricante_id = self.db_test.fabricante.insert(nome='fabricante para ' + self.nome,cpf_cnpj='02441251554')
		self.db_test.commit() 
		self.db_test.marca.insert(nome=self.nome.upper(),fabricante_id=[fabricante_id],situacao='INATIVO')
		self.db_test.commit()
		time.sleep(0.5)
		self.driver.get(self.url_inserir_marca)
		self.driver.find_element_by_id('marca_nome').send_keys(self.nome)
		mensagem_de_erro = 'value already in database or empty'
		self.submit_form()
		time.sleep(0.5)
		assert (self.driver.find_element_by_id('nome__error').text == mensagem_de_erro)

	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroMarca('test_inserir_campos_obrigatorios_vazios'))
		suite.addTest(TestCadastroMarca('test_inserir_campos_obrigatorios_preenchidos'))
		suite.addTest(TestCadastroMarca('test_validar_nome_marca_repetido'))
		return suite	
		