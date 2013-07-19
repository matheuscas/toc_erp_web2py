import unittest
import time
from testSetup import TestSetup
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0

class TestCadastroFornecedor(TestSetup):
	"""docstring for TestCadastroFornecedor"""
	
	def setUp(self):
		super(TestCadastroFornecedor, self).setUp()	

		self.compras_url_base = 'http://127.0.0.1:8000/toc_erp_web2py/compras'	
		self.inserir_fornecedor = '/inserir_fornecedor'
		self.atualizar_fornecedor = '/atualizar_fornecedor'
		self.url_inserir_fornecedor = self.compras_url_base + self.inserir_fornecedor
		self.url_atualizar_fornecedor = self.compras_url_base + self.atualizar_fornecedor
		self.cpf_cnpj_num = "02441251591"
		self.limpa_dados_tabela('fornecedor')

	def busca_e_preenche_campos_obrigatorios_e_submit(self):

		nome = self.driver.find_element_by_id("no_table_nome")
		cpf_cnpj = self.driver.find_element_by_id("no_table_cpf_cnpj")
		rua = self.driver.find_element_by_id("no_table_rua")
		bairro = self.driver.find_element_by_id("no_table_bairro")
		cidade = self.driver.find_element_by_id("no_table_cidade")
		estado = self.driver.find_element_by_id("no_table_estado")
		
		nome.send_keys("fornecedor qualquer")
		cpf_cnpj.send_keys(self.cpf_cnpj_num)
		rua.send_keys("E")
		bairro.send_keys("MDA")
		cidade.send_keys("FSA")
		estado.send_keys("Bahia")

		self.driver.find_element_by_xpath(self.submit_button).click()			

	def exclui_fornecedor_de_teste(self):
		rows = self.db_test(self.db_test.fornecedor.cpf_cnpj == self.cpf_cnpj_num).select()

		if len(rows) > 0:
			endereco_id_to_del = rows[0].endereco
			contato_id_to_del = rows[0].contato_id

			#db_test(db_test.fornecedor.id == fornecedor_id).delete()
			self.db_test(self.db_test.fornecedor.cpf_cnpj == self.cpf_cnpj_num).delete()
			self.db_test(self.db_test.endereco.id == endereco_id_to_del).delete()
			self.db_test(self.db_test.contato.id == contato_id_to_del).delete()

			self.db_test.commit()		

	def test_inserir_fornecedor_com_campos_obrigatorios_vazios(self):
	
		self.driver.get(self.url_inserir_fornecedor)		

		mensagem_erro_padrao = 'enter a value'

		self.driver.find_element_by_xpath(self.submit_button).click()

		time.sleep(0.5)

		nome_error = self.driver.find_element_by_id("nome__error")
		cpf_cnpj_error = self.driver.find_element_by_id("cpf_cnpj__error")
		rua_error = self.driver.find_element_by_id("rua__error")
		bairro_error = self.driver.find_element_by_id("bairro__error")
		cidade_error = self.driver.find_element_by_id("cidade__error")
		estado_error = self.driver.find_element_by_id("estado__error")

		nome_error_assert = (nome_error.text == mensagem_erro_padrao)
		cpf_cnpj_error_assert = (cpf_cnpj_error.text == mensagem_erro_padrao)
		rua_error_assert = (rua_error.text == mensagem_erro_padrao)
		bairro_error_assert = (bairro_error.text == mensagem_erro_padrao)
		cidade_error_assert = (cidade_error.text == mensagem_erro_padrao)
		estado_error_assert = (estado_error.text == mensagem_erro_padrao)

		assert (nome_error_assert and cpf_cnpj_error_assert and rua_error_assert and 
			bairro_error_assert and cidade_error_assert and estado_error_assert) == True

	def test_inserir_fornecedor_com_campos_obrigatorios_preenchidos(self):
		
		self.driver.get(self.url_inserir_fornecedor)
		self.busca_e_preenche_campos_obrigatorios_e_submit()
		time.sleep(0.5) #para dar tempo ao commit do banco

		rows = self.db_test(self.db_test.fornecedor.cpf_cnpj == self.cpf_cnpj_num).select()

		assert (len(rows) > 0) == True

		self.exclui_fornecedor_de_teste()

	def test_inserir_cpf_cnpj_repetido(self):
		
		#insere a primeira vez
		self.driver.get(self.url_inserir_fornecedor)
		self.busca_e_preenche_campos_obrigatorios_e_submit()

		time.sleep(0.5)

		#tenta inserir a segunda vez para dar o erro do cpf/cnpj repetido
		self.driver.get(self.url_inserir_fornecedor)

		time.sleep(0.5)

		self.busca_e_preenche_campos_obrigatorios_e_submit()

		time.sleep(0.5)

		cpf_cnpj_error = self.driver.find_element_by_id("cpf_cnpj__error")
		mensagem_erro_padrao = 'value already in database or empty'

		assert cpf_cnpj_error.text == mensagem_erro_padrao

		time.sleep(0.1)

		self.exclui_fornecedor_de_teste()

	def test_mostrar_fornecedor_com_id_existente(self):
		
		self.driver.get(self.url_inserir_fornecedor)
		self.busca_e_preenche_campos_obrigatorios_e_submit()
		time.sleep(0.5)
		rows = self.db_test(self.db_test.fornecedor.cpf_cnpj == self.cpf_cnpj_num).select()
		self.driver.get(self.url_atualizar_fornecedor + '/' + str(rows[0].id))
		cpf_cnpj = self.driver.find_element_by_id("fornecedor_cpf_cnpj")
		assert cpf_cnpj.get_attribute("value")  == self.cpf_cnpj_num
		self.exclui_fornecedor_de_teste()

	def test_excluir_fornecedor_com_movimentacoes(self):
		print "Teste vazio"

	def test_excluir_fornecedor_sem_movimentacoes(self):
		print "Teste vazio"


	@classmethod	
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroFornecedor('test_inserir_fornecedor_com_campos_obrigatorios_vazios'))
		suite.addTest(TestCadastroFornecedor('test_inserir_fornecedor_com_campos_obrigatorios_preenchidos'))
		suite.addTest(TestCadastroFornecedor('test_inserir_cpf_cnpj_repetido'))
		suite.addTest(TestCadastroFornecedor('test_mostrar_fornecedor_com_id_existente'))
		return suite			
		
if __name__ == '__main__':
    unittest.main()	