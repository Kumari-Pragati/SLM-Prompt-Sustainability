import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(increment_numerics(['1', '2', '3'], 1), ['2', '3', '4'])
        self.assertEqual(increment_numerics(['10', '20', '30'], 10), ['20', '30', '40'])

    def test_edge_conditions(self):
        self.assertEqual(increment_numerics(['0', '-1', '999'], 1), ['1', '0', '1000'])
        self.assertEqual(increment_numerics(['999', '1000', '1001'], 1), ['1000', '1001', '1002'])
        self.assertEqual(increment_numerics(['0', '-999', '999'], -1), ['-998', '-1000', '998'])

    def test_boundary_conditions(self):
        self.assertEqual(increment_numerics(['999', '1000'], 1), ['1000', '1001'])
        self.assertEqual(increment_numerics(['-999', '-1000'], -1), ['-1000', '-1001'])

    def test_complex_cases(self):
        self.assertEqual(increment_numerics(['1a', '2b', '3c'], 1), ['2a', '3b', '4c'])
        self.assertEqual(increment_numerics(['10a', '20b', '30c'], 10), ['20a', '30b', '40c'])
        self.assertEqual(increment_numerics(['0', '-1', '999a'], 1), ['1', '-1', '999a'])

    def test_empty_input(self):
        self.assertEqual(increment_numerics([], 1), [])
