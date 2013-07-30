
import unittest
import sys
import os
from os import path

sys.path.append('../../../') # we need this to use web2py's modules

from gluon.sql import DAL, Field
from gluon.validators import *

class Estoquista(object):
	"""docstring for Estoquista"""
	def __init__(self):
		
		db_username_postgres = 'postgres'
		db_password_postgres = '1234'
		db_postgres_url = 'postgres://' + db_username_postgres + ':' + db_password_postgres + '@localhost/dev'

		path_to_database = path.join(path.curdir, "../databases")
		self.db_copy = DAL(db_postgres_url, folder=path_to_database)
		self.db_copy.import_table_definitions(path_to_database)
		
	def criar_registro_de_entrada_no_estoque(self, item_da_nota_fiscal):		
		self.db_copy.registro_estoque.insert(produto_id=item_da_nota_fiscal.produto_id,
												descricao_produto=item_da_nota_fiscal.descricao,
												quantidade_entrada=item_da_nota_fiscal.total, 
												quantidade_saida=0)	
		self.db_copy.commit()
	def atualizar_registro_de_entrada_no_estoque(self, item_estoque, item_da_nota_fiscal):		
		quantidade_entrada_atualizada = item_estoque[0].quantidade_entrada + item_da_nota_fiscal.total
		saldo_atualizado = quantidade_entrada_atualizada - item_estoque[0].quantidade_saida
		self.db_copy(self.db_copy.registro_estoque.produto_id 
						== item_da_nota_fiscal.produto_id).update(quantidade_entrada=quantidade_entrada_atualizada,
																	saldo=saldo_atualizado)
		self.db_copy.commit()

	def atualizar_estoque_para_entradas(self,lista_itens_nota_fiscal):
		for item_da_nota_fiscal in lista_itens_nota_fiscal:
			item_estoque = self.db_copy(self.db_copy.registro_estoque.produto_id 
				== item_da_nota_fiscal.produto_id).select()
			if len(item_estoque) > 0:
				self.atualizar_registro_de_entrada_no_estoque(item_estoque,item_da_nota_fiscal)
			else:
				self.criar_registro_de_entrada_no_estoque(item_da_nota_fiscal)	

			