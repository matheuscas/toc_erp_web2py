import unittest
from test_cadastro_condicao_pagamento import TestCadastroCondicaoPagamento

def suite_financeiro():
	suite = unittest.TestSuite()
	suite_condicao_pagamento = TestCadastroCondicaoPagamento.suite()
	suite.addTest(suite_condicao_pagamento)
	return suite