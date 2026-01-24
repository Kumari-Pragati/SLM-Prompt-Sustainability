import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_typical_case(self):
        test_list = ['1', '2', '3']
        K = 2
        self.assertEqual(increment_numerics(test_list, K), ['3', '4', '5'])

    def test_edge_case(self):
        test_list = ['9', '99', '999']
        K = 1
        self.assertEqual(increment_numerics(test_list, K), ['10', '100', '1000'])

    def test_boundary_case(self):
        test_list = ['99', '999', '9999']
        K = 10
        self.assertEqual(increment_numerics(test_list, K), ['109', '1099', '10999'])

    def test_corner_case(self):
        test_list = ['0', '00', '000']
        K = 1
        self.assertEqual(increment_numerics(test_list, K), ['1', '01', '001'])

    def test_invalid_input(self):
        test_list = ['1', '2', 'abc']
        K = 1
        with self.assertRaises(TypeError):
            increment_numerics(test_list, K)
