import unittest
from testCadastroEmbalagem import TestCadastroEmbalagem
from testCadastroSecao import TestCadastroSecao

def suite_estoque():
	suite = unittest.TestSuite()
	suite_embalagem = TestCadastroEmbalagem.suite()
	suite_secao = TestCadastroSecao.suite()
	suite.addTest(suite_embalagem)
	suite.addTest(suite_secao)
	return suite
	