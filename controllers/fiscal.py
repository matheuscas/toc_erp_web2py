def inserir_imposto():
	form=crud.create(db.imposto, 
		onvalidation=valida_trinca_tipo_imposto_tipo_aliquota_e_percentual_imposto)
	return dict(form=form)

def pesquisar_imposto():
	form=SQLFORM.grid(db.imposto, user_signature=False)
	return dict(form=form)

def atualizar_imposto():
	#crud.settings.update_deletable = False
	#form = crud.update(db.imposto,request.args(0))
	form = SQLFORM(db.imposto,request.args(0))
	return dict(form=form)		
	