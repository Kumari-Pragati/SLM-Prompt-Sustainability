import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(increment_numerics(['1', '2', '3'], 2), ['3', '4', '5'])
        self.assertEqual(increment_numerics(['10', '20', '30'], 10), ['20', '30', '40'])

    def test_edge_cases(self):
        self.assertEqual(increment_numerics(['0', '9', '99'], 1), ['1', '10', '100'])
        self.assertEqual(increment_numerics(['9', '99', '999'], 10), ['19', '109', '1099'])

    def test_boundary_conditions(self):
        self.assertEqual(increment_numerics(['99', '999', '9999'], 1), ['100', '1000', '10000'])
        self.assertEqual(increment_numerics(['999', '9999', '99999'], 10), ['1009', '10009', '100009'])

    def test_corner_cases(self):
        self.assertEqual(increment_numerics(['001', '010', '100'], 1), ['002', '011', '101'])
        self.assertEqual(increment_numerics(['000', '0000', '00000'], 1), ['001', '0001', '00001'])
