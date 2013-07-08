
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
	pass

def listar_fornecedores():	
	pass

def inserir_ramo_atividade():
	form = SQLFORM(db.ramoAtividade)
	if form.process().accepted:
		response.flash = 'Registro inserido com sucesso'
	return dict(form=form)   
	