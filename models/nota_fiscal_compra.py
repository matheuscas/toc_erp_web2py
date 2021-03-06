import gluon.contrib.simplejson as simplejson
import urllib 

db.define_table('nota_fiscal_compra',
	Field('numero','integer',required=True, notnull=True, unique=True, length=255),
	Field('data_emissao','date',required=True, notnull=True),
	Field('data_chegada','date',required=True, notnull=True),
	Field('natureza_operacao',required=True, notnull=True),
	Field('fornecedor_id','reference fornecedor'),
	Field('base_calculo_icms','double'),
	Field('valor_icms','decimal(4,2)'),
	Field('valor_ipi','decimal(4,2)'),
	Field('frete','double'),
	Field('outras','double'),
	Field('desconto','decimal(4,2)'),
	Field('condicao_pagamento_id','reference condicao_pagamento'),
	Field('total','double',required=True, notnull=True),
	format='%(numero)s')

def valida_itens(form):
	if request.cookies.has_key('itens'):		
		decoded = urllib.unquote(request.cookies['itens'].value).decode('utf8')
		json = simplejson.loads(decoded)
		if len(json) == 0:
			form.errors.cod_prod = 'A nota nao pode ser confirmada sem itens.'
			response.flash = 'A nota nao pode ser confirmada sem itens.'