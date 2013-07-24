db.define_table('registro_estoque',
	Field('produto_id','reference produto'),
	Field('descricao_produto'),
	Field('quantidade_entrada','double'),
	Field('quantidade_saida','double'),
	Field('saldo','double'),
	format='%(produto_id)s %(descricao_produto)s %(saldo)s')