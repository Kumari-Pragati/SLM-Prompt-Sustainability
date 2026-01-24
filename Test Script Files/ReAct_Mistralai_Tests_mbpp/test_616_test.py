import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_normal_operation(self):
        self.assertEqual(tuple_modulo((3, 2), (1, 1)), (3, 0))
        self.assertEqual(tuple_modulo((10, 3), (2, 1)), (4, 0, 1))
        self.assertEqual(tuple_modulo((-5, 3), (-2, 1)), (2, 2))

    def test_mismatched_lengths(self):
        self.assertRaises(ValueError, tuple_modulo, (3, 2), (1))
        self.assertRaises(ValueError, tuple_modulo, (3, 2), (1, 2, 3))

    def test_negative_numbers(self):
        self.assertEqual(tuple_modulo((-3, 2), (-1, 1)), (-1, 1))
        self.assertEqual(tuple_modulo((-3, 2), (-2, -1)), (1, -1))

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, tuple_modulo, (0, 2))
