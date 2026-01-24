import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(tuple_modulo((10, 20, 30), (5, 10, 15)), (0, 0, 0))

    def test_negative_numbers(self):
        self.assertEqual(tuple_modulo((-10, -20, -30), (5, 10, 15)), (0, 0, 0))

    def test_mixed_numbers(self):
        self.assertEqual(tuple_modulo((10, -20, 30), (5, -10, 15)), (0, 0, 0))

    def test_different_lengths(self):
        self.assertEqual(tuple_modulo((10, 20), (5, 10)), (0, 0))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            tuple_modulo((10, 20, 30), (0, 10, 0))
