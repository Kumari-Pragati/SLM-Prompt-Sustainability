import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            tuple_to_int(())

    def test_single_element_input(self):
        self.assertEqual(tuple_to_int((5,)), 5)

    def test_max_value_input(self):
        self.assertEqual(tuple_to_int((9, 9, 9, 9, 9, 9, 9, 9, 9, 9)), 9999999999)

    def test_min_value_input(self):
        self.assertEqual(tuple_to_int((-9, -9, -9, -9, -9, -9, -9, -9, -9, -9)), -9999999999)

    def test_mixed_sign_input(self):
        self.assertEqual(tuple_to_int((-1, 2, -3, 4, -5)), -1234)

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            tuple_to_int(("a", "b", "c"))

    def test_long_input(self):
        self.assertEqual(tuple_to_int((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)), 1234567891011)
