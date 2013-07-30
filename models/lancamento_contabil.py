db.define_table('lancamento_contabil',
	Field('valor','double',required=True, notnull=True),
	Field('conta_credito',required=True, notnull=True),
	Field('conta_debito',required=True, notnull=True),
	Field('transacao','integer',required=True, notnull=True),
	Field('data_lancamento','date',required=True, notnull=True),
	format='%(conta_credito)s - %(conta_debito)s - %(valor)s')
