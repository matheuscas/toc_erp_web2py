db.define_table('embalagem',
	Field('nome','string',required=True,notnull=True,unique=True),
	Field('unidade_medida','string',required=True,notnull=True),
	Field('quantidade_casas_decimais',required=True,notnull=True),
	format = '%(nome) - %(unidade_medida) - %(quantidade_casas_decimais)')

db.embalagem.nome.requires = [IS_NOT_EMPTY(),IS_UPPER(),CLEANUP(),IS_NOT_IN_DB(db, 'embalagem.nome')]
db.embalagem.quantidade_casas_decimais.requires = IS_IN_SET([0,1,2,3],zero=None)

def valida_unidade_medida_e_quantidade_casas_decimais():
	pass