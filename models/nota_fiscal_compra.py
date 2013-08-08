db.define_table('nota_fiscal_compra',
	Field('numero','integer',required=True, notnull=True, unique=True),
	Field('data_emissao','date',required=True, notnull=True),
	Field('data_chegada','date',required=True, notnull=True),
	Field('natureza_operacao',required=True, notnull=True),
	Field('fornecedor_id','reference fornecedor'),
	Field('item_compra_id','list:reference item_compra'),
	Field('base_calculo_icms','double'),
	Field('valor_icms','decimal(4,2)'),
	Field('valor_ipi','decimal(4,2)'),
	Field('frete','double'),
	Field('outras','double'),
	Field('desconto','decimal(4,2)'),
	Field('condicao_pagamento_id','reference condicao_pagamento'),
	Field('total','double',required=True, notnull=True),
	format='%(numero)s')