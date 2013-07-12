import unittest
from testCadastroImposto import TestCadastroImposto
from testCadastroFornecedor import TestCadastroFornecedor
from testCadastroRamoAtividade import TestCadastroRamoAtividade
from testSuiteCompras import suite_compras
from testSuiteFiscal import suite_fiscal

completeSuite = unittest.TestSuite()
suiteCompras = suite_compras()
suiteFiscal = suite_fiscal()
completeSuite.addTests(suiteCompras)
completeSuite.addTests(suiteFiscal)

unittest.TextTestRunner(verbosity=2).run(completeSuite) 
