db.define_table('secao',
	Field('nome','string',required=True, notnull=True, unique=True),
	Field('descricao','text'),
	format = '%(secao)')

db.secao.nome.requires = [IS_NOT_EMPTY(),IS_UPPER(),CLEANUP(),IS_NOT_IN_DB(db, 'secao.nome')]