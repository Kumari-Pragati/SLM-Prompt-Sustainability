import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tuple_modulo((10, 3, 5), (2, 1, 4)), (1, 2, 1))

    def test_edge_case_zero(self):
        with self.assertRaises(ZeroDivisionError):
            tuple_modulo((10, 3, 5), (0, 1, 4))

    def test_edge_case_negative(self):
        self.assertEqual(tuple_modulo((-10, 3, 5), (2, 1, 4)), (-1, 2, 1))

    def test_edge_case_single_element(self):
        self.assertEqual(tuple_modulo((10,), (2,)), (0,))

    def test_edge_case_empty(self):
        with self.assertRaises(IndexError):
            tuple_modulo((), (2,))

    def test_edge_case_mismatched_length(self):
        with self.assertRaises(IndexError):
            tuple_modulo((10, 3, 5), (2, 1))
