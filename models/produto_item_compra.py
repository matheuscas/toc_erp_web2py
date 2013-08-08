db.define_table('item_compra',
	Field('produto_id','integer','reference produto',required=True, notnull=True),
	Field('nota_fiscal_id','integer','reference nota_fiscal_compra',required=True, notnull=True),
	Field('descricao'),
	Field('preco_unitario','double'),
	Field('quantidade','double'),
	Field('unidade_compra'),
	Field('quantidade_embalagem','double'),
	Field('aliquota_icms','decimal(4,2)'),
	Field('total_item','double'),
	format='%(produto_id)s %(descricao)s')

#db.item_compra.produto_id.widget = SQLFORM.widgets.autocomplete(request,
	#db.produto.nome, id_field=db.produto.id)
db.item_compra.produto_id.requires = [IS_NOT_EMPTY()]
