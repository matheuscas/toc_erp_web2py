import unittest
from test_cadastro_condicao_pagamento import TestCadastroCondicaoPagamento
from test_modulo_financeiro import TestGerenteFinanceiro

def suite_financeiro():
	suite = unittest.TestSuite()
	suite_condicao_pagamento = TestCadastroCondicaoPagamento.suite()
	suite_modulo_financeiro_gerente_financeiro = TestGerenteFinanceiro.suite()
	suite.addTest(suite_condicao_pagamento)
	suite.addTest(suite_modulo_financeiro_gerente_financeiro)
	return suite