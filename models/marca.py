db.define_table('marca',
	Field('nome','string',required=True, notnull=True, unique=True),
	Field('imagem','upload'),
	Field('fabricante_id','list:reference fabricante',required=True,notnull=True),
	Field('situacao','string',required=True,notnull=True),
	format='%(nome)s %(situacao)s')

db.marca.nome.requires = [IS_NOT_EMPTY(), IS_UPPER(), CLEANUP(), IS_NOT_IN_DB(db,'marca.nome')]
db.marca.fabricante_id.requires = IS_IN_DB(db,'fabricante.id',db.fabricante._format,multiple=True)
db.marca.situacao.requires = IS_IN_SET(['ATIVO','INATIVO'],zero=None)