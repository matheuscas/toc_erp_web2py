import unittest
from testCadastroEmbalagem import TestCadastroEmbalagem
from testCadastroSecao import TestCadastroSecao
from testCadastroSubsecao import TestCadastroSubsecao
from testCadastroFabricante import TestCadastroFabricante
from testCadastroMarca import TestCadastroMarca
from testCadastroProduto import TestCadastroProduto
from test_modulo_estoque_estoquista import TestEstoquista

def suite_estoque():
	suite = unittest.TestSuite()
	#cadastros
	suite_embalagem = TestCadastroEmbalagem.suite()
	suite_secao = TestCadastroSecao.suite()
	suite_subsecao = TestCadastroSubsecao.suite()
	suite_fabricante = TestCadastroFabricante.suite()
	suite_marca = TestCadastroMarca.suite()
	suite_produto = TestCadastroProduto.suite()
	suite.addTest(suite_embalagem)
	suite.addTest(suite_secao)
	suite.addTest(suite_subsecao)
	suite.addTest(suite_fabricante)
	suite.addTest(suite_marca)
	suite.addTest(suite_produto)

	#modulos
	suite_modulo_estoque = TestEstoquista.suite()
	suite.addTest(suite_modulo_estoque)
	
	return suite
	