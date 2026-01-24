import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(tuple_to_float((1, 2, 3)), 1.23)

    def test_single_digit(self):
        self.assertAlmostEqual(tuple_to_float((4)), 4.0)

    def test_zero(self):
        self.assertAlmostEqual(tuple_to_float((0, 0, 0)), 0.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(tuple_to_float((-1, -2, -3)), -1.23)

    def test_large_numbers(self):
        self.assertAlmostEqual(tuple_to_float((10, 20, 30)), 10.2030)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(tuple_to_float((1.1, 2.2, 3.3)), 1.123)

    def test_empty_tuple(self):
        with self.assertRaises(ValueError):
            tuple_to_float(())

    def test_non_integer_elements(self):
        with self.assertRaises(ValueError):
            tuple_to_float((1, 2.2, '3'))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tuple_to_float(123)
