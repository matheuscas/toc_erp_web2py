db.define_table('produto',
	Field('nome','string',required=True, notnull=True),
	Field('descricao','text'),
	Field('secao_id','reference secao',required=True, notnull=True),
	Field('subsecao_id','reference subsecao'),
	Field('marca_id','reference marca'),
	Field('fabricante_id','reference fabricante'),
	Field('fornecedor_id','reference fornecedor'),
	Field('codigo_barras','string'),
	Field('codigo_ncm','string'),
	Field('unidade_medida','string', required=True, notnull=True),
	Field('estoque_padrao_compra','float'),
	Field('tipo_item','string'),
	Field('cst_compra_pis','string'),
	Field('cst_compra_cofins','string'),
	Field('cst_compra_ipi'),
	format='%(nome)s')

db.produto.nome.requires = [IS_NOT_EMPTY(), IS_UPPER(), CLEANUP()]
db.produto.secao_id.requires = IS_IN_DB(db, 'secao.id',zero=None)
db.produto.subsecao_id.requires = IS_EMPTY_OR(IS_IN_DB(db, 'subsecao.id'))
db.produto.marca_id.requires = IS_EMPTY_OR(IS_IN_DB(db,'marca.id'))
db.produto.fabricante_id.requires = IS_EMPTY_OR(IS_IN_DB(db,'fabricante.id'))
db.produto.fornecedor_id.requires = IS_EMPTY_OR(IS_IN_DB(db,'fornecedor.id'))
db.produto.estoque_padrao_compra.requires = IS_EMPTY_OR(IS_FLOAT_IN_RANGE(0,100))
