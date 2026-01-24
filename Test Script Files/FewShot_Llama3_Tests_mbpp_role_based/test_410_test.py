import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)

    def test_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_list_with_non_integers(self):
        self.assertIsNone(min_val([1, 2, 'a', 4, 5]))

    def test_list_with_single_element(self):
        self.assertEqual(min_val([1]), 1)

    def test_list_with_duplicates(self):
        self.assertEqual(min_val([1, 1, 2, 3, 4]), 1)

    def test_list_with_negative_numbers(self):
        self.assertEqual(min_val([-1, -2, -3, 4, 5]), -3)
