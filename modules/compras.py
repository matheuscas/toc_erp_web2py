
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
		
		
		