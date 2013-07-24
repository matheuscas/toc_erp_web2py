import unittest
import sys
import os
from os import path

sys.path.append('../../../') # we need this to use web2py's modules

from gluon.sql import DAL, Field
from gluon.validators import *

class TestModuleSetup(unittest.TestCase):
	"""docstring for TestModuleSetup"""
	def setUp(self):
		db_username_postgres = 'postgres'
		db_password_postgres = '1234'
		db_postgres_url = 'postgres://' + db_username_postgres + ':' + db_password_postgres + '@localhost/dev'

		path_to_database = path.join(path.curdir, "../databases")
		self.db_test = DAL(db_postgres_url, folder=path_to_database)
		self.db_test.import_table_definitions(path_to_database)

	def limpa_dados_tabela(self, nome_tabela):
		self.db_test.executesql('delete from ' + nome_tabela)
		self.db_test.commit()		
		