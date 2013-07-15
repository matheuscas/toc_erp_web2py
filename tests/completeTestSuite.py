import unittest
from testCadastroImposto import TestCadastroImposto
from testCadastroFornecedor import TestCadastroFornecedor
from testCadastroRamoAtividade import TestCadastroRamoAtividade
from testSuiteCompras import suite_compras
from testSuiteFiscal import suite_fiscal
from testSuiteEstoque import suite_estoque

completeSuite = unittest.TestSuite()
suiteCompras = suite_compras()
suiteFiscal = suite_fiscal()
suiteEstoque = suite_estoque()
completeSuite.addTests(suiteCompras)
completeSuite.addTests(suiteFiscal)
completeSuite.addTests(suiteEstoque)

unittest.TextTestRunner(verbosity=2).run(completeSuite) 
