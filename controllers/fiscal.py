def inserir_imposto():
	form=crud.create(db.imposto, 
		onvalidation=valida_trinca_tipo_imposto_tipo_aliquota_e_percentual_imposto)
	return dict(form=form)
	