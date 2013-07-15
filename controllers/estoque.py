def inserir_embalagem():
	form = crud.create(db.embalagem)
	return dict(form=form)