import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (4, 5, 6)), (1, 3, 2))
        self.assertEqual(tuple_modulo((-1, 0, 1), (2, 3, 4)), (-1, 0, 1))
        self.assertEqual(tuple_modulo((5, -3, 7), (2, -4, 6)), (1, 3, 1))

    def test_edge_case_zero(self):
        self.assertEqual(tuple_modulo((0, 0), (1, 0)), (0,))
        self.assertEqual(tuple_modulo((0, 1), (0, 0)), (1,))
        self.assertEqual(tuple_modulo((0, 0), (0, 1)), (0,))

    def test_edge_case_negative(self):
        self.assertEqual(tuple_modulo((-1, -2), (3, 4)), (-2, -3))
        self.assertEqual(tuple_modulo((-1, -2), (-3, -4)), (1, 2))

    def test_edge_case_longer(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (4, 5, 6, 7)), (1, 3, 2))
        self.assertEqual(tuple_modulo((1, 2, 3, 4), (4, 5, 6)), (1, 3, 2, 0))

    def test_edge_case_shorter(self):
        self.assertEqual(tuple_modulo((1, 2), (4, 5, 6)), (1, 2))
        self.assertEqual(tuple_modulo((1, 2, 3), (4, 5)), (1, 3, 2))
