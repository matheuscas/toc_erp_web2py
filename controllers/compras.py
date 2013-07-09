
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
	pass

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
