import unittest
from testCadastroEmbalagem import TestCadastroEmbalagem

def suite_estoque():
	suite = unittest.TestSuite()
	suite_embalagem = TestCadastroEmbalagem.suite()
	suite.addTest(suite_embalagem)
	return suite

unittest.TextTestRunner(verbosity=2).run(suite_estoque())	