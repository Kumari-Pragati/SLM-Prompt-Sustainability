import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):
    def test_positive_tuples(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (1, 2, 3)), (1, 1, 1))
        self.assertEqual(tuple_modulo((4, 5, 6), (2, 3, 4)), (0, 2, 2))

    def test_mixed_tuples(self):
        self.assertEqual(tuple_modulo((1, 2, -3), (1, 2, 3)), (0, 1, -2))
        self.assertEqual(tuple_modulo((-1, 0, 1), (2, 2, 2)), (-1, 0, 1))

    def test_empty_tuples(self):
        self.assertEqual(tuple_modulo((), ()), ())
        self.assertEqual(tuple_modulo((1,), ()), ())
        self.assertEqual(tuple_modulo(()), ())

    def test_negative_tuples(self):
        self.assertEqual(tuple_modulo((-1, -2, -3), (-1, -2, -3)), (1, 1, 1))
