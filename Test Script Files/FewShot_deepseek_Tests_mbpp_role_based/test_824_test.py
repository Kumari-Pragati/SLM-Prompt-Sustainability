import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_even([1, 2, 3, 4]), [1, 3])

    def test_empty_list(self):
        self.assertEqual(remove_even([]), [])

    def test_list_with_only_even_numbers(self):
        self.assertEqual(remove_even([2, 4, 6]), [])

    def test_list_with_only_odd_numbers(self):
        self.assertEqual(remove_even([1, 3, 5]), [1, 3, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_even([1, 2, 2, 3, 4]), [1, 3])

    def test_large_list(self):
        self.assertEqual(remove_even(list(range(1, 101))), list(range(1, 101, 2)))

    def test_negative_numbers(self):
        self.assertEqual(remove_even([-1, -2, -3, -4]), [-1, -3])

    def test_mixed_numbers(self):
        self.assertEqual(remove_even(list(range(-10, 11))), list(range(-10, 11, 2)))
