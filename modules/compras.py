
class ItemNotaFiscalCompra(object):
	"""docstring for ItemNotaFiscalCompra"""
	def __init__(self, produto_id=None,	descricao=None,	
				preco_unitario=None, quantidade=None,
				unidade_compra=None, quantidade_embalagem=None,
				aliquota_icms=None,total=None):
		self.produto_id = produto_id
		self.descricao = descricao
		self.preco_unitario = preco_unitario
		self.quantidade = quantidade
		self.unidade_compra = unidade_compra
		self.quantidade_embalagem = quantidade_embalagem
		self.aliquota_icms = aliquota_icms
		self.total = total

class NotaFiscalCompra(object):
	"""docstring for NotaFiscalCompra"""
	def __init__(self, numero=None,data_emissao=None,
					data_chegada=None, natureza_operacao=None,
					fornecedor_id=None, base_calculo_icms=None,
					valor_icms=None, valor_ipi=None,
					frete=None, outras=None, desconto = None,
					condicao_pagamento_id=None, total=None):
		self.numero=numero
		self.data_emissao = data_emissao
		self.data_chegada = data_chegada
		self.natureza_operacao = natureza_operacao
		self.fornecedor_id = fornecedor_id
		self.base_calculo_icms = base_calculo_icms
		self.valor_icms = valor_icms
		self.valor_ipi = valor_ipi
		self.frete = frete
		self.outras = outras
		self.desconto = desconto
		self.condicao_pagamento_id = condicao_pagamento_id
		self.total = total
		
						
		
		
		