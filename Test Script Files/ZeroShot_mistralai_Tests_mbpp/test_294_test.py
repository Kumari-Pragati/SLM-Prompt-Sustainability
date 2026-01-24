import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_val([]))

    def test_list_with_non_integer(self):
        self.assertIsNone(max_val([1, 'a', 3]))

    def test_list_with_only_integer(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_list_with_negative_and_positive_integers(self):
        self.assertEqual(max_val([-5, -3, -1, 1, 3, 5]), 5)

    def test_list_with_floats(self):
        self.assertEqual(max_val([1.1, 2.2, 3.3]), 3.3)

    def test_list_with_large_numbers(self):
        self.assertEqual(max_val([1000000001, 999999999, 1000000002]), 1000000002)
