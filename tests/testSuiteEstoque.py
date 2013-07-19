import unittest
from testCadastroEmbalagem import TestCadastroEmbalagem
from testCadastroSecao import TestCadastroSecao
from testCadastroSubsecao import TestCadastroSubsecao
from testCadastroFabricante import TestCadastroFabricante
from testCadastroMarca import TestCadastroMarca

def suite_estoque():
	suite = unittest.TestSuite()
	suite_embalagem = TestCadastroEmbalagem.suite()
	suite_secao = TestCadastroSecao.suite()
	suite_subsecao = TestCadastroSubsecao.suite()
	suite_fabricante = TestCadastroFabricante.suite()
	suite_marca = TestCadastroMarca.suite()
	suite.addTest(suite_embalagem)
	suite.addTest(suite_secao)
	suite.addTest(suite_subsecao)
	suite.addTest(suite_fabricante)
	suite.addTest(suite_marca)
	return suite
	