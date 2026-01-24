import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_even([1, 2, 3, 4]), [1, 3])

    def test_empty_list(self):
        self.assertEqual(remove_even([]), [])

    def test_all_even(self):
        self.assertEqual(remove_even([2, 4, 6]), [])

    def test_all_odd(self):
        self.assertEqual(remove_even([1, 3, 5]), [1, 3, 5])

    def test_mixed_numbers(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_single_even_number(self):
        self.assertEqual(remove_even([2]), [])

    def test_single_odd_number(self):
        self.assertEqual(remove_even([1]), [1])

    def test_large_numbers(self):
        self.assertEqual(remove_even(list(range(1, 101))), list(range(1, 101, 2)))

    def test_negative_numbers(self):
        self.assertEqual(remove_even([-2, -4, -6]), [])

    def test_mixed_negative_numbers(self):
        self.assertEqual(remove_even([-1, -2, -3, -4]), [-1, -3])

    def test_duplicates(self):
        self.assertEqual(remove_even([2, 2, 4, 4]), [])

    def test_duplicates_mixed(self):
        self.assertEqual(remove_even([1, 2, 2, 3, 4, 4]), [1, 3])
