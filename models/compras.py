db.define_table('endereco',
	Field('rua','string',required=True, notnull=True),
	Field('numero','integer'),
	Field('bairro','string',required=True, notnull=True),
	Field('cidade','string',required=True, notnull=True),
	Field('estado','string',required=True, notnull=True),
	Field('cep','string',length=8),
	format='%(rua), %(numero), %(bairro)')

db.define_table('contato',
	Field('nome_contato','string'),
	Field('telefone_contato','string'), 
	format='%(nome_contato) - %(telefone_contato)')

db.define_table('fornecedor',
	Field('nome','string',required=True, notnull=True),
	Field('nomeFantasia','string'),
	Field('cpf_cnpj','string',required=True,notnull=True,unique=True, length=14),
	Field('endereco','reference endereco',writable=False, readable=False),
	Field('email','string'),
	Field('telefone','string'),
	Field('contato_id','reference contato', writable=False, readable=False),
	Field('historico','text'),
	format='%(nomeFantasia) - %(cpf_cnpj)')

db.define_table('ramoAtividade',
	Field('nome_ramo','string',required=True, notnull=True),
	Field('descricao','text'),
	Field('fornecedor_id','reference fornecedor', writable=False, readable=False), 
	format='%(nome_ramo)')