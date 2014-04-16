__author__ = 'kvogelgesang'

import sys
sys.path.append("../main")
sys.path.append("src/main")
from mock import Mock, patch, MagicMock
from configuration import SetEnv
import unittest
import sqlite


class Test_sqlite(unittest.TestCase):

    my_sqlite = sqlite
    db_name = SetEnv().resources_dir + "/cdcol.sqlite"
    db = my_sqlite.Database(db_name, __name__, sql_dialect="sqlite", in_memory=False).connect_sqlite()

    def test_get_cds_by_interpret(self):
        result = self.my_sqlite.Sql(self.db).get_cds_by_interpret("Van")
        self.assertEquals(result[0][0],"Glee")

    def test_get_cds_by_name_with_mock(self):
        my_mock_class = sqlite.Sql(True)
        my_mock_class.get_cds_by_interpret = MagicMock(return_value="Glee")
        self.assertEquals(my_mock_class.get_cds_by_interpret("Van"),"Glee")


if __name__ == '__main__':
    unittest.main()