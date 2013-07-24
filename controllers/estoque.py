#EMBALAGEM
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

#SECAO
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

#SUBSECAO
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

#FABRICANTE
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

#MARCA
def inserir_marca():
	form = crud.create(db.marca)
	return dict(form=form)

def pesquisar_marcas():
	form = SQLFORM.grid(db.marca)
	return dict(form=form)

def atualizar_marca():
	crud.settings.update_deletable = False
	form = crud.update(db.marca, request.args(0))
	return dict(form=form)

#PRODUTO
def inserir_produto():
	form = crud.create(db.produto)	
	return dict(form=form)

def pesquisar_produtos():
	form = SQLFORM.grid(db.produto)
	return dict(form=form)

def atualizar_produto():
	crud.settings.update_deletable = False
	form = crud.update(db.produto, request.args(0))
	return dict(form=form)	

#ESTOQUE
def pesquisar_estoque():
	form = SQLFORM.grid(db.registro_estoque)
	return dict(form=form)		