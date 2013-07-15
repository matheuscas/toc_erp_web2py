db.define_table('embalagem',
	Field('nome','string',required=True,notnull=True,unique=True),
	Field('unidade_medida','string',required=True,notnull=True),
	Field('quantidade_casas_decimais','string',required=True,notnull=True),
	Field('situacao','string',required=True,notnull=True),
	format = '%(nome) - %(unidade_medida) - %(quantidade_casas_decimais)')

db.embalagem.nome.requires = [IS_NOT_EMPTY(),IS_UPPER(),CLEANUP(),IS_NOT_IN_DB(db, 'embalagem.nome')]
db.embalagem.quantidade_casas_decimais.requires = IS_IN_SET(['0','1','2','3'],zero=None)
db.embalagem.situacao.requires = IS_IN_SET(['ATIVO','INATIVO'],zero=None)

def valida_unidade_medida_e_quantidade_casas_decimais(form):
	rows = db(db.embalagem.unidade_medida == form.vars.unidade_medida and
	 		db.embalagem.quantidade_casas_decimais == form.vars.quantidade_casas_decimais).select()
	if len(rows) > 0:
	 	form.errors.unidade_medida = 'value already in database'
	 	form.errors.quantidade_casas_decimais = 'value already in database'