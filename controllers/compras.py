import compras
import financeiro
import estoque 

import gluon.contrib.simplejson as simplejson
import urllib 

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
	cookies = True
	if request.cookies.has_key('itens'):		
		decoded = urllib.unquote(request.cookies['itens'].value).decode('utf8')
		json = simplejson.loads(decoded)
		if len(json) == 0:
			cookies = False	 

	redirect_vars = {}		

	if cookies and form.process().accepted:
		capa_nota_fiscal = compras.NotaFiscalCompra(form.vars.numero,form.vars.data_emissao,
							form.vars.data_chegada,form.vars.natureza_operacao,
							form.vars.fornecedor_id,form.vars.base_calculo_icms,
							form.vars.valor_icms,form.vars.valor_ipi,
							form.vars.frete, form.vars.outras, form.vars.desconto,
							form.vars.condicao_pagamento_id, form.vars.total)

		gerenteFinanceiro = financeiro.GerenteFinanceiro()

		gerenteFinanceiro.gerar_automaticamente_conta_pagar_fornecedor(capa_nota_fiscal)

		estoquista = estoque.Estoquista()

		itens = []

		for item in json:
			db.item_compra.insert(produto_id=item['id'],nota_fiscal_id=form.vars.id,
											descricao=item['descricao'],preco_unitario=item['valor_unitario'],
											quantidade=item['quantidade'],unidade_compra=item['unidade'],
											aliquota_icms=item['aliquota'],total_item=item['valor_total'])
			item_da_nota_fiscal = estoque.ItemNotaFiscal()
			item_da_nota_fiscal.produto_id = item['id']
			item_da_nota_fiscal.descricao = item['descricao']
			item_da_nota_fiscal.total = item['valor_total']

			estoquista.criar_registro_de_entrada_no_estoque(item_da_nota_fiscal)

			itens.append(item['id'])

		redirect_vars = {"nota_id":form.vars.id, "itens_nota":itens}	
		redirect(URL('nota_fiscal_compra_espelho',vars=redirect_vars))

		#response.flash = 'Registro inserido com sucesso'
	elif form.errors:
		response.flash = 'O formulario contem erros.'
	return dict(form=form)

def nota_fiscal_compra_espelho():
	nota_fiscal = db(db.nota_fiscal_compra.id == request.vars.nota_id).select()
	itens_da_nota = db(db.item_compra.nota_fiscal_id == request.vars.nota_id).select()
	lancamentos_da_nota = db(db.conta_pagar.numero_nota_fiscal == nota_fiscal[0].numero).select()
	contabeis = []
	for l in lancamentos_da_nota:
		contabil = db(db.lancamento_contabil.transacao == l.numero_titulo).select()
		contabeis.append(contabil[0])

	return dict(nota_fiscal=nota_fiscal[0], itens_da_nota=itens_da_nota,
		lancamentos_da_nota=lancamentos_da_nota, contabeis=contabeis)

def retornar_dados_produto():
	prod_rows = db(db.produto.id == request.vars.id).select()
	if len(prod_rows) > 0:
		return prod_rows[0].nome + "," + prod_rows[0].unidade_medida + "," + str(len(prod_rows))
	else:
		return "none,none,0" 	
	
