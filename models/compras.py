db.define_table('endereco',
	Field('rua','string',required=True, notnull=True),
	Field('numero','integer'),
	Field('bairro','string',required=True, notnull=True),
	Field('cidade','string',required=True, notnull=True),
	Field('estado','string',required=True, notnull=True),
	Field('cep','string',requires=IS_LENGTH(8)),
	format=lambda f: f.rua + '/' + f.bairro)

db.define_table('pessoaContato',
	Field('nome','string'),
	Field('telefone','string'),
	format=lambda f: f.nome + ':' + f.telefone)

db.define_table('fornecedor',
	Field('nome','string',required=True, notnull=True),
	Field('nomeFantasia','string'),
	Field('cpf_cnpj','integer',required=True,notnull=True,unique=True),
	Field('endereco_id','reference endereco',required=True,notnull=True),
	Field('email','string'),
	Field('telefone','string'),
	Field('contato_id','reference pessoaContato'),
	Field('historico','text'),
	format=lambda f: f.nome + '-' + f.cpf_cnpj)

db.define_table('ramoAtividade',
	Field('nome','string',required=True, notnull=True),
	Field('descricao','text'),
	Field('forncedor_id','reference fornecedor'),
	format= lambda f: f.nome + '(s)')