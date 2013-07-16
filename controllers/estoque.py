def inserir_embalagem():
	form = crud.create(db.embalagem, onvalidation=valida_unidade_medida_e_quantidade_casas_decimais)
	return dict(form=form)

def pesquisar_embalagens():
	form = SQLFORM.grid(db.embalagem)
	return dict(form=form)

def atualizar_embalagem():
	crud.settings.update_deletable = False	
	form = crud.update(db.embalagem, request.args(0))
	return dict(form=form)	

def inserir_secao():
	form = crud.create(db.secao)
	return dict(form=form)

def pesquisar_secoes():
	form = SQLFORM.grid(db.secao)
	return dict(form=form)

def atualizar_secao():
	crud.settings.update_deletable = False
	form = crud.update(db.secao, request.args(0))
	return dict(form=form)	