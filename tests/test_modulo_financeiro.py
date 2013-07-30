import unittest
import datetime
import time
from test_module_setup import TestModuleSetup
from applications.toc_erp_web2py.modules.financeiro import GerenteFinanceiro
from applications.toc_erp_web2py.modules.compras import NotaFiscalCompra

class TestGerenteFinanceiro(TestModuleSetup):
	"""docstring for TestGerenteFinanceiro"""
	def setUp(self):
		super(TestGerenteFinanceiro, self).setUp()
		self.limpa_dados_tabela('conta_pagar')
		self.limpa_dados_tabela('nota_fiscal_compra')
		self.limpa_dados_tabela('fornecedor')
		self.limpa_dados_tabela('condicao_pagamento')
		self.limpa_dados_tabela('contato')
		self.limpa_dados_tabela('endereco')

	def test_gerar_automaticamente_conta_pagar_fornecedor(self):

		numero_parcelas = 3
		numero_nf = '1000'
		data_emissao = datetime.date.today()
		data_chegada = data_emissao		
		data_vencimento = data_emissao + datetime.timedelta(days=30)
		cfop = 'ENTRADA'
		total = 100.0

		contato_id = self.db_test.contato.insert(nome_contato='BASTARDO')
		self.db_test.commit()

		endereco_id = self.db_test.endereco.insert(rua='E',bairro='bairro',cidade='fsa',estado='ba')
		self.db_test.commit()

		fornecedor_id = self.db_test.fornecedor.insert(nome='NOME',cpf_cnpj='cpf_cnpj',
														endereco=endereco_id,contato_id=contato_id)
		self.db_test.commit()

		condicao_pagamento_id = self.db_test.condicao_pagamento.insert(descricao='desc',
																		data_vencimento=data_vencimento,
																		numero_parcelas=numero_parcelas,
																		situacao='ATIVO')
		self.db_test.commit()
		nota_fiscal_compra = NotaFiscalCompra(numero=numero_nf,data_emissao=data_emissao,
												data_chegada=data_chegada, natureza_operacao=cfop,
												fornecedor_id=fornecedor_id,
												condicao_pagamento_id=condicao_pagamento_id,
												total=total)

		gerente_fin = GerenteFinanceiro()
		gerente_fin.gerar_automaticamente_conta_pagar_fornecedor(nota_fiscal_compra)

		numero_titulos = str(fornecedor_id) + numero_nf
		rows = self.db_test(self.db_test.conta_pagar.numero_titulo == numero_titulos).select()

		assert len(rows) == numero_parcelas

	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestGerenteFinanceiro('test_gerar_automaticamente_conta_pagar_fornecedor'))
		return suite	
