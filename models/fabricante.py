db.define_table('fabricante',
	Field('nome','string',required=True, notnull=True),
	Field('nome_fantasia','string'),
	Field('cpf_cnpj','string', required=True, notnull=True, unique=True),
	Field('inscricao_estadual','string'),
	Field('inscricao_municipal','string'),
	Field('endereco_id','reference endereco'),
	Field('telefone','string'),
	Field('email','string'),	
	Field('site','string'),
	Field('observacao','text'),
	Field('situacao','string'),
	format="%(nome)s %(cpf_cnpj)s")

db.fabricante.situacao.requires = IS_IN_SET(['ATIVO','INATIVO','BLOQUEADO'],zero=None)
db.fabricante.endereco_id.requires = IS_IN_DB(db,'endereco.id',"%(rua)s %(numero)s %(bairro)s",zero=None)					
	