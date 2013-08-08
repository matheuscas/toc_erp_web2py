import compras
import financeiro
import estoque

def inserir_fornecedor():
	form = SQLFORM.factory(db.fornecedor, db.endereco, db.contato)
	if form.process().accepted:

	   id = db.endereco.insert(**db.endereco._filter_fields(form.vars))	
	   form.vars.endereco = id

	   id = db.contato.insert(**db.contato._filter_fields(form.vars))
	   form.vars.contato_id = id

	   id = db.fornecedor.insert(**db.fornecedor._filter_fields(form.vars))

	   response.flash = 'Registro inserido com sucesso'
	return dict(form=form)   

def atualizar_fornecedor():
	fornecedor = db.fornecedor(request.args(0))
	form_fornecedor = SQLFORM(db.fornecedor, fornecedor.id)
	form_contato = SQLFORM(db.contato, fornecedor.contato_id)
	form_endereco = SQLFORM(db.endereco, fornecedor.endereco)

	form_fornecedor.append(form_endereco)
	form_fornecedor.append(form_contato)

	if form_fornecedor.process().accepted:
	   id = db.endereco.update(**db.endereco._filter_fields(form_fornecedor.vars))	
	   form_fornecedor.vars.endereco = id

	   id = db.contato.update(**db.contato._filter_fields(form_fornecedor.vars))
	   form_fornecedor.vars.contato_id = id

	   id = db.fornecedor.update(**db.fornecedor._filter_fields(form_fornecedor.vars))

	   response.flash = 'Registro inserido com sucesso'
	elif form_fornecedor.errors:
		response.flash = 'Registro nao atualizado. Verifique o preenchimento.'
	return dict(form_fornecedor=form_fornecedor)	   

def listar_fornecedores():	
	grid = SQLFORM.grid(db.fornecedor,user_signature=False)
	return dict(form=grid)

#RAMOS DE ATIVIDADE
def inserir_ramo_atividade():
	form = SQLFORM(db.ramoAtividade)
	if form.process().accepted:
		response.flash = 'Registro inserido com sucesso'
	return dict(form=form)   
	
"""def atualizar_ramo_atividade():
	ramo = db.ramoAtividade(request.args(0))
	form = SQLFORM(db.ramoAtividade, ramo, deletable=True)
	if form.process().accepted:
		response.flash = 'Ramo de atividade alterado com sucesso.'
	elif form.errors:
		response.flash = 'Registro nao atualizado. Verifique o preenchimento.'	
	return dict(form=form)"""

def nota_fiscal_compra():
	form = SQLFORM(db.nota_fiscal_compra)

	if form.process().accepted:
		#cria objeto da Nota fiscal
		#cria lista de objetos de itens da nota fiscal
		#Passa o objeto para metodo que gera a conta a pagar ao fornecedor
		#Passa o objeto para metodo que gera debito e credito da transacao
		#Passa lista de itens para metodo de estoque para atualiza-lo
		"""capa_nota_fiscal = compras.NotaFiscalCompra(form.vars.numero,form.vars.data_emissao,
													form.vars.data_chegada,form.vars.natureza_operacao,
													form.vars.fornecedor_id,form.vars.base_calculo_icms,
													form.vars.valor_icms,form.vars.valor_ipi,
													form.vars.frete, form.vars.outras, form.vars.desconto,
													form.vars.condicao_pagamento_id, form.vars.total)
		gerenteFinanceiro = financeiro.GerenteFinanceiro()
		gerenteFinanceiro.gerar_automaticamente_conta_pagar_fornecedor(capa_nota_fiscal)"""

		response.flash = 'Registro inserido com sucesso'
	elif form.errors:
		response.flash = 'O formulario contem erros.'
	return dict(form=form)
