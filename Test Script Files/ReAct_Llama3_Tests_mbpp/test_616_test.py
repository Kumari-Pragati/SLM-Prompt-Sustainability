import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (2, 3, 4)), (1, 0, 1))

    def test_edge_case_zero(self):
        self.assertRaises(ZeroDivisionError, tuple_modulo, (1, 2, 3), (0, 3, 4))

    def test_edge_case_negative(self):
        self.assertEqual(tuple_modulo((-1, 2, 3), (2, 3, 4)), (-1, 0, 1))

    def test_edge_case_single_element(self):
        self.assertEqual(tuple_modulo((1,), (2,)), (1,))

    def test_edge_case_empty(self):
        with self.assertRaises(IndexError):
            tuple_modulo((), (1,))

    def test_edge_case_single_element_zero(self):
        self.assertRaises(ZeroDivisionError, tuple_modulo, (0,), (2,))

    def test_edge_case_empty_zero(self):
        with self.assertRaises(IndexError):
            tuple_modulo((), (0,))
