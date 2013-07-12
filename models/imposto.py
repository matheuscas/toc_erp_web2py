db.define_table('imposto',
	Field('nome_imposto','string',required=True,unique=True,notnull=True),
	Field('tipo_imposto','list:string',required=True),
	Field('tipo_aliquota_imposto','list:string', required=True),
	Field('percentual_imposto','decimal(4,2)',required=True, notnull=True),
	Field('situacao_imposto','list:string',required=True,notnull=True),
	format= '%(nome_imposto), %(tipo_imposto), %(tipo_aliquota_imposto), %(percentual_imposto)')

db.imposto.nome_imposto.requires = [IS_NOT_EMPTY(),IS_UPPER(),CLEANUP(),IS_NOT_IN_DB(db, 'imposto.nome_imposto')]
db.imposto.tipo_imposto.requires = IS_IN_SET(['IPI','ICMS','PIS','COFINS'],zero=T('Choose a type'))
db.imposto.tipo_aliquota_imposto.requires= IS_IN_SET(['Isento','Substituido', 'Tributado', 'Nao Tributado'],
	zero=T('Choose an aliquot'))
db.imposto.situacao_imposto.requires = IS_IN_SET(['ATIVO','INATIVO'],zero=T('Choose a status'))

def valida_trinca_tipo_imposto_tipo_aliquota_e_percentual_imposto(form):
	print form.vars.tipo_imposto, form.vars.tipo_aliquota_imposto, form.vars.percentual_imposto

	rows = db(db.imposto.tipo_imposto == form.vars.tipo_imposto and 
		db.imposto.tipo_aliquota_imposto == form.vars.tipo_aliquota_imposto and
		db.imposto.percentual_imposto == form.vars.percentual_imposto).select()
	if len(rows) > 0:
		form.errors.tipo_imposto = 'value already in database'
		form.errors.tipo_aliquota_imposto = 'value already in database'
		form.errors.percentual_imposto = 'value already in database'