db.define_table('subsecao',
	Field('nome','string',required=True, notnull=True, unique=True, length=255),
	Field('descricao','text'),
	Field('situacao','string',required=True,notnull=True),
	Field('secao_id','reference secao',required=True,notnull=True),
	format = '%(nome)s')

db.subsecao.secao_id.requires = IS_IN_DB(db, 'secao.id', '%(nome)s',zero=None)
db.subsecao.nome.requires = [IS_NOT_EMPTY(),IS_UPPER(),CLEANUP(),IS_NOT_IN_DB(db, 'subsecao.nome')]
db.subsecao.situacao.requires = IS_IN_SET(['ATIVO','INATIVO'],zero=None)