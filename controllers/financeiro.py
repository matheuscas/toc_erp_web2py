def inserir_condicao_pagamento():
	form = crud.create(db.condicao_pagamento)
	return dict(form=form)

def pesquisar_condicoes_pagamento():
	form = SQLFORM.grid(db.condicao_pagamento)
	return dict(form=form)

def atualizar_condicao_pagamento():
	crud.settings.update_deletable = False
	form = crud.create(db.condicao_pagamento, request.args(0))
	return dict(form=form)		