import unittest
from testCadastroImposto import TestCadastroImposto

def suite_fiscal():
	suite = unittest.TestSuite()
	suiteCadastroImposto = TestCadastroImposto.suite()
	suite.addTest(suiteCadastroImposto)
	return suite
	

#unittest.TextTestRunner(verbosity=2).run(suite_fiscal())	