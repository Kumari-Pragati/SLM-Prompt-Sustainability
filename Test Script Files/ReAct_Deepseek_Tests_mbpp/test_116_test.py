import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_single_digit_case(self):
        self.assertEqual(tuple_to_int((9)), 9)

    def test_zero_case(self):
        self.assertEqual(tuple_to_int((0)), 0)

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_int(()), 0)

    def test_negative_number_case(self):
        self.assertEqual(tuple_to_int((-1, -2, -3)), -123)

    def test_large_number_case(self):
        self.assertEqual(tuple_to_int((1, 2, 3, 4, 5, 6, 7, 8, 9)), 123456789)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            tuple_to_int((1, 2.5, 3))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tuple_to_int([1, 2, 3])
