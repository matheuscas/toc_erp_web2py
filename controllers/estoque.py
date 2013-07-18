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

def inserir_subsecao():
	form = crud.create(db.subsecao)
	return dict(form=form)

def pesquisar_subsecoes():
	form = SQLFORM.grid(db.subsecao)
	return dict(form=form)

def	atualizar_subsecao():
	crud.settings.update_deletable = False
	form = crud.update(db.subsecao, request.args(0))
	return dict(form=form)

def inserir_fabricante():
	form = crud.create(db.fabricante)
	return dict(form = form)

def pesquisar_fabricantes():
	form = SQLFORM.grid(db.fabricante)
	return dict(form=form)

def atualizar_fabricante():
	crud.settings.update_deletable = False
	form = crud.update(db.fabricante,request.args(0))
	return dict(form=form)			
	