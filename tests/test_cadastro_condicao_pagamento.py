import unittest
import time
import datetime
from testSetup import TestSetup

class TestCadastroCondicaoPagamento(TestSetup):
	"""docstring for TestCadastroCondicaoPagamento"""
	def setUp(self):
		super(TestCadastroCondicaoPagamento,self).setUp()
		financeiro_url_base = 'http://localhost:8000/toc_erp_web2py/financeiro/'
		controller_inserir = 'inserir_condicao_pagamento'
		self.url_inserir_condicao_pagamento = financeiro_url_base + controller_inserir
		self.descricao = 'uma condicao de pagamento qualquer'.upper()
		self.data_vencimento = str(datetime.datetime.now().year) + '-' + \
								str(datetime.datetime.now().month) + '-' + \
								str(datetime.datetime.now().day)
		self.desconto = 10
		self.acrescimo = 15
		self.numero_parcela = 3
		self.limpa_dados_tabela('condicao_pagamento')

	def test_nao_preenche_campos_obrigatorios(self):
		self.driver.get(self.url_inserir_condicao_pagamento)
		self.submit_form()
		time.sleep(0.5)
		
		mensagem_de_erro = 'enter a value'
		mensagem_de_erro_2 = 'invalid format(YYYY-MM-DD) or value'
		mensagem_de_erro_3 = 'the value is too small or too large'

		assert (self.driver.find_element_by_id('descricao__error').text == mensagem_de_erro and 
		self.driver.find_element_by_id('data_vencimento__error').text == mensagem_de_erro_2 and
		self.driver.find_element_by_id('numero_parcelas__error').text == mensagem_de_erro_3) == True

	def test_preenche_campos_obrigatorios(self):
		self.driver.get(self.url_inserir_condicao_pagamento)
		self.driver.find_element_by_id('condicao_pagamento_descricao').send_keys(self.descricao)
		self.driver.find_element_by_id('condicao_pagamento_data_vencimento').send_keys(self.data_vencimento)
		self.driver.find_element_by_id('condicao_pagamento_numero_parcelas').send_keys(self.numero_parcela)
		self.submit_form()
		time.sleep(0.5)
		rows = self.db_test(self.db_test.condicao_pagamento.descricao == self.descricao).select()
		assert (len(rows) > 0) == True

	def test_valor_desconto_negativo(self):
		self.driver.get(self.url_inserir_condicao_pagamento)
		self.desconto = -10
		self.driver.find_element_by_id('condicao_pagamento_desconto').send_keys(self.desconto)
		self.submit_form()
		time.sleep(0.5)
		mensagem_de_erro = 'enter a number between 0 and 100'

		assert mensagem_de_erro == self.driver.find_element_by_id('desconto__error').text

	def test_valor_desconto_acima_de_100(self):
		self.driver.get(self.url_inserir_condicao_pagamento)
		self.desconto = 101
		self.driver.find_element_by_id('condicao_pagamento_desconto').send_keys(self.desconto)
		self.submit_form()
		time.sleep(0.5)
		mensagem_de_erro = 'enter a number between 0 and 100'

		assert mensagem_de_erro == self.driver.find_element_by_id('desconto__error').text

	def test_valor_acrescimo_negativo(self):
		self.driver.get(self.url_inserir_condicao_pagamento)
		self.acrescimo = '-23.4'
		self.driver.find_element_by_id('condicao_pagamento_acrescimo').send_keys(self.acrescimo)
		self.submit_form()
		time.sleep(0.5)
		mensagem_de_erro = 'enter a number between 0 and 100'

		assert mensagem_de_erro == self.driver.find_element_by_id('acrescimo__error').text

	def test_valor_acrescimo_acima_de_100(self):
		self.driver.get(self.url_inserir_condicao_pagamento)
		self.acrescimo = '100.1'
		self.driver.find_element_by_id('condicao_pagamento_acrescimo').send_keys(self.acrescimo)
		self.submit_form()
		time.sleep(0.5)
		mensagem_de_erro = 'enter a number between 0 and 100'

		assert mensagem_de_erro == self.driver.find_element_by_id('acrescimo__error').text

	def test_data_vencimento_menor_que_data_atual(self):
		self.driver.get(self.url_inserir_condicao_pagamento)

		mensagem_de_erro = 'invalid format(YYYY-MM-DD) or value'
		tres_dias_atras = str(datetime.date.today() - datetime.timedelta(days=3))
		self.driver.find_element_by_id('condicao_pagamento_data_vencimento').send_keys(tres_dias_atras)
		self.submit_form()
		time.sleep(0.5)

		assert self.driver.find_element_by_id('data_vencimento__error').text == mensagem_de_erro

	def test_numero_parcelas_negativo(self):
		self.numero_parcela = -10
		mensagem_de_erro = 'the value is too small or too large'

		self.driver.get(self.url_inserir_condicao_pagamento)
		self.driver.find_element_by_id('condicao_pagamento_numero_parcelas').send_keys(self.numero_parcela)
		self.submit_form()
		time.sleep(0.5)

		assert self.driver.find_element_by_id('numero_parcelas__error').text == mensagem_de_erro		

	def test_numero_parcelas_maior_que_100(self):
		self.numero_parcela = 112
		mensagem_de_erro = 'the value is too small or too large'

		self.driver.get(self.url_inserir_condicao_pagamento)
		self.driver.find_element_by_id('condicao_pagamento_numero_parcelas').send_keys(self.numero_parcela)
		self.submit_form()
		time.sleep(0.5)

		assert self.driver.find_element_by_id('numero_parcelas__error').text == mensagem_de_erro		

	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestCadastroCondicaoPagamento('test_nao_preenche_campos_obrigatorios'))
		suite.addTest(TestCadastroCondicaoPagamento('test_preenche_campos_obrigatorios'))
		suite.addTest(TestCadastroCondicaoPagamento('test_valor_desconto_negativo'))
		suite.addTest(TestCadastroCondicaoPagamento('test_valor_desconto_acima_de_100'))
		suite.addTest(TestCadastroCondicaoPagamento('test_valor_acrescimo_negativo'))
		suite.addTest(TestCadastroCondicaoPagamento('test_valor_acrescimo_acima_de_100'))
		suite.addTest(TestCadastroCondicaoPagamento('test_data_vencimento_menor_que_data_atual'))
		suite.addTest(TestCadastroCondicaoPagamento('test_numero_parcelas_negativo'))
		suite.addTest(TestCadastroCondicaoPagamento('test_numero_parcelas_maior_que_100'))
		return suite	
