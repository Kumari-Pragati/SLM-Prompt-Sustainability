import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_single_digit(self):
        self.assertEqual(tuple_to_int((9)), 9)

    def test_zero(self):
        self.assertEqual(tuple_to_int((0)), 0)

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_int(()), 0)

    def test_negative_numbers(self):
        self.assertEqual(tuple_to_int((-1, -2, -3)), -123)

    def test_large_numbers(self):
        self.assertEqual(tuple_to_int((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)), 1234567890)

    def test_with_zero_in_middle(self):
        self.assertEqual(tuple_to_int((1, 2, 0, 3)), 1203)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            tuple_to_int(("1", "2", "3"))

    def test_with_float(self):
        with self.assertRaises(ValueError):
            tuple_to_int((1.1, 2.2, 3.3))
