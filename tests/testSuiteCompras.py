import unittest
from testCadastroFornecedor import *

suiteCadastroFornecedor = TestCadastroFornecedor.suite()
unittest.TextTestRunner(verbosity=2).run(suiteCadastroFornecedor)

