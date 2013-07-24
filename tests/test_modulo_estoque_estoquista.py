import unittest
import datetime
import time
from applications.toc_erp_web2py.modules.estoque import Estoquista
from applications.toc_erp_web2py.modules.compras import ItemNotaFiscalCompra
from test_module_setup import TestModuleSetup

class TestEstoquista(TestModuleSetup):
 	"""docstring for TestEstoque"""
 	def setUp(self):
 		super(TestEstoquista,self).setUp()
 		self.limpa_dados_tabela('registro_estoque')
 		self.limpa_dados_tabela('produto')
 		self.limpa_dados_tabela('secao')

 	def inserir_secao_e_produto_de_teste(self):
 		secao_id = self.db_test.secao.insert(nome='secao de teste',situacao='ATIVO')
 		self.db_test.commit()
 		produto_id = self.db_test.produto.insert(nome='produto de teste',secao_id=secao_id,unidade_medida='UN')
 		self.db_test.commit()

 		return produto_id

 	def cria_item_nota_fiscal_compra_teste(self, produto_id):
 		item_compra = ItemNotaFiscalCompra()
 		item_compra.produto_id = produto_id
 		item_compra.descricao = 'essa descricao tem de ser a do produto'
 		item_compra.total = 34

 		return item_compra		

 	def test_criar_registro_de_entrada_no_estoque(self):
 		
 		produto_id  = self.inserir_secao_e_produto_de_teste()
 		item_compra = self.cria_item_nota_fiscal_compra_teste(produto_id)

 		estoquista = Estoquista()
 		estoquista.criar_registro_de_entrada_no_estoque(item_compra)

 		row = self.db_test(self.db_test.registro_estoque.produto_id == item_compra.produto_id).select()
 		assert (len(row) > 0) == True

	def test_atualizar_registro_de_entrada_no_estoque(self):
		produto_id  = self.inserir_secao_e_produto_de_teste()
 		item_compra = self.cria_item_nota_fiscal_compra_teste(produto_id)

 		estoquista = Estoquista()
 		estoquista.criar_registro_de_entrada_no_estoque(item_compra)

 		item_estoque = self.db_test(self.db_test.registro_estoque.produto_id == produto_id).select()

 		item_compra.total = 66

 		estoquista.atualizar_registro_de_entrada_no_estoque(item_estoque, item_compra)

 		item_estoque = self.db_test(self.db_test.registro_estoque.produto_id == produto_id).select()

 		assert (item_estoque[0].quantidade_entrada == 100) == True

	@classmethod
	def suite(cls):
		suite = unittest.TestSuite()
		suite.addTest(TestEstoquista('test_criar_registro_de_entrada_no_estoque'))
		suite.addTest(TestEstoquista('test_atualizar_registro_de_entrada_no_estoque'))		
		return suite				
