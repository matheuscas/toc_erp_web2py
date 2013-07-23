import datetime

db.define_table('condicao_pagamento',
	Field('descricao','string', required=True, notnull=True),
	Field('data_vencimento','date',required=True, notnull=True),
	Field('desconto','decimal(3,1)'),
	Field('acrescimo','decimal(3,1)'),
	Field('numero_parcelas','integer',required=True, notnull=True),
	Field('situacao','string',required=True,notnull=True),
	Field('data_cadastro','date', writable=False, 
		default=datetime.date(datetime.datetime.now().year,
							datetime.datetime.now().month,
							datetime.datetime.now().day)),
	format='%(descricao)s')

db.condicao_pagamento.situacao.requires = IS_IN_SET(['ATIVO','INATIVO'],zero=None)
db.condicao_pagamento.desconto.requires = IS_EMPTY_OR(IS_DECIMAL_IN_RANGE(0, 100, dot="."))
db.condicao_pagamento.acrescimo.requires = IS_EMPTY_OR(IS_DECIMAL_IN_RANGE(0, 100, dot="."))
db.condicao_pagamento.data_vencimento.requires = IS_DATE_IN_RANGE(format=T('%Y-%m-%d'),
                   minimum=datetime.date(datetime.datetime.now().year,
							datetime.datetime.now().month,
							datetime.datetime.now().day),
                   error_message='invalid format(YYYY-MM-DD) or value')
db.condicao_pagamento.numero_parcelas.requires = IS_INT_IN_RANGE(0, 100,
         error_message='the value is too small or too large')

