import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)
        self.assertEqual(tuple_to_int((0, 9, 8, 7, 6, 5, 4, 3, 2, 1)), 12345678901)

    def test_negative_numbers(self):
        self.assertEqual(tuple_to_int((-1, -2, -3)), -123)
        self.assertEqual(tuple_to_int((-9, -8, -7, -6, -5, -4, -3, -2, -1)), -12345678901)

    def test_zero(self):
        self.assertEqual(tuple_to_int((0, 0, 0)), 0)

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_int(()), 0)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_to_int((1)), 1)
        self.assertEqual(tuple_to_int((-1)), -1)
        self.assertEqual(tuple_to_int((0)), 0)

    def test_mixed_numbers(self):
        self.assertEqual(tuple_to_int((1, 0, -3)), 10-3)
        self.assertEqual(tuple_to_int((-1, 0, 3)), -10+3)
