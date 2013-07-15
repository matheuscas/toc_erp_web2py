def inserir_embalagem():
	form = crud.create(db.embalagem, onvalidation=valida_unidade_medida_e_quantidade_casas_decimais)
	return dict(form=form)

def pesquisar_embalagens():
	form = SQLFORM.grid(db.embalagem)
	return dict(form=form)

def atualizar_embalagem():
	#form = SQLFORM(db.embalagem, request.args(0))
	form = SQLFORM(db.embalagem,request.args(0))
	return dict(form=form)	