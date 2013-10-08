db.define_table('fabricante',
	Field('nome','string',required=True, notnull=True),
	Field('nome_fantasia','string'),
	Field('cpf_cnpj','string', required=True, notnull=True, unique=True, length=255),
	Field('inscricao_estadual','string'),
	Field('inscricao_municipal','string'),
	Field('telefone','string'),
	Field('email','string'),	
	Field('site','string'),
	Field('observacao','text'),
	Field('situacao','string'),
	format="%(nome)s %(cpf_cnpj)s")

db.fabricante.situacao.requires = IS_IN_SET(['ATIVO','INATIVO','BLOQUEADO'],zero=None)				
	