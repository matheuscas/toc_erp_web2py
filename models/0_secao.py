db.define_table('secao',
	Field('nome','string',required=True, notnull=True, unique=True, length=255),
	Field('descricao','text'),
	Field('situacao','string',required=True,notnull=True),
	format = '%(nome)s')

db.secao.nome.requires = [IS_NOT_EMPTY(),IS_UPPER(),CLEANUP(),IS_NOT_IN_DB(db, 'secao.nome')]
db.secao.situacao.requires = IS_IN_SET(['ATIVO','INATIVO'],zero=None)
