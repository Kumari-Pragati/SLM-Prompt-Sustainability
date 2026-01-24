import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_modulo((10, 20, 30), (5, 10, 15)), (0, 0, 0))

    def test_edge_case_with_zero(self):
        self.assertEqual(tuple_modulo((0, 20, 30), (5, 10, 15)), (0, 0, 0))

    def test_edge_case_with_negative_numbers(self):
        self.assertEqual(tuple_modulo((-10, -20, -30), (5, 10, 15)), (-0, -0, -0))

    def test_edge_case_with_large_numbers(self):
        self.assertEqual(tuple_modulo((10**10, 20**10, 30**10), (10**9, 20**9, 30**9)), (10, 20, 30))

    def test_error_case_with_different_length_tuples(self):
        with self.assertRaises(ValueError):
            tuple_modulo((10, 20, 30), (5, 10))
