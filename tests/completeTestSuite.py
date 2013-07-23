import unittest
from testCadastroImposto import TestCadastroImposto
from testCadastroFornecedor import TestCadastroFornecedor
from testCadastroRamoAtividade import TestCadastroRamoAtividade
from testSuiteCompras import suite_compras
from testSuiteFiscal import suite_fiscal
from testSuiteEstoque import suite_estoque
from test_suite_financeiro import suite_financeiro

completeSuite = unittest.TestSuite()
suiteCompras = suite_compras()
suiteFiscal = suite_fiscal()
suiteEstoque = suite_estoque()
suite_financeiro = suite_financeiro()
completeSuite.addTests(suiteCompras)
completeSuite.addTests(suiteFiscal)
completeSuite.addTests(suiteEstoque)
completeSuite.addTests(suite_financeiro)

unittest.TextTestRunner(verbosity=2).run(completeSuite) 
