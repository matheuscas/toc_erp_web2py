import unittest
from testCadastroFornecedor import TestCadastroFornecedor
from testCadastroRamoAtividade import TestCadastroRamoAtividade

def suite_compras():
	suite = unittest.TestSuite()
	suiteCadastroFornecedor = TestCadastroFornecedor.suite()
	suiteCadastroRamoAtividade = TestCadastroRamoAtividade.suite()
	suite.addTests(suiteCadastroFornecedor)
	suite.addTests(suiteCadastroRamoAtividade)
	return suite
	

#unittest.TextTestRunner(verbosity=2).run(suite_compras()) 

