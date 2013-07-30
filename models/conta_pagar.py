db.define_table('conta_pagar',
	Field('numero_titulo','integer',required=True, notnull=True),
	Field('parcela','integer',required=True, notnull=True),
	Field('numero_documento'),
	Field('numero_nota_fiscal'),
	Field('fornecedor_id','reference fornecedor'),
	Field('categoria'),
	Field('historico'),
	Field('data_emissao','date'),
	Field('data_vencimento','date'),
	Field('data_criacao','date'),
	Field('valor_nominal','double'),
	Field('valor_parcela','double'),
	Field('valor_pago','double'),
	Field('valor_juros_pago','double'),
	Field('valor_encargos_pago','double'),
	Field('valor_desconto_recebido','double'),
	Field('perc_juros_atraso','double'),
	Field('acrescimo','double'),
	Field('encargos','double'),
	Field('status'),
	format='%(numero_titulo)s - %(fornecedor_id)s - %(valor_parcela)s')


db.conta_pagar.categoria.requires = IS_IN_SET(['CUSTO FIXO','CUSTO VARIAVEL','FORNECEDOR'],zero=None)
db.conta_pagar.status.requires = IS_IN_SET(['ABERTO','FECHADO','CANCELADO'], zero=None)