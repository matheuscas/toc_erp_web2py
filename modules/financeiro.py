import sys
import os
import datetime
from os import path

sys.path.append('../../../') # we need this to use web2py's modules

from gluon.sql import DAL, Field
from gluon.validators import *

class GerenteFinanceiro(object):
	"""docstring for GerenteFinanceiro"""
	def __init__(self):
		db_username_postgres = 'postgres'
		db_password_postgres = '1234'
		db_postgres_url = 'postgres://' + db_username_postgres + ':' + db_password_postgres + '@localhost/dev'

		path_to_database = path.join(path.curdir, "../databases")
		self.db_copy = DAL(db_postgres_url, folder=path_to_database)
		self.db_copy.import_table_definitions(path_to_database)

	def gerar_automaticamente_conta_pagar_fornecedor(self, nota_fiscal_compra):

		condicao_pagamento = self.db_copy(self.db_copy.condicao_pagamento.id == 
										nota_fiscal_compra.condicao_pagamento_id).select()

		quantidade_parcelas = condicao_pagamento[0].numero_parcelas

		numero_titulo = str(nota_fiscal_compra.fornecedor_id) + nota_fiscal_compra.numero
		numero_documento = '1'
		categoria = 'FORNECEDOR'
		historico = ' TITULO A PAGAR REF. AO DOCUMENTO ' + numero_documento + ' DA NF DE COMPRAS ' \
						+ nota_fiscal_compra.numero;
		data_emissao = nota_fiscal_compra.data_emissao
		data_vencimento_delta = datetime.timedelta(days=30)
		data_criacao = datetime.date.today()
		valor_nominal = nota_fiscal_compra.total
		status = 'ABERTO'

		valor_parcela = valor_nominal / quantidade_parcelas
		diff = valor_nominal - (valor_parcela * quantidade_parcelas)						

		for p in range(1, quantidade_parcelas + 1):

			if p == quantidade_parcelas:
				valor_parcela + diff

			self.db_copy.conta_pagar.insert(numero_titulo=numero_titulo, parcela=p, 
											numero_documento=numero_documento, 
											numero_nota_fiscal=nota_fiscal_compra.numero,
											fornecedor_id=nota_fiscal_compra.fornecedor_id,categoria=categoria,
											historico=historico, data_emissao=data_emissao,
											data_vencimento=(data_emissao + (data_vencimento_delta * p)),
											data_criacao=data_criacao, valor_nominal=valor_nominal,
											status=status, valor_parcela=valor_parcela)
		self.db_copy.commit()	
		

	def gerar_credito_debito_de_conta_a_pagar(self, conta_pagar_id):
		conta_pagar = self.db_copy.conta_pagar[conta_pagar_id]
		self.db_copy.lancamento_contabil.insert(valor=conta_pagar.valor_parcela,conta_credito='COMPRAS',
												conta_debito='CAIXA', transacao=conta_pagar.numero_titulo,
												data_lancamento=conta_pagar.data_vencimento)
		self.db_copy.commit()											