import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = (10, 2, 5)
        test_tup2 = (3, 4, 7)
        result = tuple_modulo(test_tup1, test_tup2)
        self.assertEqual(result, (1, 0, 3))

    def test_edge_case_zero(self):
        test_tup1 = (10, 0, 5)
        test_tup2 = (3, 4, 7)
        with self.assertRaises(ZeroDivisionError):
            tuple_modulo(test_tup1, test_tup2)

    def test_edge_case_empty_tuple(self):
        test_tup1 = ()
        test_tup2 = (1, 2, 3)
        with self.assertRaises(IndexError):
            tuple_modulo(test_tup1, test_tup2)

    def test_edge_case_tuple_of_diff_lengths(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5)
        with self.assertRaises(IndexError):
            tuple_modulo(test_tup1, test_tup2)
