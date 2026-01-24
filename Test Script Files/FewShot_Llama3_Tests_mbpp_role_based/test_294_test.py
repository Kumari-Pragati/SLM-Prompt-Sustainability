import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_val([]))

    def test_list_with_non_integers(self):
        self.assertIsNone(max_val([1, 2, 'a', 4, 5]))

    def test_list_with_single_integer(self):
        self.assertEqual(max_val([1]), 1)

    def test_list_with_multiple_integers(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5, 6]), 6)

    def test_list_with_negative_numbers(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)
