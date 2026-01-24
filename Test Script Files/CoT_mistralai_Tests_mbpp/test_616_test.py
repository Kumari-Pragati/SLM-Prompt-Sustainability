import unittest
from mbpp_616_code import tuple_modulo

class TestTupleModulo(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(tuple_modulo((1, 2, 3), (4, 5, 6)), (1, 3, 2))
        self.assertEqual(tuple_modulo((-1, 2, -3), (4, 5, 6)), (-1, 3, -2))
        self.assertEqual(tuple_modulo((0, 2, 0), (4, 5, 6)), (0, 2, 0))

    def test_mixed_types(self):
        self.assertRaises(TypeError, lambda: tuple_modulo((1, 2, 3), 'abc'))
        self.assertRaises(TypeError, lambda: tuple_modulo('xyz', (1, 2, 3)))

    def test_empty_tuples(self):
        self.assertEqual(tuple_modulo((), ()), ())
        self.assertRaises(ValueError, lambda: tuple_modulo((1,), ()))
        self.assertRaises(ValueError, lambda: tuple_modulo((), (1,)))

    def test_single_element_tuples(self):
        self.assertEqual(tuple_modulo((1,), (2,)), (1,))
        self.assertEqual(tuple_modulo((2,), (1,)), (0,))

    def test_negative_numbers(self):
        self.assertEqual(tuple_modulo((-1, -2, -3), (-4, -5, -6)), (1, 3, 2))
        self.assertEqual(tuple_modulo((-1, -2, -3), (4, 5, 6)), (-1, -3, -2))

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, lambda: tuple_modulo((0,), (0,)))
