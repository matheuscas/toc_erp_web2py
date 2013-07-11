import unittest
from testCadastroFornecedor import TestCadastroFornecedor
from testCadastroRamoAtividade import TestCadastroRamoAtividade

suite = unittest.TestSuite()
suiteCadastroFornecedor = TestCadastroFornecedor.suite()
suiteCadastroRamoAtividade = TestCadastroRamoAtividade.suite()

suite.addTests(suiteCadastroFornecedor)
suite.addTests(suiteCadastroRamoAtividade)

unittest.TextTestRunner(verbosity=2).run(suite)

